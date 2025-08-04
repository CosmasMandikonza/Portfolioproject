#!/bin/bash

cd ~/Portfolioproject || { echo "Directory not found!"; exit 1; }

git fetch origin main && git reset --hard origin/main

docker compose -f docker-compose.prod.yml down

docker compose -f docker-compose.prod.yml up -d --build

echo "Redeploy complete. Portfolio service has been restarted."
echo "Check status with: docker ps"

