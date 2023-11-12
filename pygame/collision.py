import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Collision")
x2 = screen_width // 2
y2 = screen_height // 2
pos_easing = 1
black = (0, 0, 0)
color = black

x1, y1, r1 = map(int, input("원1의 중심좌표와 반지름의 길이를 입력하세요 :").split())

pygame.font.init()
my_font = pygame.font.SysFont('malgungothic', 14)


running = True
while running :
    screen.fill((255, 255, 255))
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            running = False


    (x2, y2) = pygame.mouse.get_pos()

    temp = screen_width // 6
    length = 70     
    

    # calculate
    D = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))**0.5
    if D > r1 + 50 :
        text = "충돌하지 않음"
    else:
        text = "충돌함"

    text_surface = my_font.render(text, False, (0, 0, 0))

    screen.blit(text_surface, (0,0))
    pygame.draw.line(screen, color, [x1, y1], [x2, y2], 3 )
    pygame.draw.circle(screen, color, (x1, y1), r1 , 3)
    pygame.draw.circle(screen, color, (x2, y2), 50 , 3)
    pygame.display.update()

pygame.quit()