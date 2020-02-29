#!/usr/bin/env python

import os

orig_txt = input("origin txt file? >>> ")

result_txt = []

prefixs = ['origin_', 'over_sat_', 'under_sat_',
           'over_exp_', 'under_exp_', 'over_ct_', 'under_ct_']

with open(orig_txt, 'r') as orig_f:
    lines = orig_f.read().split('\n')

    for line in lines:
        if line != '':
            for prefix in prefixs:
                result_txt.append(os.path.join(os.path.dirname(line),
                                               prefix + os.path.basename(line)))

obfs_txt = input("obfuscated txt file? >>> ")

with open(obfs_txt, 'w') as obfs_f:
    obfs_f.write('\n'.join(result_txt))

print("done")
