import random

def main():
    monty_hall()

def monty_hall():
    doorList = [1, 2, 3]
    carDoor = doorList.pop(random.randrange(len(doorList)))
    otherDoor1 = doorList.pop(random.randrange(len(doorList)))
    otherDoor2 = doorList.pop(random.randrange(len(doorList)))
    selectedDoor = int(input("Please select Door 1, Door 2, or Door 3: "))

    if carDoor == selectedDoor:
        print("Door {} contains a donkey behind it.".format(otherDoor1))
        revealedDoor = otherDoor1
        switchToDoor = otherDoor2
    else:
        for x in range(1, 4):
            if x != selectedDoor and x != carDoor:
                revealedDoor = x
        for x in range(1, 4):
            if revealedDoor != x and selectedDoor != x:
                switchToDoor = x
        print("Door {} contains a donkey".format(revealedDoor))

    switchAnswer = str(input("You have selected Door {}. Would you like to switch doors to Door {}? (Y/N)".format(selectedDoor, switchToDoor)))
    if switchAnswer == "Y":
        selectedDoor = switchToDoor

    if selectedDoor == carDoor:
        print("Congratulations! You have gotten the car from door {}.".format(selectedDoor))
    else:
        print("Sorry, you lost!")

    playAgain = str(input("Would you like to play again? (Y/N) "))
    if playAgain == "Y":
        monty_hall()

main()