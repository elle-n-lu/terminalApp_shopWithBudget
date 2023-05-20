#!/bin/bash

# Check if Python3 is installed
if ! command -v python3 &>/dev/null;
then
    echo "Python3 is not installed, installing it now"
    echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python, check out https://installpython3.com/' >&2
fi
# Create virtual environment
if ! source myenv/bin/activate 2>/dev/null
then   
    echo "Creating virtual environment"
    python3 -m venv myenv
    source myenv/bin/activate
fi

# Install pytest
if ! python3 -c "import pytest" &> /dev/null
then 
    echo "Installing pytest"
    python3 -m pip install -r requirements.txt

fi

python3 main.py 

