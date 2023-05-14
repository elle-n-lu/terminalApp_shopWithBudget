#!/bin/bash

# Check if Python3 is installed
if command -v python3 &>/dev/null; then
    echo "Python3 is already installed"
else
    echo "Python3 is not installed, installing it now"
    echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python, check out https://installpython3.com/' >&2
fi

# Create virtual environment
echo "Creating virtual environment"
python3 -m venv myenv
source myenv/bin/activate

# Install Selenium package
echo "Installing Selenium package"
python3 -m pip install selenium

# Install beautifulsoup4 package
echo "Installing lxml package"
python3 -m pip install lxml

# Install beautifulsoup4 package
echo "Installing beautifulsoup4 package"
python3 -m pip install beautifulsoup4

# Run main.py
python3 main.py