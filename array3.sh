#!/bin/bash
PROGDIR=$(dirname "$0")
cd "${PROGDIR}" || exit
source ./venv/bin/active
python3 main.py
deactive