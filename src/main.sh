#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
  echo 'Error: 
    This program runs on Python3, but it looks like Python3 is not installed.
    To install Python, check out https://installpython3.com/' >&2
elif ! python3 -c "import selenium" &> /dev/null; 
then
    echo 'selenium is required but is uninstalled'
elif ! pip3 show beautifulsoup4 &> /dev/null
then
    echo 'beautifulsoup4 is required but is uninstalled'
else
    python3 main.py
fi
  