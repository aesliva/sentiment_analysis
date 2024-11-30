resource "aws_instance" "app_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id
  key_name      = var.key_name

  vpc_security_group_ids = [var.security_group_id]

  user_data = templatefile("${path.module}/user_data.sh", {})

  root_block_device {
    volume_size = 20 # arbitrary, dont think i need that much space
    volume_type = "gp3"
  }

  tags = {
    Name        = "${var.project_name}-server-${var.environment}"
    Environment = var.environment
  }
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["al2023-ami-2023*-x86_64"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  # ebs to store docker images for persistence
  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
} 