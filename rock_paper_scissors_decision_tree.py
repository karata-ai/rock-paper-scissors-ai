from sklearn.tree import DecisionTreeClassifier
import random

#data storage for training the model
X = []  #last two moves of the player (used as features)
y = []  #player's next move (used as target)

#mappings between move labels and numeric values
label_to_int = {'rock': 0, 'paper': 1, 'scissors': 2}
int_to_label = {v: k for k, v in label_to_int.items()}
counter_moves = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

#initialize the decision tree classifier
clf = DecisionTreeClassifier()

def get_user_move():
    #prompt the user to enter a valid move
    move = input('Your move (rock/paper/scissors): ').lower()
    while move not in label_to_int:
        move = input('Invalid move. Try again: ').lower()
    return move

def get_ai_move(last_two):
    #predict the player's next move based on their previous two, and return the counter move
    if len(X) < 5:
        return random.choice(list(label_to_int.keys()))
    clf.fit(X, y)
    predicted = clf.predict([last_two])[0]
    predicted_label = int_to_label[predicted]
    return counter_moves[predicted_label]

#main game loop
def play():
    #start with one random move to fill history
    move_history = [random.choice(list(label_to_int.keys()))]

    while True:
        user_move = get_user_move()
        move_history.append(user_move)

        if len(move_history) >= 3:
            #extract last two user moves (excluding current one)
            last_two_moves = move_history[-3:-1]
            X.append([label_to_int[m] for m in last_two_moves])
            y.append(label_to_int[user_move])
            ai_move = get_ai_move([label_to_int[m] for m in last_two_moves])
        else:
            ai_move = random.choice(list(label_to_int.keys()))

        print(f'AI played: {ai_move}')

        #determine result
        if ai_move == user_move:
            print('Draw!')
        elif (user_move == 'rock' and ai_move == 'scissors') or \
             (user_move == 'paper' and ai_move == 'rock') or \
             (user_move == 'scissors' and ai_move == 'paper'):
            print('You win!')
        else:
            print('AI wins!')

play()