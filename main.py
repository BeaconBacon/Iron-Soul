import pygame, sys
from settings import *
from level import Level


class Game:
    def __init__(self):
        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH), pygame.RESIZABLE)
        pygame.display.set_caption('Iron Soul')
        self.clock = pygame.time.Clock()
        self.start_screen()
        self.level = Level()
        self.main_sound = pygame.mixer.Sound('audio/main.ogg')
        self.main_sound.set_volume(0.1)
        self.main_sound.play(loops = -1)
        
        
		
        
		#sound


    def start_screen(self):
        font = pygame.font.Font('graphics/font/joystix.ttf', 40)
        title = font.render('IRON SOUL', True, (255, 255, 255))
        prompt = font.render('Press SPACE to Start', True, (255, 255, 255))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return  # exit the start screen loop and start the game

            self.screen.fill((0, 0, 0))  # fill the screen with black
            self.screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGTH / 3))
            self.screen.blit(prompt, (WIDTH / 2 - prompt.get_width() / 2, HEIGTH / 2))
            pygame.display.update()


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()

            self.screen.fill(WATER_COLOR)

            if self.level.player.health <= 0:
                self.game_over()
            else: 
                self.level.run()
                pygame.display.update()
                self.clock.tick(FPS)

    def game_over(self):
        font = pygame.font.Font('graphics/font/joystix.ttf', 40)
        title = font.render('GAME OVER', True, (255, 255, 255))
        restart_button = font.render('Press R to Restart', True, (255, 255, 255))
        quit_button = font.render('Press Q to Quit', True, (255, 255, 255))
        self.screen.blit(title, (WIDTH / 2 - title.get_width() / 2, HEIGTH / 2 - title.get_height() / 3))
        self.screen.blit(restart_button, (WIDTH / 2 - restart_button.get_width() / 2, HEIGTH / 1.9 + restart_button.get_height()))
        self.screen.blit(quit_button, (WIDTH / 2 - quit_button.get_width() / 2, HEIGTH/ 2 + quit_button.get_height() / 2))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        new_game = Game()
                        new_game.run()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()


if __name__ == '__main__':
    game = Game()
    game.run()
