import pygame

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Game")
posx = screen_width // 2
posy = screen_height // 2
posx2 = screen_width // 4
posy2 = screen_height // 4
rad = 40
rad2 = 20
xspeed = 0.1
yspeed = 0.1
xspeed2 = 0.1
yspeed2 = 0.1

running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running :
    for event in pygame.event.get() : #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT : #창을 닫는 이벤트 발생했는가?
            running = False
    
    screen.fill((255, 255, 255))
    posx += xspeed
    posy += yspeed
    posx2 += xspeed2
    posy2 += yspeed2

    if posx + rad >= screen_width or posx - rad <= 0 :
        xspeed *= -1
    if posy + rad >= screen_height or posy - rad <= 0 :
        yspeed *= -1
    if posx2 + rad2 >= screen_width or posx2 - rad2 <= 0 :
        xspeed2 *= -1
    if posy2 + rad2 >= screen_height or posy2 - rad2 <= 0 :
        yspeed2 *= -1
    D = ((posx - posx2) * (posx - posx2) + (posy - posy2) * (posy - posy2))**0.5
    if rad + rad2 > D :
        posx *= -1
        posy *= -1
        posx2 *= -1
        posy2 *= -1
    pygame.draw.circle(screen, (0, 0, 0), (posx, posy), rad)
    pygame.draw.circle(screen, (0, 0, 0), (posx2, posy2), rad2)
    pygame.display.update()


pygame.quit()