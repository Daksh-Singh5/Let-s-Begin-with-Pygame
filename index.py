import pygame

pygame.init()

height = 500
width = 500

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("make screen")

bg = pygame.transform.scale(pygame.image.load("background (1).png").convert(),(height,width))
image = pygame.transform.scale(pygame.image.load("hello penguin.png").convert_alpha(),(200,200))

hitbox = image.get_rect(center = (width // 2,height//2-30))

words = pygame.font.Font(None,28).render("Cool",True ,pygame.Color("black"))
wordsHitBox = words.get_rect(center = (width // 2,height//2-200))

Fps = pygame.time.Clock()
working = True
while working:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            working = False

    display.blit(bg,(0,0))
    display.blit(image,hitbox)
    display.blit(words,wordsHitBox)

    pygame.display.flip()
    Fps.tick(30)

pygame.quit
