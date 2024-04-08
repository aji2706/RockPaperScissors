### Adam Islam ###

import random

handOptions = ["Rock", "Paper", "Scissors"]
nameOptions = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


# Player class that holds a name, the players choice of hand thrown and eliminated status
class Player:
    name = ""
    throw = None
    eliminated = False

    def __init__(self, name):
        self.name = name

    # randomly select from Rock, Paper or Scissors
    def chooseThrow(self):
        self.throw = random.choice(handOptions)


def playGame(playerList):
    # if playerList is only 1, that means only one player is left in the game,
    # and we have a winner!
    while len(playerList) > 1:
        numEliminated = 0
        losingThrow = ""
        throwCounts = {}

        # iterate through all players, and show their hands
        # throwCounts is a dictionary that holds each hand thrown and its frequency
        for player in playerList:
            player.chooseThrow()
            hand = player.throw
            print(f"Player {player.name} threw {hand}")

            if hand in throwCounts:
                throwCounts[hand] += 1
            else:
                throwCounts[hand] = 1

        # one item is thrown by all,we have a tie, and no one is eliminated
        if len(throwCounts) == 1:

            print("We have a tie!")

        # two items thrown, all who threw losing item are eliminated
        elif len(throwCounts) == 2:

            mostThrows = max(throwCounts, key=throwCounts.get)
            leastThrows = min(throwCounts, key=throwCounts.get)

            if (mostThrows == "Scissors" and leastThrows == "Paper") or (
                    mostThrows == "Rock" and leastThrows == "Scissors") or (
                    mostThrows == "Paper" and leastThrows == "Rock"):

                losingThrow = leastThrows
                print(f"{mostThrows} beats {losingThrow}")
            else:
                losingThrow = mostThrows
                print(f"{leastThrows} beats {losingThrow}")

        # all three items thrown
        else:
            maxFreq = max(throwCounts.values())

            winners = [throw for throw, count in throwCounts.items() if count == maxFreq]

            # if two or more throws have a tie, nobody is eliminated
            if len(winners) > 1:
                print("We have a tie!")

            # whichever throw has the highest frequency is the winner
            else:
                mostThrows = max(throwCounts, key=throwCounts.get)

                if mostThrows == "Rock":
                    losingThrow = "Scissors"
                elif mostThrows == "Paper":
                    losingThrow = "Rock"
                elif mostThrows == "Scissors":
                    losingThrow = "Paper"

                print(f"{mostThrows} beats {losingThrow}")

        # Set each eliminated player's status accordingly
        for player in playerList:
            if player.throw == losingThrow:
                player.eliminated = True
                numEliminated += 1

        # Remove eliminated players from game
        playerList = [player for player in playerList if not player.eliminated]
        print(f"Eliminated {numEliminated}")
        print("----------------------")

    if len(playerList) == 1:
        print(f"Player {playerList[0].name} is the winner!")
    else:
        print("No winner!")


if __name__ == '__main__':
    print("Let's play Rock-Paper-Scissors!")
    numPlayers = random.randint(2, 10)
    print(f"CPU has generated {numPlayers} Players\n")

    # add all players to lobby
    playerList = []
    for i in range(numPlayers):
        playerList.append(Player(nameOptions[i]))

    playGame(playerList)
