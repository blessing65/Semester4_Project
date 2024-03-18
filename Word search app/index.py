#!/usr/bin/env pyton
from flask import Flask
import random
import string

from pprint import pprint


handle = open('/etc/dictionaries-common/words')
words = handle.readlines()
handle.close()

words = [random.choice(words).upper().replace("'",'').strip() \
         for _ in range(5) ]
 
grid_size = 20

grid = [ [ '_' for _ in range(grid_size) ] for _ in range(grid_size) ]

def print_grid():
    for x in range(grid_size):
        print '\t'*8 + ' '.join( grid[x] )

print_grid()