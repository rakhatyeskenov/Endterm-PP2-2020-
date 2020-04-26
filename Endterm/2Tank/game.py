import pygame
pygame.init()

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Tank War")
screen = pygame.Surface((window.get_size()))

bg = pygame.image.load(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\felt_green.jpg')
fps = pygame.time.Clock()

effect = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\move_Sound.wav')
effect.set_volume(0.08)

Gameover_sound = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\gameover_sound.ogg')

fire = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\fire_sound.wav')

explosion = pygame.mixer.Sound(
    r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\explotion_sound.wav')

class Tank1():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.speed = 2
        self.bitmap = pygame.image.load(filename)
        self.const = self.bitmap

    def drawTank1(self):
        screen.blit(self.const, (self.x, self.y))
        return self.x, self.y

    def movementTank1(self, lastMove):
        if lastMove == "up":
            self.const = pygame.transform.rotate(self.bitmap, 0)
            self.y -= self.speed
        elif lastMove == "down":
            self.const = pygame.transform.rotate(self.bitmap, 180)
            self.y += self.speed
        elif lastMove == "left":
            self.const = pygame.transform.rotate(self.bitmap, 90)
            self.x -= self.speed
        elif lastMove == "right":
            self.const = pygame.transform.rotate(self.bitmap, -90)
            self.x += self.speed
        return lastMove

    def InfiniteTank1(self):
        if self.x > 640:
            self.x = -32
        elif self.x < -32:
            self.x = 640
        elif self.y > 480:
            self.y = -32
        elif self.y < -32:
            self.y = 480


class Tank2():
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.speed = 2
        self.bitmap = pygame.image.load(filename)
        self.const = self.bitmap

    def drawTank2(self):
        screen.blit(self.const, (self.x, self.y))
        return self.x, self.y

    def movementTank2(self, lastMove1):
        if lastMove1 == "up":
            self.const = pygame.transform.rotate(self.bitmap, 0)
            self.y -= self.speed
        elif lastMove1 == "down":
            self.const = pygame.transform.rotate(self.bitmap, 180)
            self.y += self.speed
        elif lastMove1 == "left":
            self.const = pygame.transform.rotate(self.bitmap, 90)
            self.x -= self.speed
        elif lastMove1 == "right":
            self.const = pygame.transform.rotate(self.bitmap, -90)
            self.x += self.speed
        return lastMove1

    def InfiniteTank2(self):
        if self.x > 640:
            self.x = -32
        elif self.x < -32:
            self.x = 640
        elif self.y > 480:
            self.y = -32
        elif self.y < -32:
            self.y = 480


class Bullet1():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8

    def move(self):
        if self.direction == "up":
            self.y -= self.vel
        elif self.direction == "down":
            self.y += self.vel
        elif self.direction == "left":
            self.x -= self.vel
        elif self.direction == "right":
            self.x += self.vel

    def leave(self):
        if self.x > 640 or self.x < 0 or self.y > 480 or self.y < 0:
            return True
        return False

    def draw(self, screen):
        self.move()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Bullet2():
    def __init__(self, x, y, radius, color, direction2):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction2 = direction2
        self.vel = 8

    def move2(self):
        if self.direction2 == "up":
            self.y -= self.vel
        elif self.direction2 == "down":
            self.y += self.vel
        elif self.direction2 == "left":
            self.x -= self.vel
        elif self.direction2 == "right":
            self.x += self.vel

    def leave2(self):
        if self.x > 640 or self.x < 0 or self.y > 480 or self.y < 0:
            return True
        return False

    def draw2(self, screen):
        self.move2()
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


def Intersect(x1, y1, w1, h1, x2, y2, w2, h2):
    if (x2 + w2 >= x1 >= x2) and (y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2) and (y2 + h2 >= y1 >= y2):
        return True
    elif (x2 + w2 >= x1 >= x2) and (y2 + h2 >= y1 + h1 >= y2):
        return True
    elif (x2 + w2 >= x1 + w1 >= x2) and (y2 + h2 >= y1 + h2 >= y2):
        return True
    else:
        return False


def pause():
    paused = True
    while paused:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Paused. Press enter to continue', 220, 240, 20)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            paused = False
        pygame.display.update()
        fps.tick(15)


def win(who):
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('WIN: ' + who, 240, 240, 30)
        pygame.display.update()
        fps.tick(15)


def GameOver():
    gameover = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        print_text('Game Over', 240, 240, 30)
        pygame.display.update()
        fps.tick(15)


def print_text(message, x, y, font_size, font_color=(0, 0, 0), font_type=None):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    window.blit(text, (x, y))


def drawWindow():
    tank1.InfiniteTank1()
    tank2.InfiniteTank2()

    screen.blit(bg, (0, 0))

    tank1.drawTank1()
    tank2.drawTank2()

    for bullet in bullets:
        bullet.draw(screen)
    for bullet2 in bullets2:
        bullet2.draw2(screen)

    window.blit(screen, (0, 0))

    print_text('Hp1:= ' + str(Hp1), 10, 10, 25)
    print_text('Hp2:= ' + str(Hp2), 560, 10, 25)
    
    if Intersect(tank1.x, tank1.y, 15, 15, tank2.x, tank2.y, 15, 15) == True: 
        explosion.play()
        Gameover_sound.play()
        GameOver()

    if Hp1 == 0:
        win('Player 1')
    elif Hp2 == 0:
        win('Player 2')

    pygame.display.flip()



tank1 = Tank1(
    100, 240, r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\up_green_tank.png')
tank2 = Tank2(
    500, 240, r'C:\games\Endterm\2Tank\mini_pictures_tank_sounds\up_red_tank.png')

lastMove = "stop"
lastMove1 = "stop"

bullets = []
bullets2 = []

Hp1 = 3
Hp2 = 3

done = True
while done:
    fps.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                effect.play()
                lastMove = "left"
            if e.key == pygame.K_RIGHT:
                effect.play()
                lastMove = "right"
            if e.key == pygame.K_UP:
                effect.play()
                lastMove = "up"
            if e.key == pygame.K_DOWN:
                effect.play()
                lastMove = "down"

            if e.key == pygame.K_a:
                effect.play()
                lastMove1 = "left"
            if e.key == pygame.K_d:
                effect.play()
                lastMove1 = "right"
            if e.key == pygame.K_w:
                effect.play()
                lastMove1 = "up"
            if e.key == pygame.K_s:
                effect.play()
                lastMove1 = "down"

            if e.key == pygame.K_RETURN:
                fire.play()
                direction = lastMove
                if len(bullets) < 10:
                    bullets.append(Bullet1(round(tank1.x + 16 // 2),
                                           round(tank1.y + 16 // 2), 3, (255, 0, 0), direction))
            if e.key == pygame.K_SPACE:
                fire.play()
                direction2 = lastMove1
                if len(bullets2) < 10:
                    bullets2.append(Bullet2(round(tank2.x + 16 // 2),
                                            round(tank2.y + 16 // 2), 3, (0, 0, 255), direction2))

    for bullet in bullets:
        if bullet.leave():
            bullets.remove(bullet)
        if Intersect(bullet.x, bullet.y, 5, 5, tank2.x, tank2.y, 30, 30) == True:
            explosion.play()
            bullets.remove(bullet)
            Hp1 -= 1

    for bullet2 in bullets2:
        if bullet2.leave2():
            bullets2.remove(bullet2)
        if Intersect(bullet2.x, bullet2.y, 5, 5, tank1.x, tank1.y, 30, 30) == True:
            explosion.play()
            bullets2.remove(bullet2)
            Hp2 -= 1

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
        pause()
    lastMove = tank1.movementTank1(lastMove)
    lastMove1 = tank2.movementTank2(lastMove1)
    drawWindow()
