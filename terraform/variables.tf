variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project"
  default     = "sentiment-tool"
}

variable "environment" {
  description = "Environment (dev/staging/prod)"
  default     = "prod"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  default     = "10.0.0.0/16"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "key_name" {
  description = "Name of the SSH key pair"
}

variable "allowed_ips" {
  description = "List of IPs allowed to access the EC2 instance"
  type        = list(string)
}