'''
Created on Feb 11, 2017

@author: Pavan
'''

import pygame

pygame.init()

obstacle = pygame.Rect(180, 200, 300, 200)
obstacle1 = pygame.Rect(600, 300, 10, 200)
obstacle2 = pygame.Rect(400, 490, 200, 10)

image_source = pygame.image.load('robot.bmp')
image_dest = pygame.image.load('dest.bmp')

font = pygame.font.SysFont("comicsansms", 18, bold=True)
font1 = pygame.font.SysFont("verdana", 14, bold=True)
textSuccess = font.render(
    "GREAT! Robot Successfully reached to the destination.", True, (0, 128, 0))
textFailure = font.render(
    "SORRY! Robot could not reach to destination.", True, (128, 0, 0))
textToGoal = font.render(
    "ROBOT MOVING TOWARDS DESTINATION.", True, (0, 128, 128))
textNavigate = font.render(
    "ROBOT NAVIGATING THE OBSTACLE.", True, (0, 0, 128))
textBug = font1.render(
    "IMPLEMENTATION OF BUG 2 ALGORITHM", True, (0, 0, 0))
intersect_x = 0
intersect_y = 0

#obstacle = 0


class Robot(object):

    def drawGridLine(self):
        pygame.draw.line(
            screen, 0xcc44cc, (start_x, start_y), (end_x, end_y), 1)
        a = 20
        b = 20
        while a < 960:
            pygame.draw.line(screen, 0xffffff, (a, 0), (a, 720), 1)
            a = a + 20

        while b < 720:
            pygame.draw.line(screen, 0xffffff, (0, b), (960, b), 1)
            b = b + 20

        pygame.draw.rect(screen, 0xffff44, (180, 200, 300, 200), 5)
        pygame.draw.rect(screen, 0xffff44, (600, 300, 10, 200), 1)
        pygame.draw.rect(screen, 0xffff44, (400, 490, 200, 10), 1)
        pygame.draw.line(screen, 0xffff44, (605, 300), (605, 500), 10)
        pygame.draw.line(screen, 0xffff44, (400, 495), (600, 495), 10)
        screen.blit(image_source, (start_x, start_y))
        screen.blit(image_dest, (end_x, end_y))
        screen.blit(textBug, (300, 10))

    def ValidateDest(self, end_x, end_y):
        if((obstacle1.collidepoint(end_x, end_y) == True) or (obstacle2.collidepoint(end_x, end_y) == True)):
            print(
                "Invalid Destination address. Destination must be within free space.")
