import candy_land_card
def create_board():
    colors = ["R", "P", "Y", "B", "O", "G"]*22
    board = colors
    board.insert(0, 'Start')
    board.insert(9, "CC")
    board.insert(20,"IC")
    board.insert(42,"JJ")
    board.insert(69, "GP")
    board.insert(92,"LP")
    board.insert(102,"PS")
    board.insert(117,"BB")
    board[4] = "BS60"
    board[29] = "'BS41'"
    board[45] ="GL"
    board[76] ="GL"
    board.append("MC")
    print(board)
    return board


def helper_function(player,board,card_drawn):
    for i in range(player[1]+1,len(board)):
        if card_drawn[1] == board[i][0]:
            return (player[0], i)
    return (player[0], i)


def take_turn(player,board,deck):
    original_player_location = player
    card_drawn = candy_land_card.draw(deck)
    print("Player",player[0],"drew",card_drawn[2])
    if card_drawn[0] == 1:
        player = helper_function(player, board, card_drawn)
    elif card_drawn[0] == 2:
        player = helper_function(player, board, card_drawn)
        player = helper_function(player, board, card_drawn)
    elif card_drawn[2] == 'CC':
        player = (player[0], 9)
    elif card_drawn[2] == 'IC':
        player = (player[0], 20)
    elif card_drawn[2] == 'JJ':
        player = (player[0], 42)
    elif card_drawn[2] == 'GP':
        player = (player[0], 69)
    elif card_drawn[2] == 'LP':
        player = (player[0], 92)
    elif card_drawn[2] == 'PS':
        player = (player[0], 102)
    elif card_drawn[2] == 'BB':
        player = (player[0],117)

    if player[1] == 4:
        print("Player",player,"took a shortcut!")
        return (player[0], 60)
        
    if player[1] == 29:
        print("Player",player,"took a shortcut!")
        return (player[0], 41)
    
    if player[1] == 45:
        print("Player",player,"lost a turn!")
        return original_player_location
    
    if player[1] == 76:
        print("Player",player,"lost a turn!")
        return original_player_location
    
    print("Player",player[0],"landed on", board[player[1]], "(", player[1], ")")
    return player


def play_game(board,num_players):
    deck = candy_land_card.make_deck()
    deck = candy_land_card.shuffle(deck)
    board = create_board()
    number_of_players = num_players
    if number_of_players ==1:
        players = [("Red",0)]
    elif number_of_players ==2:
        players = [("Red",0),("Yellow",0)]
    elif number_of_players == 3:
        players = [("Red",0),("Yellow",0),("Blue",0)]
    else:
        players = [("Red",0),("Yellow",0),("Blue",0),("Orange",0)]
    print(players)


    playerWon = False

    while not playerWon:
        for i in range(len(players)):
            player_after_turn = take_turn(players[i], board, deck)
            if len(deck) == 0:
                deck = candy_land_card.make_deck()
                deck = candy_land_card.shuffle(deck)
            players[i] = player_after_turn
            players_location = players[i][1]
            if players_location >= 134:
                print("Player",players[i][0],"wins!")
                playerWon = True
                break



def main():
    board = create_board()
    prompt = int(input("How many players will be playing?: "))
    if(prompt==0):
        print("Number of player shouldn't be 0")
    play_game(board,prompt)
if __name__=="__main__":
    main()