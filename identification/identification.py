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
    sum = 314686575
    return sum

"""
Creates prefix cumulative probability distribution
"""
def get_cumul_prob(mesg, sum):
    with open("idsorted.txt") as f:
	i = 0;
    	for line in f:
		i = i + 1
		if line.strip() == str(61100120140124017):
			return i*(float(1)/sum)

"""
Creates list of ordered prefixes
"""
def create_prefix_ordered_list():
    lines = [line.rstrip('\n') for line in open('filename')]
    return lines


# given random message string as int, return int message with last digit appended such that new string is Luhn-valid
def luhn(m):
    sum = 0
    for i in list(str(m)):
        sum += int(i)
    last = (9 * sum) % 10
    return m * 10 + last

class IdentificationProbabilityFxns(MessageSpaceProbabilityFxnsWei):

    def __init__(self):
        self.sum = getTotalProbability()

        # define probability distribution fxn
        # this actually doesn't depend on the prefix but only the length of the string....
        # whatever
        def prob(self, m):
            return float(1)/314686575
            

        # define cumul distribution fxn
        def cumul(self, m):
            with open("idsorted.txt") as f:
		i = 0
    	        for line in f:
                    i = i + 1
                    if line.strip() == str(m):
                        return i*(float(1)/314686575)

        # define next message fxn
        # simplified to never carry over to another prefix
        def next_msg(self,m):
            with open("idsorted.txt") as f:
		i = 0
		find = 0
    	        for line in f:
                    i = i + 1
                    if find == 1:
			return line.strip()
                    if line.strip() == str(m):
                        find = 1


        # Initialize MessageSpaceProbabilityFxns
        MessageSpaceProbabilityFxnsWei.__init__(self, cumul, prob, next_msg)

    
