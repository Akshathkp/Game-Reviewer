import time

gamePrompt = ""
userName = input("What is your username:  ")
print("Hello, " + userName +". Welcome to Game Reviewer!\n")
gamePrompt = input("Enter the name of the game:  ")

if gamePrompt == "GTA 5":
       print("GTA 5 gets 94/100")
       time.sleep(5.5)
elif gamePrompt == "Fifa 20":
       print("Fifa 20 gets 87/100")
       time.sleep(5.5)
elif gamePrompt == "Fifa 21":
       print("Fifa 21 gets 89/100")
       time.sleep(5.5)
elif gamePrompt == "Fifa 22":
       print("Fifa 22 gets 93/100")
       time.sleep(5.5)
elif gamePrompt == "Fifa 23":
       print("Fifa 23 gets 96/100")
       time.sleep(5.5)
elif gamePrompt == "Cyberpunk 2077":
       print("Cyberpunk gets 63/100")
       time.sleep(4.5)



