# Define a dictionary to store game reviews
game_reviews = {
    "GTA 5": "GTA 5 gets 94/100",
    "Fifa 20": "Fifa 20 gets 87/100",
    "Fifa 21": "Fifa 21 gets 89/100",
    "Fifa 22": "Fifa 22 gets 93/100",
    "Fifa 23": "Fifa 23 gets 96/100",
    "Cyberpunk 2077": "Cyberpunk 2077 gets 63/100",
    "Fifa Mobile": "Fifa Mobile gets 91/100",
    "The Witcher 3": "The Witcher 3 gets 98/100",
    "Minecraft": "Minecraft gets 90/100",
    "Red Dead Redemption 2": "Red Dead Redemption 2 gets 97/100",
    "Call of Duty: Warzone": "Call of Duty: Warzone gets 88/100",
    "Assassin's Creed Valhalla": "Assassin's Creed Valhalla gets 86/100",
    "Fortnite": "Fortnite gets 91/100",
    "Apex Legends": "Apex Legends gets 89/100",
    "The Elder Scrolls V: Skyrim": "The Elder Scrolls V: Skyrim gets 94/100",
    "Among Us": "Among Us gets 85/100",
    "Valorant": "Valorant gets 90/100",
    "Overwatch": "Overwatch gets 88/100",
    "Battlefield V": "Battlefield V gets 84/100",
    "Destiny 2": "Destiny 2 gets 86/100",
    "Fallout 4": "Fallout 4 gets 92/100",
    "Resident Evil Village": "Resident Evil Village gets 89/100",
    "The Last of Us Part II": "The Last of Us Part II gets 93/100",
    "Halo Infinite": "Halo Infinite gets 88/100",
    "Doom Eternal": "Doom Eternal gets 90/100",
    "Far Cry 6": "Far Cry 6 gets 87/100",
    "Cyber Shadow": "Cyber Shadow gets 86/100",
    "Sekiro: Shadows Die Twice": "Sekiro: Shadows Die Twice gets 94/100",
    "Control": "Control gets 88/100",
    "The Outer Worlds": "The Outer Worlds gets 89/100",
    "Monster Hunter: World": "Monster Hunter: World gets 90/100",
    "No Man's Sky": "No Man's Sky gets 82/100",
    "Star Wars Jedi: Fallen Order": "Star Wars Jedi: Fallen Order gets 86/100",
    "Death Stranding": "Death Stranding gets 85/100",
    "Ghost of Tsushima": "Ghost of Tsushima gets 93/100",
    "Ratchet & Clank: Rift Apart": "Ratchet & Clank: Rift Apart gets 89/100",
    "The Legend of Zelda: Breath of the Wild": "The Legend of Zelda: Breath of the Wild gets 97/100",
    "Super Mario Odyssey": "Super Mario Odyssey gets 96/100",
    "Hades": "Hades gets 95/100",
    "Cyberpunk 2077": "Cyberpunk 2077 gets 63/100",
    "Hollow Knight": "Hollow Knight gets 94/100",
    "Celeste": "Celeste gets 92/100",
    "Bioshock Infinite": "Bioshock Infinite gets 95/100",
    "Dark Souls III": "Dark Souls III gets 89/100",
    "Mass Effect 2": "Mass Effect 2 gets 96/100",
    "Bastion": "Bastion gets 86/100",
    "Braid": "Braid gets 91/100",
    "Cuphead": "Cuphead gets 88/100",
    "The Stanley Parable": "The Stanley Parable gets 90/100",
    "Ori and the Blind Forest": "Ori and the Blind Forest gets 93/100",
    "Stardew Valley": "Stardew Valley gets 87/100",
    "Undertale": "Undertale gets 94/100",
    "Terraria": "Terraria gets 92/100",
    "Super Meat Boy": "Super Meat Boy gets 90/100",
    "Dead Cells": "Dead Cells gets 89/100",
    "Inside": "Inside gets 88/100",
    "Hotline Miami": "Hotline Miami gets 91/100",
    "Ori and the Will of the Wisps": "Ori and the Will of the Wisps gets 94/100",
    "Hotline Miami 2: Wrong Number": "Hotline Miami 2: Wrong Number gets 88/100",
    # Add 40 more mobile games and their reviews here
"Clash of Clans": "Clash of Clans gets 92/100",
"Candy Crush Saga": "Candy Crush Saga gets 89/100",
"Pokémon GO": "Pokémon GO gets 88/100",
"Subway Surfers": "Subway Surfers gets 90/100",
"Clash Royale": "Clash Royale gets 87/100",
"Temple Run": "Temple Run gets 86/100",
"PUBG Mobile": "PUBG Mobile gets 94/100",
"Candy Crush Soda Saga": "Candy Crush Soda Saga gets 91/100",
"Garena Free Fire": "Garena Free Fire gets 95/100",
"Mobile Legends: Bang Bang": "Mobile Legends: Bang Bang gets 93/100",
"Hill Climb Racing": "Hill Climb Racing gets 84/100",
"Angry Birds 2": "Angry Birds 2 gets 89/100",
"Sonic Dash": "Sonic Dash gets 85/100",
"Archero": "Archero gets 92/100",
"Fruit Ninja": "Fruit Ninja gets 88/100",
"Clash of Kings": "Clash of Kings gets 86/100",
"Gardenscapes": "Gardenscapes gets 91/100",
"My Talking Tom": "My Talking Tom gets 90/100",
"Roblox": "Roblox gets 87/100",
"Tomb of the Mask": "Tomb of the Mask gets 84/100",
"Color Bump 3D": "Color Bump 3D gets 88/100",
"Scribble Rider": "Scribble Rider gets 85/100",
"BitLife": "BitLife gets 90/100",
"8 Ball Pool": "8 Ball Pool gets 89/100",
"Idle Miner Tycoon": "Idle Miner Tycoon gets 91/100",
"Slither.io": "Slither.io gets 87/100",
"Ludo King": "Ludo King gets 86/100",
"My Talking Angela": "My Talking Angela gets 90/100",
"Minecraft Pocket Edition": "Minecraft Pocket Edition gets 95/100",
"Hay Day": "Hay Day gets 94/100",
}

# The rest of your code remains the same
def gamePrompt():
    userName = input("What is your username:  ")
    print("Hello, " + userName + ". Welcome to Game Reviewer!\n")

    while True:
        game_name = input("Enter the name of the game (or 'exit' to quit):  ")
        
        if game_name.lower() == "exit":
            print("Exiting...")
            break

        # Check if the game is in the dictionary and print its review
        if game_name in game_reviews:
            print(game_reviews[game_name])
        else:
            print("Game not found.")

        choice = input("Do you want to exit (y/n)? ").lower()
        if choice == "y":
            print("Exiting...")
            break

gamePrompt()