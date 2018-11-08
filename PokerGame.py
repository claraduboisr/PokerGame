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
        if rank.index(self.get_rank()) < rank.index(other.get_rank()):
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

    def is_two_pair(self):
        pairs =0
        for i in range(5):
            for j in range(i + 1, 5):
                if self.cards[i].get_rank() == self.cards[j].get_rank():
                    pairs += 1
        if pairs == 2:
            return True

    def is_three_of_a_kind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank():
                        return True
        return False

    def is_four_of_a_kind(self):
        for i in range(5):
            for j in range(i + 1, 5):
                for k in range(j + 1, 5):
                    for l in range(k + 1, 5):
                        if self.cards[i].get_rank() == self.cards[j].get_rank() == self.cards[k].get_rank() == self.cards[l].get_rank():
                            return True
        return False

    def is_straight(self):
        self.cards.sort()  # order the cards from 4 3 6 5 to 3 4 5 6
        for i in range(4):
            if rank.index(self.cards[i].get_rank()) + 1 != rank.index(self.cards[i + 1].get_rank()):
                # the index of the first one is one less of the next card
                # 1 + 1 != 2 (F)
                # 2 + 1 != 3 (F) ...
                return False
        return True

    def is_flush(self):
        self.cards[0].get_suit()
        for i in range(1,5):
            if self.cards[0].get_suit() == self.cards[1].get_suit() == self.cards[2].get_suit() == self.cards[3].get_suit() == self.cards[4].get_suit():
                return True
            return False

    def is_straight_flush(self):
        self.cards.sort()
        for i in range (5):
            if self.is_straight() and self.is_flush():
                return True
            return False

    def is_high_card(self):
        self.cards.sort()
        return self.cards[4]

    def is_full_house(self):
        self.cards.sort()
        if self.is_three_of_a_kind(): # a = x x x y z & b = z y x x x -- position[2] of a == position[2] of b
            if self.cards[0].get_rank() == self.cards[1].get_rank() and self.cards[len(self.cards) - 1].get_rank() == self.cards[len(self.cards) - 2].get_rank():
                return True
            return False

    def is_royal_flush(self):
        self.cards.sort()
        if self.is_high_card().get_rank() == "A" and self.is_straight_flush():
            return True
        return False


times = 0
result = {"Royal Flush":0,"Straight Flush":0, "Four of a kind":0, "Full House":0,"Flush":0,"Straight":0,"Three of a kind":0,"Two Pair":0,"Pair":0,"High Card":0}

for i in range(1000):
    new_deck = Deck()
    new_deck.shuffle()
    print(new_deck)
    hand = Hand(new_deck)
    print(hand, end="-> ")
    if hand.is_royal_flush():
        print( "Royal Flush")
        result ["Royal Flush"] += 1
    elif hand.is_straight_flush():
        print("Straight Flush")
        result["Straight Flush"] += 1
    elif hand.is_four_of_a_kind():
        print ("Four of a kind")
        result["Four of a kind"] += 1
    elif hand.is_full_house():
        print ("Full House")
        result["Full House"] += 1
    elif hand.is_flush():
        print ("Flush")
        result["Flush"] += 1
    elif hand.is_straight():
        print ("Straight")
        result["Straight"] += 1
    elif hand.is_three_of_a_kind():
        print ("Three of a kind")
        result["Three of a kind"] += 1
    elif hand.is_two_pair():
        print ("Two Pair")
        result["Two Pair"] += 1
    elif hand.is_pair():
        print ("Pair")
        result["Pair"] += 1
    else:
        print ("High Card")
        result["High Card"] += 1

    print (" ")

    times += 1


print ("This is a stimulation of" ,times, "hands")

print (result)

# STATISTICS:

print("Royal Flush", ((result["Royal Flush"]/1000)*100),"%")
print("Straight Flush", (result["Straight Flush"]/1000),"%")
print("Four of a kind", (result["Four of a kind"]/1000),"%")
print("Full House", ((result["Full House"]/1000)*100),"%")
print("Flush", ((result["Flush"]/1000)*100),"%")
print("Straight", ((result["Straight"]/1000)*100),"%")
print("Three of a kind", ((result["Three of a kind"]/1000)*100),"%")
print("Two Pair", ((result["Two Pair"]/1000)*100),"%")
print("Pair", ((result["Pair"]/1000)*100),"%")
print("High Card", ((result["High Card"]/1000)*100),"%")



# Run a stimulation of 10,000 hands. Count the number of times each type of hand occurs. Do some statistical analysis.
# Royal flush +
# Straight flush +
# Four of a kind +
# Full House +
# Flush +
# Straight +
# Three of a kind +
# Two pair +
# Pair +
# High Card +

