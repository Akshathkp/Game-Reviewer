import time

def gamePrompt():
    userName = input("What is your username:  ")
    print("Hello, " + userName +". Welcome to Game Reviewer!\n")

    while True:
        game_name = input("Enter the name of the game (or 'exit' to quit):  ")
        
        if game_name.lower() == "exit":
            print("Exiting...")
            break

        if game_name == "GTA 5":
            print("GTA 5 gets 94/100")
        elif game_name == "Fifa 20":
            print("Fifa 20 gets 87/100")
        elif game_name == "Fifa 21":
            print("Fifa 21 gets 89/100")
        elif game_name == "Fifa 22":
            print("Fifa 22 gets 93/100")
        elif game_name == "Fifa 23":
            print("Fifa 23 gets 96/100")
        elif game_name == "Cyberpunk 2077":
            print("Cyberpunk gets 63/100")
        elif game_name == "Fifa Mobile":
            print("Fifa Mobile gets 91/100")
        else:
            print("Game not found.")

        choice = input("Do you want to exit (y/n)? ").lower()
        if choice == "y":
            print("Exiting...")
            break

gamePrompt()


