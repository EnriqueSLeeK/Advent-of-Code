#!/bin/bash

echo "Before using please copy your input to the system clipboard"

#Careful with the because it can overwrite data
#Basic script to create a dir and files
echo "Input day:"
read day

mkdir "$day day"
mkdir "$day day/phase_1"
xclip -o -sel clip > "$day day/phase_1/input"
echo 'with open("input", "r") as f:' > "$day day/phase_1/solver.py"
mkdir "$day day/phase_2"
xclip -o -sel clip > "$day day/phase_2/input"
echo 'with open("input", "r") as f:' > "$day day/phase_2/solver.py"
