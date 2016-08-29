#!/usr/bin/env python

import sys
import argparse

from functions import load_stronghold, calculate_earnings, save_stronghold, build_stronghold

parser = argparse.ArgumentParser(description='D&D 5e Strongholds Tool')
parser.add_argument('--load_file', type=str, dest='load_file', help='path to an existing stronghold file to load')
parser.add_argument('--weeks', type=int, dest='weeks', help='number of weeks to calculate earnings for')

args = parser.parse_args()

if args.weeks is not None and args.load_file is None:
    print '[!] You must select a load file if you want to calculate earnings'
    sys.exit(0)

s = None

if args.load_file is not None:
    s = load_stronghold(args.load_file)
    print s
    if args.weeks is not None:
        calculate_earnings(s, args.weeks)
else:
    s = build_stronghold()
    print s
    if 'Y' == raw_input('[+] Do you want to save this stronghold (Y/n)? '):
        fn = raw_input('[+] Enter filename to save stronghold as: ')
        save_stronghold(s, fn + '.stronghold')
