#!/bin/bash

# Go to your project directory
cd ~/Portfolioproject || { echo "Directory not found!"; exit 1; }

# Update your git repo to latest main branch
git fetch origin main && git reset --hard origin/main

#Spinning any existing containers down to prevent memory issues on vps instances
docker compose -f docker-compose.prod.yml down

#The spin up  new container instances 

docker compose -f docker-compose.prod.yml -d --build 

echo "Redeploy complete. Portfolio service has been restarted."
echo "Check status with: systemctl status myportfolio"
