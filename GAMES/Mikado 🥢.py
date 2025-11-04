import random

# Define the sticks and which sticks are lying on top of them
sticks = {
    "blue": ["yellow", "white"],
    "yellow": [],
    "white": [],
    "red": ["blue"],
    "green": ["red"],
}

points = {
    "blue": 3,
    "yellow": 1,
    "white": 1,
    "red": 5,
    "green": 7,
}

removed = []

def removable_sticks():
    """Return list of sticks that can currently be removed"""
    return [s for s in sticks if s not in removed and all(top not in sticks or top in removed for top in sticks[s])]

score = 0

print("=== Mikado Text Game ===\n")

while len(removed) < len(sticks):
    options = removable_sticks()
    print("\nSticks you can remove now:", options)

    if not options:
        print("No sticks can be removed — game over.")
        break

    choice = input("Pick a stick to remove: ")

    if choice not in options:
        print("❌ Can't remove that one!")
        continue

    removed.append(choice)
    score += points[choice]
    print(f"✅ Removed {choice}! +{points[choice]} points")

print("\n✅ Game finished!")
print("Removed sticks:", removed)
print("Total score:", score)
