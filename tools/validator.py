import subprocess
import os

def validate_terraform(hcl_code):
    # Create a temporary directory/file to test the HCL
    os.makedirs("infra/temp_test", exist_ok=True)
    with open("infra/temp_test/remediation.tf", "w") as f:
        f.write(hcl_code)
    
    # Run terraform validate (requires terraform installed in the container)
    result = subprocess.run(
        ["terraform", "validate"], 
        cwd="infra/temp_test", 
        capture_output=True, 
        text=True
    )
    
    if result.returncode == 0:
        return True, "Valid Terraform Code"
    else:
        return False, result.stderr

