import pygame
from random import randint
pygame.init()

back = (255, 255, 255)
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('dino')

window.fill(back)

fps = pygame.time.Clock()

# sprite
class Hitbox():
    def __init__(self, x, y, width, height):
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(window, (255, 0, 0), self.hitbox)

class Sprite(Hitbox):
    def __init__(self, x, y, width, height, filename):
        Hitbox.__init__(self, x, y, width, height)
        self.image = pygame.image.load(filename)  #Створення картинки

    def show(self):
        self.draw()
        window.blit(self.image, (self.hitbox.x, self.hitbox.y))

dino = Sprite(15, 400, 61, 70, "dino.png")


#появлення кактусів рандомно
cactus_image = ["kaktus.png", "kaktus2.png", "kaktus3.png"]
cactuses = []
for i in range(0, 50):
    cactus = Sprite(510 + 150 * i + randint(10,150), 434, 10, 33,  cactus_image[randint(0, 2)])
    cactuses.append(cactus)



# висота стрибка
jumpCount = 0
jumpMax = 30

move_jump = False
move_s = False

game = True 
while game:
    window.fill(back)
    dino.show()


# пригати і присідати
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if not move_jump and event.key == pygame.K_w:
                move_jump = True
                jumpCount = jumpMax
            if event.key == pygame.K_s:
                move_s = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                dino.hitbox.y = 400
                dino.image = pygame.image.load("dino.png")
                move_s = False

    if move_jump:
        dino.hitbox.y -= jumpCount
        if jumpCount > - jumpMax:
            jumpCount -= 1
        else:
            move_jump = False
    
    if move_s:
        dino.hitbox.y = 414
        dino.image = pygame.image.load("dino1.png")
        
    for cactus in cactuses:
        cactus.hitbox.x -= 2

    for cactus in cactuses:
        cactus.show()

    for cactus in cactuses:
        if dino.hitbox.colliderect(cactus.hitbox):
            pygame.time.delay(2000)
            game = False
        
    
    pygame.display.update()
    fps.tick(40)