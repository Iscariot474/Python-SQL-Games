import random

# Create domino set
def create_dominoes():
    return [(i, j) for i in range(7) for j in range(i, 7)]

# Print domino nicely
def print_domino(d):
    return f"[{d[0]}|{d[1]}]"

def print_hand(hand):
    for i, d in enumerate(hand):
        print(f"{i}: {print_domino(d)}")

def can_play(domino, left, right):
    return domino[0] == left or domino[1] == left or \
           domino[0] == right or domino[1] == right

def play_domino(domino, board, side):
    left, right = board[0][0], board[-1][1]

    a, b = domino
    if side == "L":
        if b == left:
            board.insert(0, (a, b))
        else:
            board.insert(0, (b, a))
    else:
        if a == right:
            board.append((a, b))
        else:
            board.append((b, a))

def pip_sum(hand):
    return sum(a + b for a, b in hand)

def main():
    dominoes = create_dominoes()
    random.shuffle(dominoes)

    player = dominoes[:7]
    computer = dominoes[7:14]

    # Find starting tile (highest double)
    all_tiles = player + computer
    doubles = [d for d in all_tiles if d[0] == d[1]]

    if doubles:
        start = max(doubles)
    else:
        start = max(all_tiles)

    if start in player:
        turn = "player"
        player.remove(start)
    else:
        turn = "computer"
        computer.remove(start)

    board = [start]

    print("Starting tile:", print_domino(start))

    passes = 0

    while True:
        print("\nBoard:", " ".join(print_domino(d) for d in board))
        left, right = board[0][0], board[-1][1]

        if turn == "player":
            print("\nYour hand:")
            print_hand(player)

            playable = [d for d in player if can_play(d, left, right)]
            if not playable:
                print("You pass.")
                passes += 1
                turn = "computer"
                continue

            passes = 0
            choice = int(input("Choose tile index: "))
            side = input("Play Left or Right? (L/R): ").upper()

            domino = player[choice]
            if not can_play(domino, left, right):
                print("Invalid move!")
                continue

            play_domino(domino, board, side)
            player.remove(domino)

            if not player:
                print("🎉 You win!")
                break

            turn = "computer"

        else:
            playable = [d for d in computer if can_play(d, left, right)]
            if not playable:
                print("\nComputer passes.")
                passes += 1
                turn = "player"
                continue

            passes = 0
            domino = random.choice(playable)

            if domino[0] == left or domino[1] == left:
                play_domino(domino, board, "L")
            else:
                play_domino(domino, board, "R")

            computer.remove(domino)
            print("\nComputer plays", print_domino(domino))

            if not computer:
                print("💻 Computer wins!")
                break

            turn = "player"

        if passes == 2:
            print("\nGame blocked!")
            ps, cs = pip_sum(player), pip_sum(computer)
            print("Your pips:", ps, "| Computer pips:", cs)
            if ps < cs:
                print("🎉 You win!")
            elif cs < ps:
                print("💻 Computer wins!")
            else:
                print("🤝 Draw!")
            break

if __name__ == "__main__":
    main()
