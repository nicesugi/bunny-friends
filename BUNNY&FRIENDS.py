import pygame
import sys
import random
from time import sleep

# BLACK = (0, 0, 0)
padwidth = 480
padheight = 640

itemsimage = ['item01.png', 'item02.png', 'item03.png', 'item04.png', 'item05.png']  # 5-아이템 이미지
# abataimage = ['ab01.png', 'ab02.png', 'ab03.png', 'ab04.png', 'ab05.png']

def writecount(count):
    global gamepad
    font = pygame.font.Font('PoorStory-Regular.ttf', 20)
    text = font.render('경험치:' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (20, 10))  # 맨 왼쪽 위에

def writeFcount(count):
    global gamepad
    font = pygame.font.Font('PoorStory-Regular.ttf', 20)
    text = font.render('피로도:' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (380, 10))  # 맨 왼쪽 위에

def crash():
    global gamepad
    writecount()





def drawobject(obj, x, y):  # 1-게임에 등장하는 객체를 드로잉
    global gamepad
    gamepad.blit(obj, (x, y))


def initgame():
    global gamepad, clock, background, bunny, items, abata
    pygame.init()
    gamepad = pygame.display.set_mode((padwidth, padheight))  # 1-게임화면설정
    pygame.display.set_caption('BUNNY & FRIENDS.py')  # 1-게임 이름
    background = pygame.image.load('background.png')  # 2-배경 그림
    bunny = pygame.image.load('ab05.png')  # 3-주인공 그림
    # ab1 = pygame.image.load('ab01.png')
    # ab2 = pygame.image.load('ab02.png')
    # ab3 = pygame.image.load('ab03.png')
    # ab4 = pygame.image.load('ab04.png')

    clock = pygame.time.Clock()


def rungame():
    global gamepad, clock, background, bunny, items, crash, abata

    # 전투기 미사일에 운석이 맞을 경우 True
    score = False
    itemcount = 0
    friendcount = 0

    # 3-주인공 크기
    bunnysize = bunny.get_rect().size
    bunnywidth = bunnysize[0]
    bunnyheight = bunnysize[1]

    # 3-주인공 초기 위치(x,y)
    x = padwidth * 0.45
    y = padheight * 0.9
    bunnyX = 0

    # 5-아이템 랜덤 생성
    items = pygame.image.load(random.choice(itemsimage))
    itemssize = items.get_rect().size  # 아이템크기
    itemswidth = itemssize[0]
    itemsheight = itemssize[1]

    # 5-아이템 초기 위치 설정
    itemsX = random.randrange(0, padwidth - itemswidth)
    itemsY = 0  # y는 꼭대기에서 떨어지니까 0
    itemsspeed = 3.5
    isdraw = True


    # 8-아바타
    # ab = pygame.image.load(random.choice(abataimage))
    # absize = ab.get_rect().size  # 아이템크기
    # abwidth = absize[0]
    # abheight = absize[1]
    #
    # # 초기 위치 설정
    # abX = random.randrange(0, padwidth - itemswidth)
    # abY = 0  # y는 꼭대기에서 떨어지니까 0
    # abspeed = 3.5
    # isdraw = True



    ongame = False
    while not ongame:
        for event in pygame.event.get():
            if event.type in [pygame.quit]:  # 1-게임 프로그램 종료
                pygame.quit()
                sys.exit()

            if event.type in [pygame.KEYDOWN]:  # 4-주인공 왼쪽으로 이동
                if event.key == pygame.K_LEFT:
                    bunnyX -= 5

                elif event.key == pygame.K_RIGHT:  # 4-주인공 오른쪽으로 이동
                    bunnyX += 5

        if event.type in [pygame.KEYUP]:  # 4-방향키를 떼면 주인공 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                bunnyX = 0

        drawobject(background, 0, 0)  # 2-배경 화면 그리기

        drawobject(bunny, x, y)  # 3-주인공을 게임 화면의 (x,y)좌표에 그리기



        if isdraw:
            drawobject(items, itemsX, itemsY)  # 5-아이템 그리기
            # drawobject(ab, abX, abY)


            # 4-주인공 위치 재조정
        x += bunnyX  # 키보드로부터 변경된 위치를 x좌표 위치로 발현시켜줌
        if x < 0:  # x가 0보다 작을 경우(=게임 왼쪽끝까지 가는 경우 밖으로 빠지지 않게 고정
            x = 0
        elif x > padwidth - bunnywidth:  # x가 0보다 클 경우(=게임 오른쪽끝까지 가는 경우 밖으로 빠지지 않게 고정
            x = padwidth - bunnywidth


        # 6-충돌인지
        if isdraw == True and y < itemsY + itemsheight:
            if (itemsX > x and itemsX < x + bunnywidth) or \
                    (itemsX + itemswidth > x and itemsX + itemswidth < x + bunnywidth):
                print('crash')
                isdraw = False
                score = True
                itemcount += 1  # 맞았으니까 카운트
                friendcount += 1  # 맞았으니까 카운트

        # 5-아이템이 아래로 내려감
        itemsY += itemsspeed
        print(itemsX, itemsY)

        writecount(itemcount)
        writeFcount(friendcount)

        # 5-아이템이 바닥으로 떨어진
        if itemsY > padheight:  # 5-스피드5로 적용했던걸 rockY에 적용
            # 5-새로운 아이템 랜덤 생성
            items = pygame.image.load(random.choice(itemsimage))
            itemssize = items.get_rect().size
            itemswidth = itemssize[0]
            itemsheight = itemssize[1]

            # 5-아이템 바닥에 떨어지고, 새아이템 위치 재!!설정(위에 초기설정과 동일하지만 필요한 작업)
            itemsX = random.randrange(0, padwidth - itemswidth)
            itemsY = 0
            isdraw = True

        # # 8-충돌인지
        # if isdraw == True and y < abY + abheight:
        #     if (abX > x and abX < x + bunnywidth) or \
        #             (abX + abwidth > x and abX + abwidth < x + bunnywidth):
        #         print('crash')
        #         isdraw = False
        #         score = True
        #         itemcount += 2  # 맞았으니까 카운트
        #         friendcount -= 3  # 맞았으니까 카운트
        #
        #
        # # 8-아이템이 아래로 내려감
        # abY += abspeed
        # print(abX, abY)
        #
        # # 5-아이템이 바닥으로 떨어진
        # if abY > padheight:  # 5-스피드5로 적용했던걸 rockY에 적용
        #     # 5-새로운 아이템 랜덤 생성
        #     ab = pygame.image.load(random.choice(abataimage))
        #     absize = abs.get_rect().size
        #     abwidth = absize[0]
        #     abheight = absize[1]
        #
        #     # 5-아이템 바닥에 떨어지고, 새아이템 위치 재!!설정(위에 초기설정과 동일하지만 필요한 작업)
        #     abX = random.randrange(0, padwidth - abwidth)
        #     abY = 0
        #     isdraw = True

        writecount(itemcount)
        writeFcount(friendcount)

        pygame.display.update()

        clock.tick(60)  # 1-게임화면의 초당 프레임수를 60으로 설정


pygame.quit()  # 1-pygame종료

initgame()
rungame()
