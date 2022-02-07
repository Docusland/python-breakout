# Tutorial from : https://www.101computing.net/breakout-tutorial-using-pygame-getting-started/
"""
Breakout game.

"""   
import pygame
from colors import *
from constants import *
from models import Paddle, Ball, Brick

class Game:
    def __init__(self):
        """
            Game constructor.
            This is what is first executed during launch.
        """
        self.score = 0
        self.lives = 3
        self.screen = None # Main pygame application.
        self.carryOn = True # Variable used as game loop. If False, quits the game. 
        self.paddle = self.ball = None

        self.__open_window_interface()
        self.__generate_sprites()
        self.__game_loop()
    def __open_window_interface(self):
        """ Create the application window. """
        pygame.init()
        # Open a new window
        size = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(GAME_TITLE)

    def __generate_sprites(self):
        # This will be a list that will contain all the sprites we intend to use in our game.
        self.all_sprites_list = pygame.sprite.Group()
        self.all_bricks = pygame.sprite.Group()

        # Create the Paddle
        self.paddle = Paddle(LIGHTBLUE, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.rect.x = (SCREEN_WIDTH - PADDLE_WIDTH) / 2
        self.paddle.rect.y = (SCREEN_HEIGHT - BOUNCE_TOP_LIMIT)

        # Create the ball sprite
        self.ball = Ball(WHITE, BALL_WIDTH, BALL_HEIGHT)
        self.ball.rect.x = 345
        self.ball.rect.y = 195

        # Add the paddle and the ball to the list of sprites
        self.all_sprites_list.add(self.paddle)
        self.all_sprites_list.add(self.ball)

        self.__generate_bricks()

    def __generate_bricks(self):
        """ 
            Generate bricks that will be displayed on the starting screen.
            Adds them to the all_sprites_list and all_bricks containers.
        """
        BRICK_WIDTH = 80
        BRICK_HEIGHT = 30
        for i in range(7):
            brick = Brick(RED, BRICK_WIDTH, BRICK_HEIGHT)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 60
            self.all_sprites_list.add(brick)
            self.all_bricks.add(brick)
        for i in range(7):
            brick = Brick(ORANGE, BRICK_WIDTH, BRICK_HEIGHT)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 100
            self.all_sprites_list.add(brick)
            self.all_bricks.add(brick)
        for i in range(7):
            brick = Brick(YELLOW, BRICK_WIDTH, BRICK_HEIGHT)
            brick.rect.x = 60 + i * 100
            brick.rect.y = 140
            self.all_sprites_list.add(brick)
            self.all_bricks.add(brick)

    def check_quit_events(self):
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.carryOn = False  # Flag that we are done so we exit this loop

    def move_paddle_on_key_events(self):
        # Moving the paddle when the use uses the arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.moveLeft(PADDLE_VELOCITY)
        if keys[pygame.K_RIGHT]:
            self.paddle.moveRight(PADDLE_VELOCITY)

    def check_if_ball_bounces_on_wall(self):
        # Check if the ball is bouncing against any of the 4 walls:
        if self.ball.rect.x >= BOUNCE_RIGHT_LIMIT:
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.x <= BOUNCE_LEFT_LIMIT:
            self.ball.velocity[0] = -self.ball.velocity[0]
        if self.ball.rect.y < BOUNCE_TOP_LIMIT:
            self.ball.velocity[1] = -self.ball.velocity[1]

    def check_if_ball_bounces_on_bottom(self):
        if self.ball.rect.y > 590:
            self.ball.velocity[1] = -self.ball.velocity[1]
            self.lives -= 1
            if self.lives == 0:
                # Display Game Over Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("GAME OVER", 1, WHITE)
                self.screen.blit(text, (250, 300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # Stop the Game
                self.carryOn = False

    def check_ball_paddle_collision(self):
        """
            Detect collisions between the ball and the paddles.
        """
        if pygame.sprite.collide_mask(self.ball, self.paddle):
            self.ball.rect.x -= self.ball.velocity[0]
            self.ball.rect.y -= self.ball.velocity[1]
            self.ball.bounce()

    def check_ball_brick_collision(self):
        """
            Check if there is the ball collides with any of bricks
            :return:
        """
        brick_collision_list = pygame.sprite.spritecollide(self.ball,
                                                           self.all_bricks,
                                                           False)
        for brick in brick_collision_list:
            self.ball.bounce()
            self.score += 1
            brick.kill()
            if len(self.all_bricks) == 0:
                # Display Level Complete Message for 3 seconds
                font = pygame.font.Font(None, 74)
                text = font.render("LEVEL COMPLETE", 1, WHITE)
                self.screen.blit(text, (200, 300))
                pygame.display.flip()
                pygame.time.wait(3000)

                # Stop the Game
                self.carryOn = False

    def redraw(self):
        """ Draing the game screen. Launched at each frame. """
        # First, clear the screen to dark blue.
        self.screen.fill(DARKBLUE)
        pygame.draw.line(self.screen, WHITE, [0, 38], [800, 38], 2)

        # Display the score and the number of lives at the top of the screen
        font = pygame.font.Font(None, 34)
        text = font.render(f"Score: {self.score}", 1, WHITE)
        self.screen.blit(text, (20, 10))
        text = font.render(f"Lives: {self.lives}", 1, WHITE)
        self.screen.blit(text, (650, 10))

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        self.all_sprites_list.draw(self.screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    def __game_loop(self):
        """
            Main infinite loop.
            Until carryOn is set to False.
        """

        clock = pygame.time.Clock() # Used to control how fast the screen updates

        while self.carryOn:
            self.check_quit_events()
            self.move_paddle_on_key_events()
            self.all_sprites_list.update()

            self.check_if_ball_bounces_on_wall()
            self.check_if_ball_bounces_on_bottom()

            self.check_ball_paddle_collision()
            self.check_ball_brick_collision()

            self.redraw()

            # --- Limit to 60 frames per second
            clock.tick(FPS)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()

if __name__ == '__main__':
    Game() # Launch the game.