# Rock Paper Scissors – AI vs Statistical Strategy

This project explores two different approaches to predicting and countering a player’s move in the classic game of Rock, Paper, Scissors (RPS):

- A **statistical approach**, which identifies the player’s most frequent move
- A **machine learning approach** using a Decision Tree trained on the last two moves

---

## Project Goals

- Practice working with scikit-learn
- Explore basic pattern recognition and behavior prediction
- Build and compare two AI strategies for a simple decision-based game

---

## Project Structure

- `rock_paper_scissors_statistic.py`: A simple rule-based AI that counters the player's most common move.
- `rock_paper_scissors_decision_tree.py`: A smarter AI that uses a Decision Tree to detect patterns in the last two moves.

---

## AI Strategy: Decision Tree Classifier

In `rock_paper_scissors_decision_tree.py`:
- The AI tracks the player’s last two moves.
- It uses these as features to train a `DecisionTreeClassifier`.
- The model is updated as the game progresses.
- Based on the predicted next move, it plays the best counter.

### Why it's interesting:
- Demonstrates a time-series-like approach (very small window) to modeling user behavior.
- Shows how even simple ML models can outperform random strategies in repetitive games.

---

## Statistical Strategy

In `rock_paper_scissors_statistic.py`:
- The AI keeps a count of how many times the user plays `rock`, `paper`, or `scissors`.
- It always chooses the counter to the most frequent move.

### Why it's useful:
- Very fast and requires no training
- Surprisingly effective against players who fall into predictable patterns

---

## Technologies Used

- Python 3
- scikit-learn
- DecisionTreeClassifier
- Basic input/output and list handling

---

## Visualization

- I include a win-rate progression chart (based on the Decision Tree AI) to show how performance evolves as the model gathers more data.

---

## How to Run

```bash
# Run the statistical version
python rock_paper_scissors_statistic.py

# Run the decision tree version
python rock_paper_scissors_decision_tree.py

