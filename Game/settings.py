import pygame
import os

card_size = 50, 80
chip_size = 35, 35
big_chip_size = 40, 40
players = []
wallet = 100
pygame.mixer.init()
pygame.font.init()


# Colours
light_grey = 204, 204, 204
dark_grey = 181, 181, 181
black = 0, 0, 0
yellow = 200, 200, 10
texas = 255, 225, 128
brown =102, 76, 49
dark_brown= 71, 54, 36


# global bools
settings = False
game_on = False
title_on = True
betting = False
endGame = True


# images
title_page = pygame.image.load(os.path.join("images","main_menu.png"))
table = pygame.image.load(os.path.join("images", "table.png"))
table = pygame.image.load(os.path.join("images", "table.png"))


# Sounds
chip_noise = pygame.mixer.Sound("images/final_chip_sound.wav")
card_noise = pygame.mixer.Sound("images/cardSlide3.wav")


# Text Variables / buttons
button_font = pygame.font.SysFont("Arial", 24)
score_font = pygame.font.SysFont("Arial", 20)
small_button_font = pygame.font.SysFont("Arial", 18)
really_small_button_font = pygame.font.SysFont("Arial", 15)
settings_font = pygame.font.SysFont("Arial", 26)
main_menu_font = pygame.font.SysFont("Texas Ranger Regular", 32)
player_font = pygame.font.SysFont("Arial", 22)
sounds_on = button_font.render("ON", True, black)
sounds_off = button_font.render("OFF", True, black)
player_1 = button_font.render("1", True, black)
player_2 = button_font.render("2", True, black)
player_3 = button_font.render("3", True, black)
player_4 = button_font.render("4", True, black)
player_5 = button_font.render("5", True, black)
player_6 = button_font.render("6", True, black)
quit = button_font.render("QUIT", True, black)
deal = button_font.render("DEAL", True, black)
place_bet_txt = button_font.render("BET", True, black)
player_number = settings_font.render("NUMBER OF BOXES? : ", True, yellow)
sounds = settings_font.render("SOUNDS", True, yellow)
play_quit = settings_font.render("DEAL/QUIT" , True, yellow)
play = main_menu_font.render("PRESS SPACE TO PLAY!", True, texas)
pull = small_button_font.render("HIT", True, texas)
stand = small_button_font.render("STAND", True, texas)
double = small_button_font.render("DOUBLE", True, texas)
sPull = really_small_button_font.render("HIT", True, texas)
sStand = really_small_button_font.render("STAND", True, texas)
sDouble = really_small_button_font.render("DOUBLE", True, texas)
turn = score_font.render("Hit, Stand or Double!", True, texas)
bet_amount = score_font.render("Hit, Stand or Double!", True, texas)
play_again = small_button_font.render("Play Again?", True, texas)
sPlay_again =really_small_button_font.render("Play Again?", True, texas)
