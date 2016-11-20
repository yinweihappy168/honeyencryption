# DTE.py

# Implementation of the distribution transforming encoder (DTE)
# using the API for a message space described in probabilityfunctionAPI.py

import random
import probabilityfunctionAPIwei

# Define length of seed space
SEED_SPACE_LENGTH = 64
seed_space = 2**SEED_SPACE_LENGTH - 1

"""
Takes in a message and a MessageSpaceProbabilityFxnsWei object
and returns a corresponding random bit string in
the seed space.
"""
def encode(m, pfxns):
    # get range of seed space to pick random string from
    start = pfxns.cumul_distr(m) * seed_space
    end = int(start + pfxns.prob_distr(m)*seed_space) - 1 
    start = int(start)

    # pick random string from corresponding seed space
    seed = int(random.random() * (end-start) + start)
    
    return seed

"""
Takes in a seed and a MessageSpaceProbabilityFxns object and
runs binary search on pre-calculated inverse sampling table and linear
search to find corresponding message.
"""
def decode(s, pfxns):
    seed_loc = float(s)/seed_space
    cur_prob = 0
    (key, value) = (0, 0)
    with open("cum_prob_table.txt") as f:
    	for line in f:
		(pre_key, pre_value) = (key, value)
		(key, value) = line.strip().split(",")
		cur_prob = float(key)
		if cur_prob > seed_loc:
			return pre_value
		
