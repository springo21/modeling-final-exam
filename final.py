import random
import matplotlib.pyplot as plt


class Card:
    SUITS = ["♣", "♦", "♥", "♠"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise Exception(f"Invalid rank, must be one of {self.RANKS}")
        if suit not in self.SUITS:
            raise Exception(f"Invalid suit, must be one of {self.SUITS}")
        self._rank = rank
        self._suit = suit

    def __gt__(self, other):
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def __str__(self):
        return f"{self.rank}{self.suit}"

    def __repr__(self):
        return self.__str__()


class Deck:
    def __init__(self):
        cards = []
        # iterate over all rank and suits, created a card and add it to the list
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                card = Card(rank, suit)
                cards.append(card)
        self._cards = tuple(cards)

    @property
    def cards(self):
        return self._cards

    def __str__(self):
        return str(self.cards)

    def shuffle(self):
        cards = list(self.cards)
        random.shuffle(cards)
        self._cards = tuple(cards)


class Hand:
    def __init__(self, deck):
        # deck is shuffled before
        cards = []
        for i in range(5):
            cards.append(deck.cards[i])
        self._cards = tuple(cards)

    def __str__(self):
        return str(self._cards)

    @property
    def cards(self):
        return self._cards

    @property
    def is_flush(self):
        suit = self._cards[0].suit
        for i in range(1, 5):
            if self._cards[i].suit != suit:
                return False
        return True

    @property
    def is_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 2:
                return True
        return False

    @property
    def is_3_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 3:
                return True
        return False

    @property
    def is_4_kind(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        for rank in ranks:
            if ranks.count(rank) == 4:
                return True
        return False

    @property
    def is_full_house(self):
        return self.is_3_kind and self.is_pair

    @property
    def is_2_pair(self):
        ranks = []
        for card in self.cards:
            ranks.append(card.rank)
        ranks = set(ranks)
        return len(ranks) == 3 and not self.is_3_kind

    def sort_hand(self):
        cards = list(self.cards)
        cards.sort()
        print(f"sorted hand is: {cards}.")


# precision = tries = 20000
# i = 0
# flush_probability = []
# while True:
#     i = i + 1
#     d = Deck()
#     d.shuffle()
#     hand = Hand(d)
#     if hand.is_flush: #my modification
#         tries -= 1
#
#     if tries == 0:
#         break
#
#     probability = precision /i * 100
#     flush_probability.append(probability)
#
#     if probability >= 99.9:
#         break
#
# print(f"The odds of getting a flush are {probability}%!") #my modification
#
# plt.plot(range(1, precision + 1), flush_probability)
# plt.xlabel('Number of draws')
# plt.ylabel('Probability of Flush (%)')
# plt.title('Flush Probability Simulation')
# plt.show()

precision = 20000
flush_count = 0
flush_probability = []

for i in range(1, precision + 1):
    d = Deck()
    d.shuffle()
    hand = Hand(d)

    # Check for flush
    if hand.is_flush:
        flush_count += 1

    # Calculate and store probability
    probability = flush_count / i * 100
    flush_probability.append(probability)

    # Break out of the loop if desired precision is reached
    if probability >= 99.9:
        break

print(f"The odds of getting a flush after {i} draws are {probability:.2f}%!")

plt.plot(range(1, i + 1), flush_probability)
plt.xlabel('Number of draws')
plt.ylabel('Probability of Flush (%)')
plt.title('Flush Probability Simulation')
plt.show()
