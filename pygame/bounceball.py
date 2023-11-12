import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game")
posx = screen_width // 2
posy = screen_height // 2
rad = 40
xspeed = 0.1
yspeed = 0.1

running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running :
    for event in pygame.event.get() : #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT : #창을 닫는 이벤트 발생했는가?
            running = False
    
    screen.fill((255, 255, 255))
    posx += xspeed
    posy += yspeed

    if posx + rad >= screen_width :
        xspeed *= -1
    elif posx + rad <= screen_width :
        xspeed *= -1
    if posy + rad >= screen_height :
        yspeed *= -1
    elif posy + rad <= screen_height :
        yspeed *= -1


    pygame.draw.circle(screen, (0, 0, 0), (posx, posy), rad)
    pygame.display.update()


pygame.quit()