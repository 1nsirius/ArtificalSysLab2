import random

def outcome(player1, player2):
    if player1 == "silence" and player2 == "silence":
        return (1, 1)  # оба получают 1 год
    elif player1 == "silence" and player2 == "betray":
        return (10, 0)  # один молчит, другой предает
    elif player1 == "betray" and player2 == "silence":
        return (0, 10)  # один предает, другой молчит
    else:
        return (5, 5)  # оба предают

def strategy(betrayal_threshold=5):
    if random.random() * 10 < betrayal_threshold:
        return "betray"
    else:
        return "silence"


def simulate_game(rounds, betrayal_threshold=5):
    results_matrix = []

    for _ in range(rounds):
        player1_move = strategy(betrayal_threshold)
        player2_move = strategy(betrayal_threshold)

        p1_outcome, p2_outcome = outcome(player1_move, player2_move)

        results_matrix.append([_, player1_move, player2_move, p1_outcome, p2_outcome])

    return results_matrix

# Запуск симуляции
rounds = 10
betrayal_threshold = 5 # порог предательства (значение от 0 до 10)
results = simulate_game(rounds, betrayal_threshold)

print("Раунд | Игрок 1 | Игрок 2 | Счет Игрока 1 | Счет Игрока 2")
print("---------------------------------------------------")
for row in results:
    print(f"{row[0]+1:>5} | {row[1]:>7} | {row[2]:>7} | {row[3]:>14} | {row[4]:>14}")