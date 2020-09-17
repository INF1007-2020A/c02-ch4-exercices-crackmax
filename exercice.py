#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):

	return len(string) % 2 == 0



def get_num_char(string, char):
	occurence = 0
	for x in string:
		if x == char:
			occurence +=1

	return occurence





def get_first_part_of_name(name):
	split_name =  name.split('-')[0]
	cap = split_name[0].upper() + split_name[1:].lower()
	return "Bonjour, " + cap


def get_random_sentence(animals, adjectives, fruits):
	basic_sentence = "Aujourd’hui, j’ai vu un %s s’emparer d’un panier %s plein de %s ."

	words = []
	for word_set in (animals, adjectives, fruits):
		words += [word_set[random.randrange(0, len(word_set))]]
	return basic_sentence % tuple(words)

if __name__ == "__main__":
	spam = "Bonjour"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
