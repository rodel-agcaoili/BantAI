
        variable "network_acl_id" { default = "stub-id" }
        variable "vpc_id" { default = "stub-vpc" }
        variable "security_group_id" { default = "stub-sg" }
    
resource "aws_network_acl_rule" "deny_malicious_ip" {
  network_acl_id = var.network_acl_id
  rule_number    = 100
  egress         = false
  protocol       = "all"
  rule_action    = "deny"
  cidr_block     = "192.168.1.50/32"
}