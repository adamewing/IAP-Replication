#!/usr/bin/env python

import sys


def compress_info(info, strain_list):
    summary = []
    for i, call in enumerate(info):
        if call in ('1', 'INS'): summary.append(strain_list[i])

    return ','.join(summary)


if len(sys.argv) == 2:
    with open(sys.argv[1], 'r') as bed:
        for line in bed:
            if line.startswith('chrm'):
                strain_list = line.strip().split()[4:]
            else:
                chrom, start, end, strand = line.strip().split()[:4]
                info = line.strip().split()[4:]

                print '\t'.join((chrom, start, end, strand, compress_info(info, strain_list)))

