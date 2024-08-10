import random

def main():
    gamesPlayed = 0
    wins = 0
    monty_hall(gamesPlayed, wins)

def monty_hall(gamesPlayed, wins):
    doorList = [1, 2, 3]
    carDoor = doorList.pop(random.randrange(len(doorList)))
    otherDoor1 = doorList.pop(random.randrange(len(doorList)))
    otherDoor2 = doorList.pop(random.randrange(len(doorList)))
    selectedDoor = int(input("Please select Door 1, Door 2, or Door 3: "))

    if carDoor == selectedDoor:
        print("Door {} contains a donkey behind it.".format(otherDoor1))
        revealedDoor, switchToDoor = otherDoor1, otherDoor2
        
    else:
        for x in range(1, 4):
            if x != selectedDoor and x != carDoor:
                revealedDoor = x
        for x in range(1, 4):
            if revealedDoor != x and selectedDoor != x:
                switchToDoor = x
        print("Door {} contains a donkey".format(revealedDoor))

    switchAnswer = str(input("You have selected Door {}. Would you like to switch doors to Door {}? (Y/N) ".format(selectedDoor, switchToDoor)))
    if switchAnswer == "Y" or "y":
        selectedDoor = switchToDoor

    if selectedDoor == carDoor:
        print("Congratulations! You have gotten the car from door {}.".format(selectedDoor))
        wins += 1
    else:
        print("Sorry, you lost!")

    gamesPlayed = gamesPlayed + 1
    print("Win rate is {}.".format((wins/gamesPlayed)))
    print("You have {} wins and {} games played".format(wins, gamesPlayed))
    playAgain = str(input("Would you like to play again? (Y/N) "))
    if playAgain != "N" or "n":
        monty_hall(gamesPlayed, wins)

main()
