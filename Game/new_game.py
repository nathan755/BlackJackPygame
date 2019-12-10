import pygame
import os
from Game.game_objects import Card, Chip, Deck, Player, Button
from Game.game_files import suits, ranks, values, images, chips
from Game.settings import *

pygame.init()

clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 600))
dealer = Player()
place_bet_btn  = Button(700,500,50,40,(dark_grey),(light_grey),place_bet_txt,place_bet_txt)
a = Chip(700,550,"1")
b = Chip(750,550,"2")
c = Chip(800,550,"5")
d = Chip(850,550,"25")
e = Chip(900,550,"100")
chips = [a,b,c,d,e]

def hit(deck,player):
	"""
	deck: Class Deck()
	player: Class Player() 
	Function adds card to player.hand
	
	"""
	single_card = deck.give_card()
	player.add_card(single_card)


def deal_card(deck, player):
	"""
	deck: Deck()
	player: Player()
	function deals two inital cards for each player and one
	card for the dealer, type_ attribute differentiates player form dealer.
	"""
	card1 = deck.give_card()
	card2 = deck.give_card()
	card3 = deck.give_card()
	
	if player.type_:
		player.add_card(card1)
	else:
		player.add_card(card1)

		player.add_card(card2)


def assign_seats(players,dealer):
	"""
	players: List of Player() objects
	dealer: Class Player()
	Function assigns player.x, player.y position, aswell as text.x and text.y position. 
	"""
	seats = [
	[50,250],   #seat 1
	[175,380],  #seat 2 
	[300,450],  #seat 3
	[400,450],  #seat 4
	[600,465],  #seat 5
	[730,375]   #seat 6
	]

	i = 0
	for player in players:
		player.x = seats[i][0]
		player.y = seats[i][1]
		player.text_x = seats[i][0]
		player.text_y = seats[i][1] - 25
		i += 1

	dealer.x, dealer.text_x = 450, 450
	dealer.y, dealer.text_y = 100, 70


def finish_dealer(deck, dealer):
	"""
	deck: Class Deck()
	dealer: Class Player()
	Function deals a card to dealer.hand until dealer.score is >=17
	"""

	while dealer.score < 17:
		pygame.mixer.Sound.play(card_noise)	
		hit(deck,dealer)
		dealer.ace_adjust()


def redraw(players,dealer):
	"""
	players: List of Player() objects
	dealer: Class PLayer ()
	function redraws all cards in dealer and players hands at the appropriate x, y pos
	"""
	global wallet
	wallet_text = score_font.render("Player Funds: £" + str(wallet), True, texas)

	if betting:
		win.blit(wallet_text,(25,25))
	else:

		pygame.Surface.fill(win,(black))

		

		assign_seats(players, dealer) 
		win.blit(table,(0,0))
		win.blit(wallet_text,(25,25))

		
		for player in players:
			count = 0
			if player.double:

				for card in player.hand:
					
					if count == 2:
						card = pygame.transform.scale(card.img,card_size)
						win.blit(pygame.transform.rotate(card,40),(player.x-20, player.y))
						
					else:
						win.blit(pygame.transform.scale(card.img,(card_size)),(player.x, player.y))
						player.draw_text(win)
						player.x += 10
						player.y += 15
						count += 1 
			else:
				for card in player.hand:
					win.blit(pygame.transform.scale(card.img,(card_size)),(player.x, player.y))
					player.draw_text(win)
					player.x += 10
					player.y += 15
			

		for card in dealer.hand:
			win.blit(pygame.transform.scale(card.img,(card_size)),(dealer.x, dealer.y))
			dealer.x += 10

		for player in players:
			if player.is_on:
				win.blit(turn,(player.text_x, player.text_y-20))


def win_check(players,dealer):
	"""
	players: List of Player() Class
	dealer: Class Player()
	Function compares score of each player in players to the dealer score.
	"""
	global wallet
	for player in players:
		if player.score > dealer.score and not player.bust:
			player.win = True
			

		elif not player.bust and dealer.score > 21:
			player.win = True
			
		elif player.score == dealer.score:
			player.push = True
		else:
			player.lose = True


def payout(players,dealer):
	global wallet
	for player in players:
		if player.score > dealer.score and not player.bust:
			wallet += player.bet*2
			
		elif player.score <= 21 and dealer.score > 21:
			wallet += player.bet*2
		elif player.score == dealer.score:
			wallet += player.bet


def reset(players, dealer):
	global bet
	global endGame

	for player in players:
		player.hand = []
		player.chips = 100
		player.bet = 0
		player.score = 0
		player.aces = 0 
		player.x = 0
		player.y = 0
		player.bust = False
		player.blackjack = False
		player.standing = False
	
		player.text_x = 0
		player.text_y = 0
		player.is_on = False
		player.double = False
		player.win = False
		player.push = False
		player.lose = False
		player.made_bet = False
		dealer.hand=[]
		bet = 0


def end(deck,dealer,players):
	"""
	deck: Class Deck()
	dealer: Class Player()
	players: List of player() objects
	Function deals with final stange of game, comparing hands etc
	"""
	global betting
	global endGame
	global game_on
	global wallet

	play_again_btn  = Button(700,500,100,50,(dark_grey),(light_grey),play_again,sPlay_again,"btn")
	while endGame:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				

		redraw(players,dealer)
		finish_dealer(deck,dealer)
		win_check(players,dealer)
		

		

		dealer.draw_text(win)
		play_again_btn.draw(win)
		play_again_btn.function()
		pygame.display.update()
		if play_again_btn.clicked:
			betting = True
			game_on = True
			payout(players,dealer)
			reset(players,dealer)
			run()


