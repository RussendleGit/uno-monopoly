import random


class Card:
        def __init__(self, color: str, value: str):
                self.color = color
                self.value  = value

class Deck:
        def __init__(self):
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
        
        def play_game(self):
                while True:
                        input(">>")
                        index = random.randint(0, len(self.deck)-1)
                        print(self.deck[index].value, self.deck[index].color)
                        self.deck.pop(index)


if __name__ == "__main__":
        card_deck = Deck()
        card_deck.play_game()



