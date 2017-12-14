class ai:

    gridWorld = [
        [1000, -2, -2, -2, -2],
        [-2, -2, -2, -2, -2],
        [-2, 500, 500, -2, -2],
        [-2, -2, -2, -2, -25],
        [-50, -2, -2, 200, -2]
    ]

    currentX = 0
    currentY = 0

    def findCurrentState():
        for i in range(5):
            for j in range(5):
                if ai.gridWorld[i][j] == 1000:
                    print('i: ' + str(i) + ' j: ' + str(j))

    def goDown():
        ai.currentX += 1

    def goLeft():
        ai.currentX -= 1

    def goRight():
        ai.currentX += 1

    def printMatrix():
        for i in range(5):
            for j in range(5):
                print(ai.gridWorld[i][j], end='')
                print(' ', end='')
            print('')

    def getCurrentDirection():
        if ai.gridWorld[ai.currentX][ai.currentY - 1]:
            tempUp = ai.gridWorld[ai.currentX][ai.currentY - 1]
            print('tempUp ' + str(tempUp))
        else:
            tempUp = ai.gridWorld[ai.currentX][ai.currentY]
        # tempDown = ai.gridWorld[ai.currentX][ai.currentY + 1]
        # tempLeft = ai.gridWorld[ai.currentX + 1][ai.currentY]
        # tempRight = ai.gridWorld[ai.currentX - 1][ai.currentY]

ai.printMatrix()
ai.getCurrentDirection()
print(ai.gridWorld[0][0-1])