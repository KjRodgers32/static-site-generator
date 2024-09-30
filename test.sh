#!/bin/bash
if [[ "$(uname)" == "Darwin" ]]; then
  python3 -m unittest discover -s src
else
  python -m unittest discover -s src
fi
