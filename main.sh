#!/bin/bash
if [[ "$(uname)" == "Darwin" ]]; then
  python3 src/main.py
else
  python src/main.py
fi
