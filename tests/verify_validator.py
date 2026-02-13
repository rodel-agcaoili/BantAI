from tools.validator import validate_terraform

# Negative Test (Purposely Broken HCL)
broken_hcl = """
resource "aws_security_group_rule" "bad_rule" {
  type        = "ingress"
  from_port   = 80
  # Missing 'to_port' and 'protocol' - This should fail
  cidr_blocks = ["0.0.0.0/0"]
"""

# Positive Test (Valid HCL)
valid_hcl = """
resource "aws_security_group_rule" "good_rule" {
  type              = "ingress"
  from_port         = 80
  to_port           = 80
  protocol          = "tcp"
  cidr_blocks       = ["0.0.0.0/0"]
  security_group_id = "sg-123456"
}
"""

def run_verification():
    print("Starting Validator Verification...")
    
    print("\n--- Test 1: Broken HCL ---")
    is_valid, error = validate_terraform(broken_hcl)
    if not is_valid:
        print(f"✅ Success: Validator caught the error as expected!")
        print(f"Error Message: {error.strip()}")
    else:
        print("❌ Fail: Validator failed to catch the broken code.")

    print("\n--- Test 2: Valid HCL ---")
    is_valid, msg = validate_terraform(valid_hcl)
    if is_valid:
        print(f"✅ Success: Validator confirmed the valid code!")
    else:
        print(f"❌ Fail: Validator rejected valid code. Error: {msg}")

if __name__ == "__main__":
    run_verification()