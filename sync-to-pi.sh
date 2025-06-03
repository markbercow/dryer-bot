#!/bin/bash

# Your local project directory (edit as needed)
LOCAL_DIR=/mnt/c/Users/mark/Projects/dryer-bot

# Remote Pi info (edit IP and path!)
PI_USER=mark
PI_HOST=dryer
PI_DIR=/home/mark/Projects/

# Rsync options
rsync -avz --delete \
  --exclude='.git' \
  --exclude='*.pyc' \
  --exclude='__pycache__' \
  --exclude='.DS_Store' \
  --exclude='.vscode' \
  --exclude='.venv' \
  "$LOCAL_DIR" "$PI_USER@$PI_HOST:$PI_DIR"
