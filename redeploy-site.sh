#!/bin/bash

# Kill all existing tmux sessions (to stop old Flask servers)
tmux kill-server 2>/dev/null

# Go to your project directory
cd ~/Portfolioproject || { echo "Directory not found!"; exit 1; }

# Update your git repo to latest main branch
git fetch origin main
git reset --hard origin/main

# Activate virtual environment and install dependencies
source venv/bin/activate
pip install -r requirements.txt

# Start new detached tmux session that runs the Flask app
tmux new-session -d -s flask-server bash -c '
  cd ~/Portfolioproject
  source venv/bin/activate
  exec flask run --host=0.0.0.0 --port=5000
'

echo "Redeploy complete. Flask app should now be running in tmux session 'flask-server'."

