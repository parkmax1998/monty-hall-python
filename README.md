# Monty Hall in Python
## The Premise
The Monty Hall problem is a probability puzzle in which is based around the idea of if you should switch doors. The goal of the game is to win a car. There are three doors presented to you and you blindly select one. Afterwards, the host will reveal a door that is guaranteed to not have a car behind it. From there, the host will ask if you'd like to switch.

The confusion caused by this problem becomes evident at this point. Many people would say that switching doors does not matter, as each door has a 1/3 probability of having the car behind it. However, it is best to switch as there is now a 2/3 chance the door you will switch to will have the car behind it.

## The Why
This program was written in order to create a showcase of why one should switch. The player will be prompted to go through the puzzle and can choose to play again. When the player wishes to end, the percentage of times you won by switching and by not switching will appear. This in contrast to the interpretation of the puzzle that switching doesn't matter.

## Under the Hood
This program uses a simple class called "Door" with the properties of "Number," "Selected," "Behind," and "Other." Though simple, this is used to show how objects work in Python classes.

[Wikipedia Source](https://en.wikipedia.org/wiki/Monty_Hall_problem)