#            break
        elif((end_x < 600) and end_y < 490):
            pass
            #obstacle = 1
        # elif()

    def bothInside(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0

        m = (end_y - start_y) / (end_x - start_x)

        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            clock.tick(20)

            obstacle = pygame.Rect(180, 200, 300, 200)

            if(image_x < end_x):
                image_x += 1
                image_y += m
            else:
                print("Great! Robot Successfully reached to destination.")
                success = 1

            screen.fill((200, 200, 200))

            Robot.drawGridLine(self)
            screen.blit(image_source, (image_x, image_y))

            if(success == 1):
                screen.blit(textSuccess, (280, 100))
                pygame.display.flip()
                pygame.time.delay(5000)
                break
            screen.blit(textToGoal, (280, 100))
            pygame.display.flip()

    def RobotInside(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0
        p = 0

        m = (end_y - start_y) / (end_x - start_x)
        y_intersect = (m * 480) - (m * start_x) + start_y
        x_intersect = ((400 - start_y) / m) + start_x

        if(y_intersect > 400):
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 400) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                    intersect_x = image_x
                else:
                    if(p == 0):
                        p = 1
                if((image_x + 20 < 480) and p == 1):
                    image_x += 1
                else:
                    if(p == 1):
                        p = 2
                if((image_y - 5 > 200) and p == 2):
                    image_y -= 1
                else:
                    if(p == 2):
                        p = 3
                if((image_x - 5 > 180) and p == 3):
                    image_x -= 1
                else:
                    if(p == 3):
                        p = 4
                if((image_y + 20 < 400) and p == 4):
                    image_y += 1
                else:
                    if(p == 4):
                        p = 5
                if((image_x < intersect_x) and p == 5):
                    image_x += 1
                else:
                    if(p == 5):
                        print("SORRY! Robot could not reach to destination.")
                        success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textFailure, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()
        else:
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 480) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                    intersect_y = image_y
                else:
                    if(p == 0):
                        p = 1
                if((image_y - 5 > 200) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x - 5 > 180) and p == 2):
                    image_x -= 1
                else:
                    if(p == 2):
                        p = 3
                if((image_y + 20 < 400) and p == 3):
                    image_y += 1
                else:
                    if(p == 3):
                        p = 4
                if((image_x + 20 < 480) and p == 4):
                    image_x += 1
                else:
                    if(p == 4):
                        p = 5
                if((image_y > intersect_y) and p == 5):
                    image_y -= 1
                else:
                    if(p == 5):
                        print("SORRY! Robot could not reach to destination.")
                        success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textFailure, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

    def DestInside(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0
        p = 0

        m = (end_y - start_y) / (end_x - start_x)
        y_intersect = (m * 180) - (m * start_x) + start_y
        x_intersect = ((200 - start_y) / m) + start_x

        if(y_intersect < 200):
            while 1:
                for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        return
                    if(event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                    intersect_x = image_x
                else:
                    if(p == 0):
                        p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                else:
                    if(p == 1):
                        p = 2
                if((image_y < 405) and p == 2):
                    image_y += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_x > 160) and p == 3):
                    image_x -= 1
                else:
                    if(p == 3):
                        p = 4
                if((image_y > 180) and p == 4):
                    image_y -= 1
                else:
                    if(p == 4):
                        p = 5
                if((image_x < intersect_x) and p == 5):
                    image_x += 1
                else:
                    if(p == 5):
                        print("SORRY! Robot could not reach to destination.")
                        success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textFailure, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()
        else:
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                    intersect_y = image_y
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 185) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_y < 405) and p == 3):
                    image_y += 1
                else:
                    if(p == 3):
                        p = 4
                if((image_x > 160) and p == 4):
                    image_x -= 1
                else:
                    if(p == 4):
                        p = 5
                if((image_y > intersect_y) and p == 5):
                    image_y -= 1
                else:
                    if(p == 5):
                        print("SORRY! Robot could not reach to destination.")
                        success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textFailure, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

    def BothOutside(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0
        p = 0

        m = (end_y - start_y) / (end_x - start_x)
        y_intersect = (m * 180) - (m * start_x) + start_y
        x_intersect = ((200 - start_y) / m) + start_x

        y_intersect1 = (m * 480) - (m * start_x) + start_y
        x_intersect1 = ((400 - start_y) / m) + start_x

        y_intersect2 = (m * 600) - (m * start_x) + start_y
        x_intersect2 = ((490 - start_y) / m) + start_x

        if((y_intersect < 200) and (y_intersect1 < 400) and (y_intersect2 < 490)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 0):
                    p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                elif(p == 1):
                    p = 2
                if((image_y < y_intersect1) and p == 2):
                    image_y += 1
                elif(p == 2):
                    p = 3
                if((image_x < 580) and p == 3):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 3):
                    p = 4
                if(image_y > 280 and p == 4):
                    image_y -= 1
                elif(p == 4):
                    p = 5
                if(image_x < 615 and p == 5):
                    image_x += 1
                elif(p == 5):
                    p = 6
                if((image_y < y_intersect2) and p == 6):
                    image_y += 1
                elif(p == 6):
                    p = 7
                if((image_y < end_y) and p == 7):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 7):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

        elif((y_intersect < 200) and (y_intersect1 < 400) and (y_intersect2 > 490)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 0):
                    p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                elif(p == 1):
                    p = 2
                if((image_y < y_intersect1) and p == 2):
                    image_y += 1
                elif(p == 2):
                    p = 3
                if((image_y < 470) and p == 3):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 3):
                    p = 4
                if(image_x < 580 and p == 4):
                    image_x += 1
                elif(p == 4):
                    p = 5
                if(image_y > 280 and p == 5):
                    image_y -= 1
                elif(p == 5):
                    p = 6
                if(image_x < 615 and p == 6):
                    image_x += 1
                elif(p == 6):
                    p = 7
                if((image_y < 505) and p == 7):
                    image_y += 1
                elif(p == 7):
                    p = 8
                if((image_x > x_intersect2 + 10) and p == 8):
                    image_x -= 1
                elif(p == 8):
                    p = 9
                if((image_y < end_y) and p == 9):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 9):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

        elif((y_intersect < 200) and (y_intersect1 > 400) and y_intersect2 > 490):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                else:
                    if(p == 1):
                        p = 2
                if((image_y < 405) and p == 2):
                    image_y += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_x > x_intersect1) and p == 3):
                    image_x -= 1
                elif(p == 3):
                    p = 4
                if((image_y < 470) and p == 4):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 4):
                    p = 5
                if(image_x < 580 and p == 5):
                    image_x += 1
                elif(p == 5):
                    p = 6
                if(image_y > 280 and p == 6):
                    image_y -= 1
                elif(p == 6):
                    p = 7
                if(image_x < 615 and p == 7):
                    image_x += 1
                elif(p == 7):
                    p = 8
                if((image_y < 505) and p == 8):
                    image_y += 1
                elif(p == 8):
                    p = 9
                if((image_x > x_intersect2 + 5) and p == 9):
                    image_x -= 1
                elif(p == 9):
                    p = 10
                if((image_y < end_y) and p == 10):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 10):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()
        elif((y_intersect > 200) and (y_intersect1 < 400) and (y_intersect2 < 490)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 180) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                elif(p == 2):
                    p = 3
                if((image_y < y_intersect1) and p == 3):
                    image_y += 1
                elif(p == 3):
                    p = 4
                if((image_x < 580) and p == 4):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 4):
                    p = 5
                if(image_y > 280 and p == 5):
                    image_y -= 1
                elif(p == 5):
                    p = 6
                if(image_x < 615 and p == 6):
                    image_x += 1
                elif(p == 6):
                    p = 7
                if((image_y < y_intersect2) and p == 7):
                    image_y += 1
                elif(p == 7):
                    p = 8
                if((image_y < end_y) and p == 8):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 8):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 80))
                    pygame.display.flip()
                    pygame.time.delay(10000)
                    break
                screen.blit(textToPrint, (280, 40))
                pygame.display.flip()
        elif((y_intersect > 200) and (y_intersect1 > 400) and (y_intersect2 < 490)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 180) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_y < 405) and p == 3):
                    image_y += 1
                else:
                    if(p == 3):
                        p = 4
                if((image_x > x_intersect1) and p == 4):
                    image_x -= 1
                else:
                    if(p == 4):
                        p = 5
                if((image_y < 580) and p == 5):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 5):
                    p = 6
                if(image_y > 280 and p == 6):
                    image_y -= 1
                elif(p == 6):
                    p = 7
                if(image_x < 615 and p == 7):
                    image_x += 1
                elif(p == 7):
                    p = 8
                if((image_y < y_intersect2) and p == 8):
                    image_y += 1
                elif(p == 8):
                    p = 9
                if((image_y < end_y) and p == 9):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 9):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(10000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()
        elif((y_intersect > 200) and (y_intersect1 > 400) and (y_intersect2 > 490)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 180) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_y < 405) and p == 3):
                    image_y += 1
                else:
                    if(p == 3):
                        p = 4
                if((image_x > x_intersect1) and p == 4):
                    image_x -= 1
                elif(p == 4):
                    p = 5
                if((image_y < 470) and p == 5):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 5):
                    p = 6
                if(image_x < 580 and p == 6):
                    image_x += 1
                elif(p == 6):
                    p = 7
                if(image_y > 280 and p == 7):
                    image_y -= 1
                elif(p == 7):
                    p = 8
                if(image_x < 615 and p == 8):
                    image_x += 1
                elif(p == 8):
                    p = 9
                if((image_y < 505) and p == 9):
                    image_y += 1
                elif(p == 9):
                    p = 10
                if(image_x > x_intersect2 and p == 10):
                    image_x -= 1
                elif(p == 10):
                    p = 11
                if((image_y < end_y) and p == 11):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 11):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(10000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

    def BothOutsideObst1(self, screen, start_x, start_y, end_x, end_y):

        clock = pygame.time.Clock()

        image_x = start_x
        image_y = start_y
        success = 0
        p = 0

        m = (end_y - start_y) / (end_x - start_x)
        y_intersect = (m * 180) - (m * start_x) + start_y
        x_intersect = ((200 - start_y) / m) + start_x

        y_intersect1 = (m * 480) - (m * start_x) + start_y
        x_intersect1 = ((400 - start_y) / m) + start_x

        if((y_intersect < 200) and (y_intersect1 < 400)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 0):
                    p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                elif(p == 1):
                    p = 2
                if((image_y < y_intersect1) and p == 2):
                    image_y += 1
                elif(p == 2):
                    p = 3
                if((image_y < end_y) and p == 3):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 3):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()

        elif((y_intersect < 200) and (y_intersect1 > 400)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_y + 20 < 200) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_x < 485) and p == 1):
                    image_x += 1
                else:
                    if(p == 1):
                        p = 2
                if((image_y < 405) and p == 2):
                    image_y += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_x > x_intersect1) and p == 3):
                    image_x -= 1
                elif(p == 3):
                    p = 4
                if((image_y < end_y) and p == 4):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 4):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(5000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()
        elif((y_intersect > 200) and (y_intersect1 < 400)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 180) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                elif(p == 2):
                    p = 3
                if((image_y < y_intersect1) and p == 3):
                    image_y += 1
                elif(p == 3):
                    p = 4
                if((image_y < end_y) and p == 4):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 4):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 80))
                    pygame.display.flip()
                    pygame.time.delay(10000)
                    break
                screen.blit(textToPrint, (280, 40))
                pygame.display.flip()
        elif((y_intersect > 200) and (y_intersect1 > 400)):
            while 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        return
                clock.tick(20)

                textToPrint = textNavigate
                if((image_x + 20 < 180) and p == 0):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                else:
                    if(p == 0):
                        p = 1
                if((image_y > 180) and p == 1):
                    image_y -= 1
                else:
                    if(p == 1):
                        p = 2
                if((image_x < 485) and p == 2):
                    image_x += 1
                else:
                    if(p == 2):
                        p = 3
                if((image_y < 405) and p == 3):
                    image_y += 1
                else:
                    if(p == 3):
                        p = 4
                if((image_x > x_intersect1) and p == 4):
                    image_x -= 1
                else:
                    if(p == 4):
                        p = 5
                if((image_y < end_y) and p == 5):
                    image_x += 1
                    image_y += m
                    textToPrint = textToGoal
                elif(p == 5):
                    print(
                        "GREAT! Robot Successfully reached to the destination.")
                    success = 1

                screen.fill((200, 200, 200))

                Robot.drawGridLine(self)
                screen.blit(image_source, (image_x, image_y))

                if(success == 1):
                    screen.blit(textSuccess, (280, 100))
                    pygame.display.flip()
                    pygame.time.delay(10000)
                    break
                screen.blit(textToPrint, (280, 100))
                pygame.display.flip()


