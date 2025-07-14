#!/bin/bash

# Go to your project directory
cd ~/Portfolioproject || { echo "Directory not found!"; exit 1; }

# Update your git repo to latest main branch
git fetch origin main
git reset --hard origin/main

# Fix SQLite configuration (since git reset reverts it)
sed -i '/# Database configuration/,/print(mydb)/c\
# Database configuration - Using SQLite\
from peewee import SqliteDatabase\
mydb = SqliteDatabase("portfolio.db")\
print("Using SQLite database:", mydb)' app.py

# Activate virtual environment and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Restart myportfolio service
systemctl restart myportfolio

echo "Redeploy complete. Portfolio service has been restarted."
echo "Check status with: systemctl status myportfolio"
