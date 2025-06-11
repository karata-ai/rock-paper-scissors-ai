import random

#counts and counters
moves_counts = {'rock': 0, 'paper': 0, 'scissors': 0}
counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

#the user input
def get_user_move():
    move = input('Your move (rock/paper/scissors): ').lower()
    while move not in moves_counts:
        move = input('Invalid move. Please try again: ').lower()
    return move

#the AI move
def get_ai_move():
    # if there isn't previous move the AI will play random
    if sum(moves_counts.values()) == 0:
        return random.choice(list(moves_counts.keys()))
    most_common = max(moves_counts, key=moves_counts.get) #if not it will search the counter of the most played move
    return counter_moves[most_common]

def play():
    while True:
        user_move = get_user_move()
        moves_counts[user_move] += 1 #here the counts are updated
        ai_move = get_ai_move()

        print(f'AI played: {ai_move}')
        if ai_move == user_move: #compare if the user and AI played same thing
            print('Draw!')
        elif (user_move == 'rock' and ai_move == 'scissors') or \
                (user_move == 'paper' and ai_move == 'rock') or \
                (user_move == 'scissors' and ai_move == 'paper'): #check every possible combination where player win
            print('You win!')
        else: #else the AI win
            print('Ai wins!')

play()