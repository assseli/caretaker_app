#!/bin/zsh
# setup_venv.sh: Set up Python virtual environment and install requirements

# Check for Python 3
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3 is not installed. Please install Python 3 first."
  exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
  python3 -m venv venv
  echo "Virtual environment created in ./venv"
else
  echo "Virtual environment already exists."
fi

# Activate the virtual environment
source venv/bin/activate

echo "Virtual environment activated."

# Install requirements if requirements.txt exists
if [ -f "requirements.txt" ]; then
  pip install --upgrade pip
  pip install -r requirements.txt
  echo "Requirements installed."
else
  echo "requirements.txt not found. Skipping package installation."
fi
