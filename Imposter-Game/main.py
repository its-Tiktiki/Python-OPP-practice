import time
import random
import os

highscore = None

print("=" * 40)
print("QUICK DRAW DUEL")
print("=" * 40)

while True:
    
    input("\nPress ENTER when you're ready...")
    os.system("cls" if os.name == "nt" else "clear")
    
    print("Get ready...")
    wait_time = random.uniform(2, 6)
    start_wait = time.time()

    while time.time() - start_wait < wait_time:
        time.sleep(0.01)

    print("\nDRAW! PRESS ENTER NOW!")
    
    start = time.perf_counter()
    input()
    reaction_time = time.perf_counter() - start
    print(f"\nReaction Time: {reaction_time:.3f} seconds")

    if highscore is None or reaction_time < highscore:
        highscore = reaction_time
        print("NEW PERSONAL BEST!")

    print(f"Best Time: {highscore:.3f} seconds")

    if reaction_time < 0.20:
        rank = "Gunslinger God"
    elif reaction_time < 0.25:
        rank = "Elite Cowboy"
    elif reaction_time < 0.30:
        rank = "Fast Shooter"
    elif reaction_time < 0.40:
        rank = "Average Human"
    else:
        rank = "Sleeping Turtle"

    print(f"Rank: {rank}")
    ai_time = random.uniform(0.18, 0.45)
    print(f"\nAI Reaction Time: {ai_time:.3f} seconds")

    if reaction_time < ai_time:
        print("You defeated the AI!")
    elif reaction_time > ai_time:
        print("The AI was faster!")
    else:
        print("It's a draw!")

    print("\n" + "=" * 40)
    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("\nThanks for playing!")
        break
