import pygame
import os

suits = ('hearts', 'dia', 'spades', 'clubs')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
          'jack': 10,
          'queen': 10, 'king': 10, 'ace': 11}


images = {
         "threeclubs" :pygame.image.load(os.path.join("images","3_of_clubs.png")),
         "twoclubs": pygame.image.load(os.path.join("images","2_of_clubs.png")),
         "fourclubs" : pygame.image.load(os.path.join("images","4_of_clubs.png")),
         "fiveclubs" : pygame.image.load(os.path.join("images","5_of_clubs.png")),
         "sixclubs": pygame.image.load(os.path.join("images","6_of_clubs.png")),
         "sevenclubs": pygame.image.load(os.path.join("images","7_of_clubs.png")),
         "eightclubs": pygame.image.load(os.path.join("images","8_of_clubs.png")),
         "nineclubs": pygame.image.load(os.path.join("images","9_of_clubs.png")),
         "tenclubs": pygame.image.load(os.path.join("images","10_of_clubs.png")),
         "jackclubs": pygame.image.load(os.path.join("images","jack_of_clubs2.png")),
         "queenclubs": pygame.image.load(os.path.join("images","queen_of_clubs2.png")),
         "kingclubs": pygame.image.load(os.path.join("images","king_of_clubs2.png")),
         "aceclubs": pygame.image.load(os.path.join("images","ace_of_clubs.png")),
         "twodia": pygame.image.load(os.path.join("images","2_of_diamonds.png")),
         "threedia": pygame.image.load(os.path.join("images","3_of_diamonds.png")),
         "fourdia": pygame.image.load(os.path.join("images","4_of_diamonds.png")),
         "fivedia": pygame.image.load(os.path.join("images","5_of_diamonds.png")),
         "sixdia":   pygame.image.load(os.path.join("images","6_of_diamonds.png")),
         "sevendia": pygame.image.load(os.path.join("images","7_of_diamonds.png")),
         "eightdia": pygame.image.load(os.path.join("images","8_of_diamonds.png")),
         "ninedia": pygame.image.load(os.path.join("images","9_of_diamonds.png")),
         "tendia": pygame.image.load(os.path.join("images","10_of_diamonds.png")),
         "jackdia":pygame.image.load(os.path.join("images","jack_of_diamonds2.png")),
         "queendia" : pygame.image.load(os.path.join("images","queen_of_diamonds2.png")),
         "kingdia": pygame.image.load(os.path.join("images","king_of_diamonds2.png")),
         "acedia": pygame.image.load(os.path.join("images","ace_of_diamonds.png")),
         "twohearts": pygame.image.load(os.path.join("images","2_of_hearts.png")),
         "threehearts": pygame.image.load(os.path.join("images","3_of_hearts.png")),
         "fourhearts": pygame.image.load(os.path.join("images","4_of_hearts.png")),
         "fivehearts": pygame.image.load(os.path.join("images","5_of_hearts.png")),
         "sixhearts": pygame.image.load(os.path.join("images","6_of_hearts.png")),
         "sevenhearts": pygame.image.load(os.path.join("images","7_of_hearts.png")),
         "eighthearts": pygame.image.load(os.path.join("images","8_of_hearts.png")),
         "ninehearts": pygame.image.load(os.path.join("images","9_of_hearts.png")),
         "tenhearts": pygame.image.load(os.path.join("images","10_of_hearts.png")),
         "jackhearts":pygame.image.load(os.path.join("images","jack_of_hearts2.png")) ,
         "queenhearts": pygame.image.load(os.path.join("images","queen_of_hearts2.png")),
         "kinghearts": pygame.image.load(os.path.join("images","king_of_hearts2.png")),
         "acehearts": pygame.image.load(os.path.join("images","ace_of_hearts.png")) ,
         "twospades":pygame.image.load(os.path.join("images","2_of_spades.png")),
         "threespades":pygame.image.load(os.path.join("images","3_of_spades.png")),
         "fourspades":pygame.image.load(os.path.join("images","4_of_spades.png")),
         "fivespades":pygame.image.load(os.path.join("images","5_of_spades.png")),
         "sixspades":pygame.image.load(os.path.join("images","6_of_spades.png")),
         "sevenspades":pygame.image.load(os.path.join("images","7_of_spades.png")),
         "eightspades":pygame.image.load(os.path.join("images","8_of_spades.png")),
         "ninespades":pygame.image.load(os.path.join("images","9_of_spades.png")) ,
         "tenspades": pygame.image.load(os.path.join("images","10_of_spades.png")),
         "jackspades":pygame.image.load(os.path.join("images","jack_of_spades2.png")) ,
         "queenspades":pygame.image.load(os.path.join("images","queen_of_spades2.png")) ,
         "kingspades": pygame.image.load(os.path.join("images","king_of_spades2.png")) ,
         "acespades": pygame.image.load(os.path.join("images","ace_of_spades.png"))
         }


chips = {  
            "1": pygame.image.load(os.path.join("images","chip_1.png")),
            "2": pygame.image.load(os.path.join("images","chip_2.png")),
            "5": pygame.image.load(os.path.join("images","chip_5.png")),
            "25": pygame.image.load(os.path.join("images","chip_25.png")),
            "100": pygame.image.load(os.path.join("images","chip_100.png"))
}

