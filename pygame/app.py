import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game")
posx = screen_width // 2
posy = screen_height // 2
xspeed = 0.1
yspeed = 0.01
gravity = 0.0005
pos_easing = 0.003
rad = 20
red = (255 , 0 , 0)
blue = (0 , 0 , 255)
green = (0 , 255 , 0)
color = red

#이벤트 루프
running = True #게임 진행 여부에 대한 변수 True : 게임 진행 중
while running :
    screen.fill((250 , 250 , 250))
    for event in pygame.event.get() : #이벤트의 발생 여부에 따른 반복문
        if event.type == pygame.QUIT : #창을 닫는 이벤트 발생했는가?
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            (x , y) = pygame.mouse.get_pos()
            if temp - length // 2 < x < temp + length // 2 and 570 > y > 500 :
                color = red
            elif temp * 3 - length // 2 < x < temp * 3 + length // 2 and 570 > y > 500 :
                color = green
            elif temp * 5 - length // 2  < x < temp * 5 + length // 2 and 570 > y > 500 :
                color = blue
    
    (targetx, targety) = pygame.mouse.get_pos()
    dx = targetx - posx
    posx += dx * pos_easing
    dy = targety - posy
    posy += dy * pos_easing

    temp = screen_width // 6
    length = 70

    pygame.draw.circle(screen,color,(posx,posy) , rad , 5)
    pygame.draw.rect(screen, red , [temp - length // 2 , 500 , length , length] , 5)
    pygame.draw.rect(screen, green , [temp * 3 - length // 2 , 500 , length , length] , 5)
    pygame.draw.rect(screen, blue , [temp * 5 - length // 2 , 500 , length , length] , 5)
   
    pygame.display.update()

#pygame 종료
pygame.quit()