#!/bin/bash
find . -name "__pycache__" -type d -print -exec rm -r "{}" \;
find . -name "machine.log" -print -exec rm -r "{}" \;
