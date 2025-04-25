from Card import Card as Card
import random

class Deck:
        def __init__(self):
                self.num_players = int(input("Enter number of players: "))
                cards = []
                colors = ["red", "yellow", "green", "blue"]
                for color in colors:
                        for x in range(2):
                                for i in range(9):
                                        cards.append(Card(color, i+1))

                for i in range(len(colors)):
                        cards.append(Card(colors[i], 0))
                        cards.append(Card(colors[i], "reverse"))
                        cards.append(Card(colors[i], "skip"))
                        cards.append(Card(colors[i], "+2"))
                        cards.append(Card(colors[i], "+$2000"))
                        cards.append(Card(colors[i], "+$4000"))
                        cards.append(Card("wild", ""))
                        cards.append(Card("wild", " +4"))

                self.deck = cards

        def choose_card(self, cards_list, stack: Card) -> int:
                toprint = ""
                avalible_card = False
                for i in range(len(cards_list)):
                        toprint += f"{i}: {cards_list[i]}\n"
                        if not avalible_card:
                                if cards_list[i].equal_colors(stack) or cards_list[i].equal_values(stack):
                                        avalible_card = True
                if (not avalible_card):
                        print("no avalible cards for you found")
                        return -1
                print(toprint)
                choice = int(input("enter card: "))
                if (cards_list[choice].equal_colors(stack) or cards_list[choice].equal_values(stack)):
                        return choice
                else:
                        print("incorrect")
                        return self.choose_card(cards_list, stack)

        
        def play_game(self):
                player_cards = []
                for i in range(self.num_players):
                        temp = []
                        for x in range(7):
                                index = random.randint(0, len(self.deck)-1)
                                temp.append(self.deck[index])
                                self.deck.pop(index)
                        player_cards.append(temp)
                        temp = []

                index = random.randint(0, len(self.deck)-1)
                pile = self.deck[index]
                self.deck.pop(index)

                player_num = 0
                while True:
                        print("\nplayer:", player_num)
                        print("deck:",pile)

                        index = self.choose_card(player_cards[player_num], pile)
                        if index == -1:
                                random_num = random.randint(0, len(self.deck)-1)
                                new_card = self.deck[random_num]
                                self.deck.pop(random_num)
                                player_cards[player_num].append(new_card)
                                print("added: ", new_card)
                                while not new_card.equal_colors(pile) and not new_card.equal_values(pile):
                                        random_num = random.randint(0, len(self.deck)-1)
                                        new_card = self.deck[random_num]
                                        self.deck.pop(random_num)
                                        player_cards[player_num].append(new_card) 
                                        print("added:",new_card) 
                                print("auto played: ",player_cards[player_num][-1])  
                                pile = player_cards[player_num][-1]
                                player_cards[player_num].pop(-1)   
                        else:
                                pile = player_cards[player_num][index]
                                player_cards[player_num].pop(index)

                        player_num += 1
                        if player_num >= len(player_cards): player_num = 0


