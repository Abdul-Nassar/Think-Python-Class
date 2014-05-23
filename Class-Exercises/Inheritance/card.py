import sys
import random

class Card(object):
	s_names = ["clubs", "Diamonds", "Hearts", "Spades"]
	r_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
	
	def __init__(self, s = 0, r = 2):
		self.s = s
		self.r = r
	
	def __str__(self):
		return '%s of %s' % (Card.r_names[self.r], Card.s_names[self.s]
)
	
	def __cmp__(self, other):
		t1 = self.s, self.r
		t2 = other.s, other.r
		return cmp(t1, t2)

class Deck(object):
	def __init__(self):
		self.cards = []
		for s in range(4):
			for r in range(1, 14):
				card = Card(s, r)
				self.cards.append(card)
	
	def __str__(self):
		res = []
		for card in self.cards:
			res.append(str(card))
		return '\n'.join(res)
	
	def add_card(self, card):
		self.cards.append(card)
	
	def rm_card(self, card):
		self.cards.remove(card)
	
	def pop_card(self, i = -1):
		return self.cards.pop(i)
	
	def shuffle(self):
		random.shuffle(self.cards)
	
	def sort(self):
		self.cards.sort()

	def mov_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
	
class Hand(Deck):
	def __init__(self, label = ''):
		self.cards = []
		self.label = label
	
def find_def_class(obj, m_name):
	for t in type(obj).mro():
		if m_name in t.__dict__:
			return t
	return None

if __name__=='__main__':
	deck = Deck()
	deck.shuffle()
	
	hand = Hand()
	print find_def_class(hand, 'shuffle')
	
	deck.mov_cards(hand, 5)
	hand.sort()
	print hand
