import random
def make_deck():
    colors = ["P","R","Y","B","O","G"]
    deck=[]
    for color in colors:
        for _ in range(6):
            deck.append((1,color, "S" + color))
        for _ in range(4):
            deck.append((2,color, "D" + color))
    
    special_cards = [(9,"X","CC"),(20,"X","IC"),(42,"X","JJ"),(69,"X","GP"),(92,"X","LP"),(102,"X","PS"),(117,"X","BB")]
    for cardTuple in special_cards:
        deck.append(cardTuple)

    return deck

def shuffle(deck):
    for i in range(len(deck)):
        j = random.randint(i,len(deck)-1)
        c = deck[i]
        deck[i] = deck[j]
        deck [j] = c
    return deck

def draw(deck):
        
        draw_card = deck.pop()
        return draw_card

def main():
    deck = make_deck()
    print(deck)

if __name__ == '__main__':
    main()