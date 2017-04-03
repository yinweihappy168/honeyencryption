# credit_card.py

# Creation of the proper probability functions required
# (cumul_distr, prob_distr, next_message, get_inverse_cumul_distr_samples)
# to create a MessageSpaceProbabilityFxns object that represents
# the message space of credit cards.

"""
Requires: 

Dictionary of prefix-probabilities {'prefix',prob(prefix)}, where sum of all prob(prefix) = 1
Dictionary of prefix-lengths {'prefix',length}, where length = number of digits in credit cards with prefix 'prefix'

"""

from probabilityfunctionAPIwei import MessageSpaceProbabilityFxnsWei
import math

# helper function to get denominator of prefix probabilities
def getTotalProbability():
    sum = 4
    return sum

"""
Creates prefix cumulative probability distribution

def get_cumul_prob(mesg, sum):
    with open("password.txt") as f:
	i = 0;
    	for line in f:
		i = i + 1
		if line.strip() == str(mesg):
			return i*(float(1)/sum)


Creates list of ordered prefixes

def create_prefix_ordered_list():
    lines = [line.rstrip('\n') for line in open('filename')]
    return lines
"""

class TelNOProbabilityFxns(MessageSpaceProbabilityFxnsWei):

    def __init__(self):
        self.sum = getTotalProbability()
        self.pdfdic = {'Cappuccino': 0.5, 'Espresso': 0.25, 'Latte': 0.125, 'Mocha': 0.125}
	self.cdfdic = {'Cappuccino': 0.5, 'Espresso': 0.75, 'Latte': 0.875, 'Mocha': 1}

        # define probability distribution fxn
        # this actually doesn't depend on the prefix but only the length of the string....
        # whatever
        def prob(self, m):
            return self.pdfdic[m]
            

        # define cumul distribution fxn
        def cumul(self, m):
            return self.cdfdic[m]

        # define next message fxn
        # simplified to never carry over to another prefix
        def next_msg(self,m):
	    return None


        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxnsWei.__init__(self, cumul, prob, next_msg)

    
