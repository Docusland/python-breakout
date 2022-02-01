import pygame
from random import randint
from colors import *
from constants import *

class Paddle(pygame.sprite.Sprite):
    """
        This class represents a paddle. The object on which a ball bounces.
        It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.x > SCREEN_WIDTH - PADDLE_WIDTH:
            self.rect.x = SCREEN_WIDTH - PADDLE_WIDTH


class Ball(pygame.sprite.Sprite):
    """
        This class represents a Ball.
        It derives from the "Sprite" class in Pygame.
    """

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the car, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Ball's velocity
        self.velocity :int = [randint(BALL_VELOCITY//2, BALL_VELOCITY),
                              randint(
            -1*BALL_VELOCITY, BALL_VELOCITY)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        """ Executed between each frame. """
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        """ Bounce on walls, bricks or paddle. """

        # Mirror effect on x
        self.velocity[0] = -self.velocity[0]

        # Randomize angle. But should not be null
        self.velocity[1] = randint(-1*BALL_VELOCITY, BALL_VELOCITY)

class Brick(pygame.sprite.Sprite):
    """
        This class represents a brick.
        It derives from the "Sprite" class in  Pygame.
    """

    def __init__(self, color, width, height):
        """ Constructor. """
        super().__init__()
        self.color = color
        # Pass in the color of the brick, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the brick (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()