#!/bin/zsh
# setup_mysql.sh: Install and start MySQL server on macOS

# Check if Homebrew is installed
if ! command -v brew >/dev/null 2>&1; then
  echo "Homebrew is not installed. Please install Homebrew first: https://brew.sh/"
  exit 1
fi

# Check if MySQL is installed
if ! brew list | grep -q '^mysql$'; then
  echo "MySQL not found. Installing MySQL..."
  brew install pkg-config mysql
else
  echo "MySQL is already installed."
fi

# Start MySQL service
brew services start mysql

echo "MySQL server started."
echo "To connect:"
echo "  mysql -u root"
echo "To stop MySQL:"
echo "  brew services stop mysql"
