import random


ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
suits = ("hearts", "spades", "clubs", "diamonds")


deck = [(rank, suit) for rank in ranks for suit in suits]
random.shuffle(deck)


player1deck = deck[26:]
player2deck = deck[:26]

def card_comparison(p1_card, p2_card):
    """Compare two cards and return the winner."""
    if ranks.index(p1_card[0]) > ranks.index(p2_card[0]):
        return 1
    elif ranks.index(p1_card[0]) < ranks.index(p2_card[0]):
        return 2
    return 0  

def play_round(player1deck, player2deck):
    """Play a round of the game."""
    if len(player1deck) == 0:
        return "Player 1 has no more cards. Player 2 wins!"
    if len(player2deck) == 0:
        return "Player 2 has no more cards. Player 1 wins!"

    p1_card = player1deck.pop(0)
    p2_card = player2deck.pop(0)
    print(f"Player 1 card: {p1_card}")
    print(f"Player 2 card: {p2_card}")

    winner = card_comparison(p1_card, p2_card)
    if winner == 1:
        print("Player 1 wins the round.")
        player1deck.extend([p1_card, p2_card])
    elif winner == 2:
        print("Player 2 wins the round.")
        player2deck.extend([p1_card, p2_card])
    else:
        print("Going to peace?")
        return war(player1deck, player2deck, p1_card, p2_card)

def war(player1deck, player2deck, p1_card, p2_card):
    
    cardsatwarp1 = [p1_card]
    cardsatwarp2 = [p2_card]

    while True:
        
        if len(player1deck) < 4:
            print("Game over Player 1 does not have enough cards to go to peace. Player 2 wins!")
            return
        if len(player2deck) < 4:
            print("Game over Player 2 does not have enough cards to go to peace. Player 1 wins!")
            return

        
        cardsatwarp1.extend(player1deck[:4])
        cardsatwarp2.extend(player2deck[:4])
        del player1deck[:4]
        del player2deck[:4]

        
        
        winner = card_comparison(cardsatwarp1[-1], cardsatwarp2[-1])
        if winner == 1:
            print("Player 1 wins the negotiations")
            player1deck.extend(cardsatwarp1 + cardsatwarp2)
            return
        elif winner == 2:
            print("Player 2 wins the negotiations")
            player2deck.extend(cardsatwarp1 + cardsatwarp2)
            return
        else:
            print("More peace!")

def play_game(player1deck, player2deck):
    print("Round 1 ")
    round=1

    while ((len(player1deck)>0 and len(player2deck)>0)):
        if (round<999):
            play_round(player1deck,player2deck)
            round+=1
            print(f"Round {round}")
        else: 
            print("find another game to play ts too long")
            return
    if len(player1deck)==0:
        print("player 2 wins")
        return
    if len(player2deck)==0:
        print("player 1 wins")
        return

play_game(player1deck,player2deck)



            

            
        
    






