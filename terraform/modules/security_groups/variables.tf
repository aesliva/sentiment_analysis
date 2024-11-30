variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  type        = string
}

variable "allowed_ips" {
  description = "List of IPs allowed to access the EC2 instance"
  type        = list(string)
}