if __name__ == '__main__':

    print("\n*** IMPLEMENTATION OF BUG 2 ALGORITHM ***\n")
    print("Working space = 960 * 720")
    print(
        "Two obstacles considered (Closed Rectangular Obstacle: 180,200,480,400 and solid L-shaped obstacle)\n")
    print("There are four options available: ")
    print("\t1. Both, robot and destinations, are inside obstacle")
    print("\t2. Both, robot and destinations, are outside obstacle")
    print("\t3. Robot is inside obstacle and destination is outside")
    print("\t4. Robot is outside obstacle and destination is inside\n")
    print(
        "Provide robot position and destination position accordingly to choose any option")

    start = input("Enter Robot position(x1 y1): ")
    startsplit = start.split()
    if(len(startsplit) < 2):
        print("Invalid Input")
    else:
        start_x = int(startsplit[0])
        start_y = int(startsplit[1])
    end = input("Enter Destination(x2 y2): ")
    endsplit = end.split()
    if(len(endsplit) < 2):
        print("Invalid Input")
    else:
        end_x = int(endsplit[0])
        end_y = int(endsplit[1])

    m = (end_y - start_y) / (end_x - start_x)
    y_inter = (m * 400) - (m * start_x) + start_y
    x_inter = ((300 - start_y) / m) + start_x
    pygame.init()
    screen = pygame.display.set_mode((960, 720))
    pygame.display.set_caption(
        "Implementation of Bug 2 algorithm in Robotics", "Bug 2 Implementation")

    if((obstacle1.collidepoint(end_x, end_y) == True) or (obstacle2.collidepoint(end_x, end_y) == True)):
        print(
            "Invalid Destination address, there is obstacle.\nDestination must be within free space.\n")
        exit(0)
    elif((end_x < 600) and (end_y < 490) and (obstacle.collidepoint(start_x, start_y) == False) and (obstacle.collidepoint(end_x, end_y) == False)):
        Robot().BothOutsideObst1(screen, start_x, start_y, end_x, end_y)
    elif(((y_inter > 500) or (x_inter > 610)) and (obstacle.collidepoint(start_x, start_y) == False) and (obstacle.collidepoint(end_x, end_y) == False)):
        Robot().BothOutsideObst1(screen, start_x, start_y, end_x, end_y)
    elif((obstacle.collidepoint(start_x, start_y) == True) and (obstacle.collidepoint(end_x, end_y) == True)):
        Robot().bothInside(screen, start_x, start_y, end_x, end_y)
    elif((obstacle.collidepoint(start_x, start_y) == True) and (obstacle.collidepoint(end_x, end_y) == False)):
        Robot().RobotInside(screen, start_x, start_y, end_x, end_y)
    elif((obstacle.collidepoint(start_x, start_y) == False) and (obstacle.collidepoint(end_x, end_y) == True)):
        Robot().DestInside(screen, start_x, start_y, end_x, end_y)
    else:
        Robot().BothOutside(screen, start_x, start_y, end_x, end_y)
