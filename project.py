import pygame

pygame.init()

height = 500
width = 500

display = pygame.display.set_mode((width,height))
pygame.display.set_caption("make screen")

bg = pygame.transform.scale(pygame.image.load("Screenshot 2025-03-29 171536.png").convert(),(height,width))
image = pygame.transform.scale(pygame.image.load("Screenshot_2025-03-29_172139-removebg-preview.png").convert_alpha(),(200,200))

hitbox = image.get_rect(center = (width // 2,height//2-30))

words = pygame.font.Font(None,28).render("Learn to make games",True ,pygame.Color("white"))
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
