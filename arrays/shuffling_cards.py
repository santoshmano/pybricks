#!/usr/bin/env python3

import random

def shuffle_cards(deck):
    """
    num = len(deck)
    for i in range(num):
        r = random.randint(0, num-i-1)
        deck[r], deck[num-i-1] = deck[num-i-1], deck[r]
    return 
    """
    for i in range(len(deck)):
        r = random.randint(i, len(deck))
        deck[r], deck[i] = deck[i], deck[r]
    return

def shuffle_cards1(deck):


dec = [i for i in range(52)]
for i in range(10):
    deck = [i for i in range(52)]
    print("Deck before shuffling:\n", deck)
    shuffle_cards(deck)
    print("Deck after shuffling:\n", deck)

