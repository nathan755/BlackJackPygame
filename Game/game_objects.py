import pygame
import random
from Game.game_files import *
from Game.settings import *
#rather than importing all this crap, just put it as args in funcs

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.img = images[self.rank + self.suit]
		self.value = values[self.rank]
	def __str__(self):
		return self.suit + self.rank


class Deck:


	def __init__(self):
		self.deck = []

	def create_deck(self):
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))
	
	def shuffle(self):
		random.shuffle(self.deck)

	def give_card(self):
		return self.deck.pop()


class Chip:
	def __init__(self, x, y, value):

		self.x = x
		self.y = y
		self.w = 35
		self.h = 35
		self.value = value
		self.img = chips[self.value]
		self.clicked = False
		self.active = False

	def function(self):
		global bet

		mx, my = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if mx > self.x and mx < self.x + self.w and my > self.y and my < self.y + self.h:
			self.active = True

			if click[0]:
				self.active = False
		else:
			self.active = False		
	
	def draw(self, win):

		chip = pygame.transform.scale(self.img, chip_size)
		big_chip = pygame.transform.scale(self.img, big_chip_size)

		if self.active:
			win.blit(big_chip,(self.x, self.y))
		else:
			win.blit(chip,(self.x, self.y))


class Button:
	def __init__(self, x, y, w, h, colour, active_colour, text,active_text, type_=None):

		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.active_colour = active_colour
		self. colour = colour
		self.text = text
		self.type_ = type_
		self.active = False
		self.clicked = False
		self.active_text = active_text

	def function(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if mouse[0] > self.x and mouse[0] < self.x + self.w and mouse[1] > self.y and mouse[1] < self.y + self.h:
			self.active = True

			if click[0] == 1:
				self.clicked = True
				self.active = False
			else:
				self.clicked = False
		else:
			self.active = False

	def draw(self, win):
		if self.type_ == "btn":
			if self.active:
				win.blit(self.text,(self.x,self.y))
			else:
				win.blit(self.active_text,(self.x,self.y))
		else:	
			if self.active:
				pygame.draw.rect(win, self.active_colour, (self.x,self.y,self.w,self.h))
				
			else:
				pygame.draw.rect(win, self.colour, (self.x,self.y,self.w,self.h))

			if self.type_ == "num":
				win.blit(self.text, ((self.x+12),(self.y+9)))
			else:
				win.blit(self.text, ((self.x),(self.y)))


class Player:
	def __init__(self,type_=None):

		self.hand = []
		
		self.bet = 0
		self.score = 0
		self.aces = 0 
		self.x = 0
		self.y = 0
		self.bust = False
		self.blackjack = False
		self.standing = False
		self.type_ = type_
		self.text_x = 0
		self.text_y = 0
		self.is_on = False
		self.double = False
		self.win = False
		self.push = False
		self.lose = False
		self.made_bet = False
	
	def add_card(self,card):

		self.hand.append(card)
		self.score += card.value

		if card.rank == "ace":
			self.aces += 1

	def ace_adjust(self):
		
		while self.score > 21 and self.aces > 0:
			self.score -= 10
			self.aces -= 1

	def draw_text(self, win):
		global betting

		if betting:
			place_bet = score_font.render("Place your bet!",True,(texas))
			bet_amount = score_font.render("£"+str(self.bet), True, texas)
			win.blit(place_bet,(self.text_x, self.text_y))
			win.blit(bet_amount,(self.text_x,self.text_y-20))
		elif self.win:
			player_win = score_font.render("Player Wins!",True,(texas))
			win.blit(player_win,(self.text_x, self.text_y))
		elif self.push:
			player_push = score_font.render("Push!",True,(texas))
			win.blit(player_push,(self.text_x, self.text_y))
		elif self.lose:
			player_lose = score_font.render("Player Lost!",True,(texas))
			win.blit(player_lose,(self.text_x, self.text_y))
		
		else:
			if self.blackjack:
				blackjack_text = score_font.render("Blackjack",True,(texas))
				win.blit(blackjack_text,(self.text_x, self.text_y))
			elif self.bust:
				bust_text = score_font.render("BUST!!",True,(black))
				win.blit(bust_text,(self.text_x, self.text_y))
			else: 
				score_text = score_font.render(str(self.score),True,(black))
				win.blit(score_text,(self.text_x, self.text_y))