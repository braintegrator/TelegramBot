#!/bin/bash
echo "Creating project structure..."
mkdir -p images videos
touch quotes.txt .env

echo "Installing dependencies..."
pip install aiogram python-dotenv

echo "Setup complete! Add your BOT_TOKEN to .env and run bot.py"