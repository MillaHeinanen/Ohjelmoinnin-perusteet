import random
random.seed(1234)

ART = {
    "rock": """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    "paper": """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    "scissors": """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
}

OPTIONS = {1: "rock", 2: "paper", 3: "scissors"}

def print_ascii(choice: str):
    print(ART[choice])
    
def winner(player: str, bot: str, player_name: str, bot_name: str):
    if player == bot:
        return f"Draw! Both players chose {player}."
    elif (player == "rock" and bot == "scissors") or \
        (player == "paper" and bot == "rock") or \
        (player == "scissors" and bot == "paper"):
        return f"{player_name} {player} beats {bot_name} {bot}."
    else:
        return f"{bot_name} {bot} beats {player_name} {player}."

def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    player_name = input("Insert player name: ").strip()
    bot_name = "RPS-3PO"
    print(f"Welcome {player_name}!")
    print(f"Your opponent is {bot_name}.")
    print("Game starts...\n")
    stats = {"player_wins": 0, "player_losses": 0, "draws": 0}
    
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        choice = input("Your choice: ").strip()
        if choice == "0":
            break
        if choice not in ["1", "2", "3"]:
            print("Invalid choice, try again.\n")
            continue
        player_choice = OPTIONS[int(choice)]
        bot_choice = OPTIONS[random.randint(1, 3)]
        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#" * 25)
        print(f"{player_name} chose {player_choice}.\n")
        print_ascii(player_choice)
        print("#" * 25)
        print(f"{bot_name} chose {bot_choice}.\n")
        print_ascii(bot_choice)
        print("#" * 25)
        
        result = winner(player_choice, bot_choice, player_name, bot_name)
        print(result + "\n")
        if "Draw" in result:
            stats["draws"] += 1
        elif player_name in result:
            stats["player_wins"] += 1
        else:
            stats["player_losses"] += 1
    print("\nResults:")
    print(f"{player_name} - wins ({stats['player_wins']}), losses ({stats['player_losses']}), draws ({stats['draws']})")
    print("\nProgram ending.")
if __name__ == "__main__":
    main()