import pygame

pygame.init()

#***WINDOW**#
screen = pygame.display.set_mode((420, 625))

pygame.display.set_caption("Tic Tac Toe")


xolist = ["1", "2", "3",

          "4", "5", "6",

          "7", "8", "9"]


match_status = True
play_count = 0

#***TO AVOID MULTIPLE ATTEMPTS IN ONE BOX***#

b0, b1, b2, b3, b4, b5, b6, b7, b8 = True, True, True, True, True, True, True, True, True

#***FIRST TURN***#

turn = "X"

#***INITIALIZING FONTS***#

turn_font = pygame.font.Font("Manterah.ttf", 100)


topbar_font = pygame.font.Font("Manterah.ttf", 32)

#***BACKEND LOGIC***#


def checkvertical():

    if xolist[0] == xolist[3] == xolist[6] == "X"or xolist[1] == xolist[4] == xolist[7] == "X"or xolist[2] == xolist[5] == xolist[8] == "X":
        return "x won"

    elif xolist[0] == xolist[3] == xolist[6] == "O"or xolist[1] == xolist[4] == xolist[7] == "O"or xolist[2] == xolist[5] == xolist[8] == "O":
        return "o won"


def checkhorizontal():

    if xolist[0] == xolist[1] == xolist[2] == "X"or xolist[3] == xolist[4] == xolist[5] == "X"or xolist[6] == xolist[7] == xolist[8] == "X":
        return "x won"

    elif xolist[0] == xolist[1] == xolist[2] == "O"or xolist[3] == xolist[4] == xolist[5] == "O"or xolist[6] == xolist[7] == xolist[8] == "O":
        return "o won"


def checkdiagonal():

    if xolist[0] == xolist[4] == xolist[8] == "X"or xolist[2] == xolist[4] == xolist[6] == "X":
        return "x won"

    elif xolist[0] == xolist[4] == xolist[8] == "O"or xolist[2] == xolist[4] == xolist[6] == "O":
        return "o won"


def checkwin():

    if checkdiagonal() == "x won" or checkhorizontal() == "x won" or checkvertical() == "x won":
        global result
        global match_status

        result = "X   HAS   WON"

        match_status = False

        return result

    elif checkdiagonal() == "o won" or checkhorizontal() == "o won" or checkvertical() == "o won":

        result = "O   HAS   WON"

        match_status = False

        return result


def turn_topbar_text():

    if match_status == True and play_count != 9:

        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 420, 75))
        topbar_text = topbar_font.render(
            str(turn) + "'s Turn", True, (0, 0, 0))
        screen.blit(topbar_text, (150, 20))

    elif match_status == False:

        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 420, 75))
        topbar_text = topbar_font.render(str(result), True, (0, 0, 0))
        screen.blit(topbar_text, (150, 20))

    else:
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 420, 75))
        topbar_text = topbar_font.render("GAME DRAWN", True, (0, 0, 0))
        screen.blit(topbar_text, (150, 20))


def button_click(x, y):
    global play_count
    global turn
    play_count += 1
    if turn == "X":
        x_text = turn_font.render("X", True, (255, 255, 255))
        screen.blit(x_text, (x, y))
        turn = "O"

    else:
        y_text = turn_font.render("O", True, (255, 255, 255))
        screen.blit(y_text, (x, y))
        turn = "X"


running = True


while running:

    turn_topbar_text()

    #***VERTICAL LINES***#
    pygame.draw.line(screen, (255, 255, 255), (147, 100), (147, 598), 1)
    pygame.draw.line(screen, (255, 255, 255), (270, 100), (270, 598), 1)

    #***HORIZONTAL LINES***#
    pygame.draw.line(screen, (255, 255, 255), (25, 266), (395, 266), 1)
    pygame.draw.line(screen, (255, 255, 255), (25, 432), (395, 432), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        mouse_position = pygame.mouse.get_pos()

    #***BUTTON EVENTS***#

        if 25 + 122 > mouse_position[0] > 25 and 100 + 166 > mouse_position[1] > 100 and b0 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 0
                b0 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(60, 150)
                checkwin()

        if 147 + 123 > mouse_position[0] > 147 and 100 + 166 > mouse_position[1] > 100 and b1 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 1
                b1 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(182, 150)
                checkwin()

        if 270 + 125 > mouse_position[0] > 270 and 100 + 166 > mouse_position[1] > 100 and b2 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 2
                b2 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(305, 150)
                checkwin()

        if 25 + 122 > mouse_position[0] > 25 and 266 + 166 > mouse_position[1] > 266 and b3 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 3
                b3 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(60, 316)
                checkwin()

        if 147 + 123 > mouse_position[0] > 147 and 266 + 166 > mouse_position[1] > 266 and b4 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 4
                b4 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(182, 316)
                checkwin()

        if 270 + 125 > mouse_position[0] > 270 and 266 + 166 > mouse_position[1] > 266 and b5 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 5
                b5 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(305, 316)
                checkwin()

        if 25 + 122 > mouse_position[0] > 25 and 432 + 166 > mouse_position[1] > 432 and b6 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 6
                b6 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(60, 482)
                checkwin()

        if 147 + 123 > mouse_position[0] > 147 and 432 + 166 > mouse_position[1] > 432 and b7 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 7
                b7 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(182, 482)
                checkwin()

        if 270 + 125 > mouse_position[0] > 270 and 432 + 166 > mouse_position[1] > 432 and b8 and match_status:

            click = pygame.mouse.get_pressed()
            if click[0] == 1:
                place = 8
                b8 = False
                xolist.pop(place)
                xolist.insert(place, turn)
                button_click(305, 482)
                checkwin()

    pygame.display.update()
