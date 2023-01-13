from player import Player
from weap import Weapon
import random
rounds = 1
player1 = Player(input("player1 name > "))
player2 = Player(input("player2 name > "))
axe = Weapon("axe", 10)
player1.get_weapon(axe)
player2.get_weapon(axe)
while rounds != 21:
    print(f"""Round {rounds}, fight
""")
    print("Player 1, your turn, current stats")
    Player.show_info(player1)
    print("")
    cmd = input("[P1] attack, heal or charge? > ")
    if cmd.lower() == "attack":
        player1.attack(player2, axe)
    elif cmd.lower() == "heal":
        player1.health += 15
        print(f"current health is {player1.health}")
    elif cmd.lower() == "charge":
        player1.strength += 10
        if player1.strength > 50:
            player1.strength = 50
            print("maximum charge reached")
        print("current strength", player1.strength)
    else:
        print("unknown command you lost your turn")
    if player2.health <= 0:
        status = ['last stand','dead','aw','23','35','24']
        rand = random.choice(status)
        if rand != "last stand":
            print(f"{player2.name} lost, Congrats {player1.name}")
            break
        else:
            print("Random revival, must heal")
            player2.health = 5

    print("Player 2, your turn, current stats")
    Player.show_info(player2)
    print("")
    cmd = input("[P2] attack, heal or charge? > ")
    if cmd.lower() == "attack":
        player2.attack(player1, axe)
        print(player1.health)
    elif cmd.lower() == "heal":
        player2.health += 15
        print(f"current health is {player2.health}")
    elif cmd.lower() == "charge":
        player2.strength += 10
        if player2.strength > 50:
            player2.strength = 50
            print("maximum charge reached")
        print("current strength",player2.strength)
    else:
        print("unknown command you lost your turn")
    if player1.health <= 0:
        status = ['last stand','dead','aw','23','35','24']
        rand = random.choice(status)
        if rand != "last stand":
            print(f"{player1.name} lost, Congrats {player2.name}")
            break
        else:
            print("Random revival, must heal")
            player1.health = 5

    rounds += 1
    if rounds == 21:
        print("Maximum rounds reached, game draw")
        break


