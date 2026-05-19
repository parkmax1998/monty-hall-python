import random
import time
# import csv
# import pandas
from door import door

def main():
    gamesPlayed = 0
    wins = 0
    keepPlaying = True

    while keepPlaying == True:
        doorList = []
        carDoor = random.randint(1, 3)
        otherDoor = 0
        informed = False

        for i in range(1, 4):
            doorList.append(door(i))
            if i == carDoor:
                doorList[i-1].assign_door('Car')
            else:
                doorList[i-1].assign_door('Donkey')

        selected = int(input("Please select Door 1, Door 2, or Door 3: "))
        for i in range(0, 3):
            if doorList[i].num == selected:
                doorList[i].select_door(True)
            
            # print(f'num: {doorList[i].num}, selected: {doorList[i].selected}, other: {doorList[i].other}, behind: {doorList[i].behind[0]}\n')

        while informed == False:
            i = random.randint(0, 2)
            if doorList[i].behind[0] == 'Donkey' and doorList[i].selected == False:
                print("\nDoor {} contains a donkey behind it.\n".format(doorList[i].num))
                for j in range(0, 3):
                    if j != i and j != selected - 1:
                        otherDoor = j + 1
                informed = True
        
        time.sleep(2)

        switchAnswer = str(input("You have selected Door {}. Would you like to switch doors to Door {}? (Y/N) ".format(selected, otherDoor))).lower()

        if switchAnswer == "y":
            selected = otherDoor

        if doorList[selected - 1].behind[0] == 'Car':
            print("Congratulations! You have gotten the car from door {}.\n".format(doorList[selected - 1].num))
            wins += 1
        else:
            print("Sorry, you lost!\n")

        gamesPlayed = gamesPlayed + 1
        print("Win rate is {}.\n".format((wins/gamesPlayed)))
        print("You have {} wins and {} games played\n".format(wins, gamesPlayed))

        playAgain = str(input("Would you like to play again? (Y/N) ")).lower()
        if playAgain == 'n':
            keepPlaying = False
        elif playAgain == 'y':
            continue
        else:
            print('Please enter either "Y" or "N"')
    print('Thank you for playing!')
    
main()