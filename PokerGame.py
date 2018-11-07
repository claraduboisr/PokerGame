import random

suits = ["♠", "♥", "♦", "♣"]
rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

    def __lt__(self, other):
        if rank.index(self.get_rank()) < rank.index(other.get_rank)
            return True
        return False


class Deck(object):
    def __init__(self):
        self.cards = []
        for s in suits:
            for r in rank:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def __str__(self):
        deck = ""
        for i in range(0, 52):
            deck += str(self.cards[i]) + " "
        return deck

    def take_one(self):
        return self.cards.pop(0)


class Hand(object):
    def __init__(self, deck):
        self.cards = []
        for i in range(5):
            self.cards.append(deck.take_one())

    def __str__(self):
        hand = ""
        for i in range(5):
            hand += str(self.cards[i]) + " "
        return hand

    def is_pair(self):
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    return True
        return False

    def is_three_of_a_kind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(i + 1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank():
                        return True
        return False

    def is_four_of_a_kind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(i + 1, 5):
                    for l in range(i + 1, 5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank() == \
                                self.cards[l].get_rank():
                            return True
        return False

    def is_straight(self):
        self.cards.sort()  # order the cards from 4 3 6 5 to 3 4 5 6
        for i in range(4):
            if rank.index(self.cards[i]) + 1 != rank.index(self.cards[i + 1]):
                # the index of the first one is one less of the next card
                # 1 + 1 != 2 (F)
                # 2 + 1 != 3 (F) ...
                return False
            return True

    def is_flush(self):
        self.cards[0].get_suit()
        for i in range(1, 4):
            if self.cards[0].get_suit() != self.cards[1].get_suit() != self.cards[2].get_suit() != self.cards[
                3].get_suit() != self.cards[4].get_suit():
                return False
            return True


new_deck = Deck()
new_deck.shuffle()
print(new_deck)
hand = Hand(new_deck)
print(hand)

# Run a stimulation of 10,000 hands. Count the number of times each type of hand occurs. Do some statistical analysis.
# Royal flush
# Straight flush
# Four of a kind +
# Full House
# Flush
# Straight +
# Three of a kind +
# Two pair
# Pair +
# High Card

