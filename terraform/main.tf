provider "aws" {
  region = var.aws_region
}

# VPC and Network Configuration
module "vpc" {
  source = "./modules/vpc"
  
  vpc_cidr        = var.vpc_cidr
  project_name    = var.project_name
  environment     = var.environment
}

# EC2 Instance
module "ec2" {
  source = "./modules/ec2"
  
  project_name    = var.project_name
  environment     = var.environment
  instance_type   = var.instance_type
  vpc_id          = module.vpc.vpc_id
  subnet_id       = module.vpc.public_subnet_ids[0]
  key_name        = var.key_name
  security_group_id = module.security_groups.security_group_id
  
  depends_on = [module.vpc, module.security_groups]
}

# Security Groups
module "security_groups" {
  source = "./modules/security_groups"
  
  vpc_id          = module.vpc.vpc_id
  project_name    = var.project_name
  environment     = var.environment
  allowed_ips     = var.allowed_ips
}