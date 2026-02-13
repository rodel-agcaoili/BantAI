import subprocess
import os
import shutil

def validate_terraform(hcl_code):
    temp_dir = "infra/temp_test"
    os.makedirs(temp_dir, exist_ok=True)
    
    # Write the AI-generated code to a file
    with open(f"{temp_dir}/remediation.tf", "w") as f:
        f.write(hcl_code)
    
    try:
        subprocess.run(["terraform", "init", "-backend=false"], cwd=temp_dir, capture_output=True)
        result = subprocess.run(["terraform", "validate", "-no-color"], cwd=temp_dir, capture_output=True, text=True)
        
        if result.returncode == 0:
            return True, "Valid Terraform Code"
        else:
            return False, result.stderr
    finally:
        # Clean up after validation
        pass