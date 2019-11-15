#!/usr/bin/env python
# coding: utf-8

import os
import sys
import argparse
import seaborn as sn
import pandas as pd


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input',dest='input', type=str, help="Input File", required=True)
parser.add_argument('-o', '--output',dest='output', type=str, help="Output File", required=True)
args = parser.parse_args()

print("%s was your input file, and %s is your output file. Cheers!" % (args.input, args.output))

input = open(args.input, "r")
print("Reading %s as input...\n" % (args.input))
line = input.readline()
print(line)

output = open(args.output, "w")
print("\nWriting %s as output...\n" % (args.output))
output.write("This is the output file. WoWoWoWoW!")
output.close

