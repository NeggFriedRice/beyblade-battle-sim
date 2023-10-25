#!/bin/bash

if ! [[ -x "$(command -v python3)" ]]
then
    echo "Python 3 not detected. Please head to https://www.python.org/downloads/ to download the latest version of Python 3." >&2
    exit 1
fi

python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 main.py
deactivate