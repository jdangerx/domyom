class Domyom:
    def __init__(self):
        self.last_bought = None

    def action_choice(self, player_info):
        if "Village" in player_info.hand:
            return "Village"
        if "Smithy" in player_info.hand:
            return "Smithy"

    def execute_action_strategy(self, action_name, player_info):
        return "None"

    def total_treasure(self, player_info):
        all_cards = player_info.discard + player_info.hand + player_info.deck
        coppers = len([c for c in all_cards if c == "Copper"])
        silvers = len([c for c in all_cards if c == "Silver"])
        golds = len([c for c in all_cards if c == "Gold"])
        return coppers + 2*silvers + 3*golds

    def buy_choice(self, player_info):
        available_cards = player_info.bank.keys()
        if player_info.treasure >= 8:
            return "Province"
        if player_info.treasure >= 4 and self.last_bought != "Smithy" and "Smithy" in available_cards:
            return "Smithy"
        elif self.total_treasure(player_info) < 8:
            if player_info.treasure >= 3:
                return "Silver"
            else:
                return "Copper"
        elif player_info.treasure >= 3 and self.last_bought != "Village":
            return "Village"
        else:
            return "None"
