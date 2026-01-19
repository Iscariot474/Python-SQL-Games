import random

# ----- Card Setup -----
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK_VALUES = {rank: i for i, rank in enumerate(RANKS, start=2)}

def create_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

def deal_hand(deck):
    return [deck.pop() for _ in range(5)]

def show_hand(hand):
    return ', '.join(f"{rank} of {suit}" for rank, suit in hand)

# ----- Hand Evaluation -----
def evaluate_hand(hand):
    ranks = sorted([RANK_VALUES[rank] for rank, _ in hand])
    suits = [suit for _, suit in hand]

    rank_counts = {r: ranks.count(r) for r in ranks}
    counts = sorted(rank_counts.values(), reverse=True)

    is_flush = len(set(suits)) == 1
    is_straight = ranks == list(range(ranks[0], ranks[0] + 5))

    if is_straight and is_flush:
        return (8, "Straight Flush")
    elif counts == [4, 1]:
        return (7, "Four of a Kind")
    elif counts == [3, 2]:
        return (6, "Full House")
    elif is_flush:
        return (5, "Flush")
    elif is_straight:
        return (4, "Straight")
    elif counts == [3, 1, 1]:
        return (3, "Three of a Kind")
    elif counts == [2, 2, 1]:
        return (2, "Two Pair")
    elif counts == [2, 1, 1, 1]:
        return (1, "One Pair")
    else:
        return (0, "High Card")

# ----- Game Logic -----
def play_poker():
    print("\n🎲 Welcome to Python Poker!")
    chips = 100
    bet = 10

    deck = create_deck()
    random.shuffle(deck)

    player_hand = deal_hand(deck)
    computer_hand = deal_hand(deck)

    print("\nYour hand:")
    print(show_hand(player_hand))

    input("\nPress ENTER to place your bet ($10) and reveal hands...")

    player_score, player_name = evaluate_hand(player_hand)
    computer_score, computer_name = evaluate_hand(computer_hand)

    print("\nComputer's hand:")
    print(show_hand(computer_hand))

    print(f"\nYour hand: {player_name}")
    print(f"Computer hand: {computer_name}")

    if player_score > computer_score:
        chips += bet
        print("\n✅ You win!")
    elif player_score < computer_score:
        chips -= bet
        print("\n❌ Computer wins!")
    else:
        print("\n🤝 It's a tie!")

    print(f"\n💰 Your chips: ${chips}")

# ----- Run Game -----
if __name__ == "__main__":
    play_poker()
