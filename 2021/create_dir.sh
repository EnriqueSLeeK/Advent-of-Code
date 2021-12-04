#!/bin/bash

#Basic script to create a dir and files
echo "Input day:"
read day

mkdir "$day day"
mkdir "$day day/phase_1"
> "$day day/phase_1/input"
> "$day day/phase_1/solver.py"
mkdir "$day day/phase_2"
> "$day day/phase_2/input"
> "$day day/phase_2/solver.py"
