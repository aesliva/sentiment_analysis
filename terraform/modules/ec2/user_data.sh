#!/bin/bash
apt-get update
apt-get install -y docker.io docker-compose git

# Add ubuntu user to docker group
usermod -aG docker ubuntu

# Install AWS CLI
apt-get install -y awscli

# Clone application repository
mkdir -p /home/ubuntu/sentiment-tool
cd /home/ubuntu/sentiment-tool
git clone https://github.com/aesliva/sentiment_analysis.git .

# Start Docker services
docker-compose -f docker-compose.prod.yml up -d 