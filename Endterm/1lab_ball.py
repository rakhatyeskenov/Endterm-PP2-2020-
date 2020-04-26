# Implement a pygame program that: draws(blits) a red ball of size
# 50 x 50 (radius=25) on white background
# when user presses Up, Down,
# Left, Right arrow keys on keyboard, the ball should move by 20 pixels in the
# direction of pressed key
# the ball should not leave the screen, i.e. user input
# that leads the ball to leave of the screen should be ignored — 10 points

import pygame
import random

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60

x = random.randint(0, 700)
y = random.randint(20, 50)

running = True


def generate(x, y):
   screen.blit(screen, (x, y))


playtime = 0.0
while running:
   milliseconds = clock.tick(30)
   playtime += milliseconds / 1000.0
   for event in pygame.event.get():
        # clock.tick(FPS)
      if event.type == pygame.QUIT:
         running = False
   pressed = pygame.key.get_pressed()
   if pressed[pygame.K_UP]:
      y -= 20
   if pressed[pygame.K_DOWN]:
      y += 20
   if pressed[pygame.K_LEFT]:
      x -= 20
   if pressed[pygame.K_RIGHT]:
      x += 20

   # infinite screen
   if x < 0 or x > width:
      x = (x + width) % width
   if y < 0 or y > height:
      y = (y + height) % height
   pygame.display.flip()

   screen.fill((255, 255, 255))
   generate(x, y)
   circle = pygame.draw.circle(screen, (255, 0, 0), (x, y), 25, 25)
   pygame.display.flip()

pygame.quit()
