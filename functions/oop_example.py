class Player:
    def __init__(self,name):
        self.name = name
        self.power = 5
        self.health = 100
        self.weapon = []


    def create_player(name, power = 5, health= 100):
        Player.name = name
        Player.power = power
        Player.health = health


    def show_stats(player_name):
        print(f"""Player's name = {player_name.name}
Your power = {player_name.power}
your health = {player_name.health}
weapons = {player_name.weapon}
        """)



player1 = Player('enzo')
