import ollama
import re

class ArchitectAgent:
    def __init__(self, model="codellama"): # Using codellama for better HCL generation
        self.model = model

    def generate_remediation(self, threat_data, error_context=None):
        # Extract the IP if present in the reason
        ip_match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', threat_data['reason'])
        target_ip = ip_match.group(1) if ip_match else "0.0.0.0/0"

        prompt = f"""
        ROLE: Senior AWS Security Architect.
        TASK: Generate a Terraform snippet to EXPLICITLY DENY a malicious IP. Generate ONLY the Terraform resource. 
        If you need to reference a Network ACL, assume the ID is passed as a variable named 'var.network_acl_id' or 
        include a data source for it so the code is syntactically valid on its own.
        TARGET IP: {target_ip}
        
        STRICT RULE: Use an 'aws_network_acl_rule' with 'rule_action = "deny"'. 
        AWS Security Groups do not support deny rules, so we must use a NACL for this remediation.

        FORMAT: Return ONLY the HCL code.
        """

        # This is the "Self-Healing" logic
        if error_context:
            prompt += f"\nPREVIOUS ERROR: The last attempt failed with this error: {error_context}. Please fix the syntax."
        
        output = ollama.generate(
            model=self.model, 
            prompt=prompt,
            options={'num_predict': 300, 'temperature': 0.1}
        )
        
        return output['response'].strip()

if __name__ == "__main__":
    # Mock data from Observer
    mock_threat = {
        "threat_level": "High",
        "reason": "Brute force attack detected from IP 192.168.1.50",
        "suggested_action": "Block the IP"
    }
    
    architect = ArchitectAgent(model="llama3")
    print(f"🛠️ BantAI Proposed Remediation:\n{architect.generate_remediation(mock_threat)}")