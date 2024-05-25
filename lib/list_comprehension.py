#!/usr/bin/env python3

def return_evens(num_list):
    #Return even number in the num_list by checking if num divided by two has a remainder of 0
    return [n for n in num_list if n % 2 == 0]
print(return_evens)

        
    

def make_exclamation(sentence_list):
    # Adds the exclamation to each string in sentence_list
    return [string + '!' for string in sentence_list]
print(make_exclamation)
    