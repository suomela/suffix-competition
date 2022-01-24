#!/usr/bin/env python3

import json
import csv

sample_fields = [ 'corpus', 'genre', 'period', 'sample', 'words', 'year']
token_fields = ['corpus', 'sample', 'dataset', 'token', 'before', 'word', 'after']

def main():
    with open('data.json') as f:
        data = json.load(f)
    with open('samples.csv', 'w', newline='') as f:
        wr = csv.DictWriter(f, sample_fields)
        wr.writeheader()
        for x in data['samples']:
            wr.writerow(x)
    with open('tokens.csv', 'w', newline='') as f:
        wr = csv.DictWriter(f, token_fields)
        wr.writeheader()
        for x in data['tokens']:
            wr.writerow(dict(zip(token_fields, x)))

main()
