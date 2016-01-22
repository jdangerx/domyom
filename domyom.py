from collections import namedtuple

Card = namedtuple("Card", ["category", "gold", "vp", "actions", "buys", "cards", "strategy"])


class Domyom:
    card_info = {
        'Copper': Card("treasure", gold=1, vp=0, actions=0, buys=0, cards=0, strategy=lambda _: "None"),
        'Silver': Card("treasure", gold=2, vp=0, actions=0, buys=0, cards=0, strategy=lambda _: "None"),
        'Gold': Card("treasure", gold=3, vp=0, actions=0, buys=0, cards=0, strategy=lambda _: "None"),

        'Estate': Card("victory", gold=0, vp=1, actions=0, buys=0, cards=0, strategy=lambda _: "None"),
        'Duchy': Card("victory", gold=0, vp=3, actions=0, buys=0, cards=0, strategy=lambda _: "None"),
        'Province': Card("victory", gold=0, vp=6, actions=0, buys=0, cards=0, strategy=lambda _: "None"),

        'Village': Card("action", gold=0, vp=0, actions=2, buys=0, cards=1, strategy=lambda _: "None"),
        # 'Chapel' 
        # 'Workshop'
        # 'Smithy'
        # 'Money Lender'
        # 'Remodel'
        # 'Feast'
        # 'Market'
        # 'Festival'
        # 'Laboratory'
    }
    def action_choice(self, player_info):
        pass

    def execute_action_strategy(self, action_name, player_info):
        self.card_info.get(action_name).strategy(player_info)

    def buy_choice(self, player_info):
        available_cards = player_info.bank.keys()
