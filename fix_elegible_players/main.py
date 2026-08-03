class Player:
    def __init__(self, name, level, is_premium, is_active):
        self.name = name
        self.level = level
        self.is_premium = is_premium
        self.is_active = is_active


def filter_eligible_players(players):
    eligible_players = []
    for player in players:
        if player.is_active and (player.level >= 10 or player.is_premium):
            eligible_players.append(player)
    return eligible_players
