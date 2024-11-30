#!/bin/bash
dnf update -y
dnf install -y docker git

# Start and enable Docker
systemctl start docker
systemctl enable docker

# Add ec2-user to docker group
usermod -aG docker ec2-user

# Clone application repository
mkdir -p /home/ec2-user/sentiment-tool
cd /home/ec2-user/sentiment-tool
git clone https://github.com/aesliva/sentiment_analysis.git .

# Install docker-compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# Start Docker services
docker-compose -f docker-compose.prod.yml up -d