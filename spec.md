Overview:

A turn in BotDominion consists of two stages, an action phase and a
buy phase.  Your dominion strategy algorithm needs to have 2 functions
for the action phase called action_choice and
action_execute_strategy. The action_choice function will select an
action to play on your turn out of the actions you have available. The
action_execute_strategy function determines how you want an action
played. For the buy phase you just need one function called buy_choice
which will select the card you want to buy in a given situation.

Function parameters: 

All three of your functions need to accept an instance of class
Player_info. The Player_info class instance holds all of the
information you will have available to make decisions on your
turn. The action_execute_strategy function also needs to accept a
string which will be the name of the action you play.

Player_info:
player_info.bank - type: dictionary 
 Holds the number of each card remaining in the bank. The keys for bank are simply the names of the cards.  

player_info.trash - type: dictionary
Holds the number of each card that have been trashed over the course of the game. The keys for trash are simply the names of the cards

player_info.deck - type: list
Lists of the names of all the cards in your deck.

player_info.discard - type: list
Lists of the names of all the cards in your discard pile.

player_info.hand - type: list
Lists of the names of all the cards in your hand.

player_info.actions_played - type: list
Lists of the names of all the action cards you have played on your turn so far.

player_info.opponent_discard - type: list
Lists of the names of all the cards in your opponent's discard pile.

player_info.opponent_hand_deck - type: list
Lists the names of all cards that are in either your opponent’s hand or deck.

player_info.actions_remaining - type: int
Tells you how many more actions you may play on your turn.

player_info.actions_available - type: list
Lists the action cards available in your hand.

player_info.buys - type: int 
Tells you how many more cards you may buy on your turn, which will be 1 unless you played actions that gained you additional buys. 

player_info.treasure - type: int 
Tells you how much treasure you have to spend on your turn. 

I will probably add some common sense methods to the Player_info class that will simplify manipulating the the information inside of it.

Card name strings:
'Copper'
 'Silver'
 'Gold'
 'Estate'
 'Duchy'
'Province'
'Village'
'Chapel' 
'Workshop'
'Smithy'
'Money Lender'
 'Remodel'
 'Feast'
'Market'
 'Festival'
'Laboratory'

If you don’t know what any of these cards do check out the wiki page for an in depth explanation.
http://wiki.dominionstrategy.com/index.php/Dominion_(Base_Set)

If you ever wish to play no more actions or buy no more cards your function should return the string ‘None’.

Action choice function:
Your action_choice function accepts an instance of player_info, it returns one of the the 16 card name strings or ‘None’. 

Your action_choice function needs to return a string of the action card name you wish to play. If you do not want to play any more actions your function should return the string ‘None’. action_choice will be initially called at the beginning of your turn then it will be looped until either ‘None’ is returned or buys = 0.

Sample action choice function:
def action_choice(player_info):
   villages_in_hand = player_info.hand.count('Village')
   if villages_in_hand > 0:
       action = 'Village'
   else:
       action = 'Smithy'
   return action





Action execute strategy function:
Your action_execute_strategy function accepts an instance of player_info and a string, what it returns changes based on the action that was played.

    Actions with no strategy required:
'Village'
'Smithy'
'Money Lender'
'Market'
 'Festival'
'Laboratory'
With these simple actions, action_execute_strategy can just return ‘None’ 

    Other actions:
'Chapel' 
When using a Chapel action_execute_strategy needs to return a list of the cards you wish to trash.

'Workshop'
When using a Workshop action_execute_strategy needs to return the card name string of the card you wish to gain.

 'Remodel'
When using a Remodel action_execute_strategy needs to return a list of two card name strings, list[0] is the card you are upgrading and list[1] is the card you wish to gain.

 'Feast'
When using a Feast action_execute_strategy needs to return the card name string of the card you wish to gain.

Sample execute action function:

def execute_action_strategy(player_info,action):

   if action == 'Remodel':
       strategy = []
       strategy_trash = raw_input("Choose card to upgrade ")
       strategy_gain = raw_input("Choose card to gain ")
       strategy.append(strategy_trash)
       strategy.append(strategy_gain)
   elif action == 'Workshop':
       strategy = raw_input("Choose card to gain ")
   elif action == 'Feast':
       strategy = raw_input("Choose card to gain ")
   elif action == 'Chapel':
       x = 0
       strategy = []
       while x < 4:
           trash_card = raw_input("Choose a card to trash")
           if trash_card == 'None':
               break
           else:
               strategy.append(trash_card)
               x += 1

   else:
       strategy = 'none'

   return strategy



Buy choice function:
Your buy_choice function accepts an instance of player_info, it returns one of the the 16 card name strings or ‘None’. 

Your buy_choice function needs to return a string of the card name you wish to buy. If you do not want to buy any more cards your function should return the string ‘None’. buy_choice will be initially called after action phase is completed then it will be looped until either ‘None’ is returned or buys = 0.

    Mistakes: If buy_choice returns anything other than one of the 16 card names in play or ‘None’ the code will just break. If buy_choice returns a card with cost that is higher than treasure, the game will continue to run but the card will not be added to your discard pile. The same goes if there are no more of the returned card remaining in the bank.

Sample buy_choice function:

def buy_choice(player_info):
   smithies_for_player = check_player_for_card_type(player_info, 'Smithy')
   villages_for_player = player_info.player.check_player_for_card_type(player_info, 'Village')
   t = player_info.treasure
   if t >= 8:
       buy = 'Province'

   elif t >= 5 and player_info.bank['Province'] <= 4: 
      buy = 'Duchy'

   elif t >= 6:
       buy = 'Gold'

   elif t>= 4 and smithies_for_player <2:
       buy = 'Smithy'

   elif t >=3 and villages_for_player < 0:
       buy = 'Village'

   elif t >= 3:
      buy = 'Silver'

   else:
       buy = 'None'

   return buy


def check_player_for_card_type(player_info, card_type):
   in_hand = player_info.hand.count(card_type)
   in_deck = player_info.deck.count(card_type)
   in_discard = player_info.deck.count(card_type)
   in_played_actions = player_info.played_actions.count(card_type)
   total = in_deck + in_discard + in_hand + in_played_actions

   return total

Git link to simulator code:
https://github.com/InspecterGadget/dominion_simulator

