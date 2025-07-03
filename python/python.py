import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def simon_says():
    colors = ['🔴 Red', '🟢 Green', '🔵 Blue', '🟡 Yellow']
    sequence = []
    level = 1
    high_score = 0
    
    print("\n=== 🎮 SIMON SAYS ===")
    print("Memorize and repeat the color sequence!")
    print("Type the COLOR LETTER (R, G, B, Y) when prompted")
    print("The sequence will get longer each round!\n")
    input("Press ENTER to start...")
    clear_screen()
    
    while True:
        # Add new color to sequence
        new_color = random.choice(colors)
        sequence.append(new_color)
        
        # Show sequence
        print(f"▶ LEVEL {level} ◀")
        print("Watch carefully...")
        for color in sequence:
            print(color, end=' ', flush=True)
            time.sleep(max(0.5, 1.5 - (level * 0.05)))  # Adaptive speed
        
        clear_screen()
        
        # Player input
        print(f"Your turn (Level {level}):")
        correct = True
        for i, color in enumerate(sequence, 1):
            # Get first letter after emoji (Unicode aware)
            correct_letter = color[0]  # Gets the emoji character
            correct_color = color.split()[1][0].upper()  # Gets 'R', 'G', etc. from '🔴 Red'
            
            guess = input(f"{i}. ").strip().upper()
            if not guess or guess[0] != correct_color:
                print(f"❌ Incorrect! It was {color}")
                correct = False
                break
        
        if not correct:
            print(f"\nGame Over! Final score: {level-1}")
            print(f"High score: {max(high_score, level-1)}")
            if level-1 == 0:
                print("Tip: Type the FIRST LETTER of the color (R/G/B/Y)")
            return
        
        level += 1
        high_score = max(high_score, level-1)
        print(f"✅ Perfect! Next level...")
        time.sleep(1)
        clear_screen()

if __name__== "__main__":
    try:
        while True:
            simon_says()
            if input("\nPlay again? (y/n): ").lower() != 'y':
                break
    except KeyboardInterrupt:
        print("\nThanks for playing!")
        