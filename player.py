

class Player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.eq = {}
        self.inv = {}
        self.status_effects = []
        self.job = ''
        self.zone = 'TOWN_MARKET'
        self.game_over = False


player = Player()