def place_bets(players,chips):
	"""
	chips: List of Chip() objects
	function used to place bets for all players/boxs
	"""
	global betting
	global game_on
	global wallet
	


	assign_seats(players,dealer)
	
	wallet_text = score_font.render("Playerspam Funds: £" + str(wallet), True, yellow)
	

	
	while betting:
		
		for player in players:
			while not player.made_bet:
				
				print(wallet)
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.QUIT
						quit()
						

					if event.type == pygame.MOUSEBUTTONDOWN:
						if event.button == 1:
							if place_bet_btn.active:
								player.made_bet = True
							else:
								if a.active:
									player.bet += 1
									wallet -= 1
									pygame.mixer.Sound.play(chip_noise)
								if b.active:
									player.bet += 2
									wallet -= 2
									pygame.mixer.Sound.play(chip_noise)
								if c.active:
									player.bet += 5
									wallet -= 5
									pygame.mixer.Sound.play(chip_noise)
								if d.active:
									player.bet += 25
									wallet -= 25
									pygame.mixer.Sound.play(chip_noise)
								if e.active:
									player.bet += 100
									wallet -= 100 
									pygame.mixer.Sound.play(chip_noise)
							
				pygame.Surface.fill(win,(black))
				win.blit(table,(0, 0))
				for chip in chips:
					chip.draw(win)
					chip.function()

				#a.draw()
				#b.draw()
				#c.draw()
				#d.draw()
				#e.draw()
				#a.function()
				#b.function()
				#c.function()
				#d.function()
				#e.function()

				place_bet_btn.draw(win)
				place_bet_btn.function()
				
				player.draw_text(win)
				print(wallet)
				redraw(players,dealer)
				pygame.display.update()

		else:
			for player in players:
				player.made_bet = False
			betting = False
			game_on = True


def title():
	"""
	Title Page !!
	"""
	global settings
	global title_on
	
	while title_on:
		pygame.display.update()
		win.blit(title_page, (0,0))
		win.blit(play, (350, 550))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				

		keys = pygame.key.get_pressed()
				
		if keys[pygame.K_SPACE]:
			settings = True
			title_on = False
			game_settings()


def game_settings():
	"""
	Depending on what button  the user presses the corresponding number 
	of players will be added to the players list. (this only works if the button 
	type == int)
	"""
	global settings
	global game_on
	global players
	global betting

	btn = {

	"sounds_on" : Button(550,100,50,50,brown,dark_brown,sounds_on,sounds_on),
	"sounds_off" : Button(490,100,50,50,brown,dark_brown,sounds_off,sounds_off),
	"1player" : Button(490,200,50,50,brown,dark_brown,player_1,player_1, 1),
	"2player" : Button(550,200,50,50,brown,dark_brown,player_2,player_2, 2),
	"3player" : Button(610,200,50,50,brown,dark_brown,player_3,player_3 ,3),
	"4player" : Button(490,260,50,50,brown,dark_brown,player_4,player_4, 4),
	"5player" : Button(550,260,50,50,brown,dark_brown,player_5,player_5 ,5),
	"6player" : Button(610,260,50,50,brown,dark_brown,player_6,player_6, 6),
	"quit" : Button(490,400,80,40,brown,dark_brown,quit,quit),
	"deal" : Button(580,400,80,40,brown,dark_brown,deal,deal)

	}
	
	while settings:

		pygame.Surface.fill(win,(0,0,0))
		win.blit(play_quit,(300,400))
		win.blit(player_number,(200, 200))
		win.blit(sounds,(300, 100))
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				settings = False
				pygame.QUIT
				

		for keys, values in btn.items():
			values.function()
			values.draw(win)

			if values.clicked:
				if values.text == deal:
					settings = False
					betting = True
				if values.text == quit:
					pygame.QUIT
					
				try:
					players = [Player() for player in range(values.type_)]
					
				except:
					continue
		pygame.display.update()


def run():
	"""
	Main game loop
	"""
	global game_on
	global wallet
	
	while True:
		title()
		game_settings()
		place_bets(players,chips)
		hit_btn = Button(900,450,50,25,brown,dark_brown,pull,sPull,"btn")
		stand_btn = Button(900,475,50,25,brown,yellow,stand,sStand,"btn")
		double_btn = Button(900,500,50,25,brown,yellow,double,sDouble,"btn")
		dealer = Player(True)
		deck = Deck()
		deck.create_deck()
		deck.shuffle()
		
		for player in players:
			deal_card(deck,player)

			if len(player.hand) == 2 and player.score == 21:
				player.blackjack = True
		deal_card(deck,dealer)
		
		while game_on:
			
			for player in players: 
				while player.score < 21 and not player.standing:
					player.is_on = True
					hit_btn.function()
					stand_btn.function()
					double_btn.function()

					for event in pygame.event.get():
						if event.type == pygame.QUIT:
							pygame.quit()
							
						
						elif event.type == pygame.MOUSEBUTTONDOWN:
							if event.button == 1:
								if hit_btn.active:
									pygame.mixer.Sound.play(card_noise)				

									hit(deck,player)
									player.ace_adjust()
								
								elif stand_btn.active:
									player.standing = True

								elif double_btn.active:
									hit(deck,player)
									pygame.mixer.Sound.play(card_noise)	
									player.double = True
									player.standing = True
									

					redraw(players,dealer)
					hit_btn.draw(win)
					stand_btn.draw(win)
					double_btn.draw(win)
					pygame.display.update()

				if player.score > 21:
					player.bust = True
				player.is_on = False

				
			else:
				game_on = False
				end(deck,dealer,players)















#def play():
    #while True:
        
       # pygame.Surface.fill(win,(black))
        #win.blit(table,(0, 0))
        #pygame.display.update()
        
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.QUIT
                #quit()
                
