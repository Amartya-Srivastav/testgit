def drawField():
    for row in range(9):
        if row % 2 == 0:
            for column in range(9):
                if column % 2 == 0:
                    if column != 8:
                        print(' ', end='')
                    else:
                        print(' ')
                else:
                    print('|', end='')
        else:
            print('-' * 9)


drawField()

player = 1
currentField = [' ', ' ', ' ', ' ', ' ']
drawField()
while (True):
    print(f'Players {player} turn')
    move = int(input('Column: '))
    if player == 1:
        currentField[move] == 'X'
        player = 2
    else:
        currentField[move] == 'O'
    drawField(currentField)