import random
print("Anime Battle Arena")
name=input("Enter your name: ")
fighters=["naruto","eren yeager","gojo saturo","tanjiro kamado"]
print("Welcome", name, "! to the anime battle arena!")
print("Available fighters:")
for fighter in fighters:
    print(fighter)
chosen_fighter = input("Choose your fighter from the list: ").lower()
if chosen_fighter == "naruto":
    player_stats = {"name": "naruto", "health": 150, "attack": 30, "defence": 20, "special_attack": "sage mode"}
    print(player_stats)
elif chosen_fighter == "eren yeager":
    player_stats = {"name": "eren", "health": 140, "attack": 35, "defence": 25, "special_attack": "titans form"}
    print(player_stats) 
elif chosen_fighter == "gojo saturo":
    player_stats = {"name": "gojo", "health": 130, "attack": 40, "defence": 30, "special_attack": "infinity"}
    print(player_stats)
elif chosen_fighter == "tanjiro kamado":
    player_stats = {"name": "tanjiro", "health": 160, "attack": 25, "defence": 15, "special_attack": "water breathing"}
    print(player_stats)
else:
    print("Invalid fighter selected.")
    raise SystemExit

print("Now it's time to choose your opponent.")
for fighter in fighters:
    print(fighter)

opponent_fighter = input("Choose your opponent from the list: ").lower()
print("you have chosen", chosen_fighter, "as your fighter and", opponent_fighter, "as your opponent.")
if opponent_fighter == "naruto":
    opponent_stats = {"name": "naruto", "health": 150, "attack": 30, "defence": 20, "special_attack": "sage mode"}
    print(opponent_stats)
elif opponent_fighter == "eren yeager":
    opponent_stats = {"name": "eren", "health": 140, "attack": 35, "defence": 25, "special_attack": "titans form"}
    print(opponent_stats) 
elif opponent_fighter == "gojo saturo":
    opponent_stats = {"name": "gojo", "health": 130, "attack": 40, "defence": 30, "special_attack": "infinity"}
    print(opponent_stats)
elif opponent_fighter == "tanjiro kamado":
    opponent_stats = {"name": "tanjiro", "health": 160, "attack": 25, "defence": 15, "special_attack": "water breathing"}
    print(opponent_stats)
else:
    print("Invalid opponent selected.")
    raise SystemExit
print("the battle begins now!")
health_of_player = player_stats["health"]                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
health_of_opponent = opponent_stats["health"]
print("Your health is",health_of_player)
print("Your opponent's health is",health_of_opponent)
chosen_fighter = input("choose your attack:" + "attack" + " or " + "defence" + "? ").lower()
if chosen_fighter == "attack":
    health_of_opponent -= player_stats["attack"]
    print("You attacked your opponent! Their health is now", health_of_opponent)
elif chosen_fighter == "defence":
    health_of_player += player_stats["defence"]
    print("You defended yourself! Your health is now", health_of_player)
attack_or_defence = random.choice(["attack", "defence"])
if attack_or_defence == "attack":
    health_of_player -= opponent_stats["attack"]
    print("Your opponent attacked you! Your health is now", health_of_player)
elif attack_or_defence == "defence":
    health_of_opponent += opponent_stats["defence"]
    print("Your opponent defended themselves! Their health is now", health_of_opponent)
while health_of_player > 0 and health_of_opponent > 0:
    chosen_fighter = input("choose your attack:" + "attack" + " or " + "defence" + "? ").lower()
    if chosen_fighter == "attack":
        health_of_opponent -= player_stats["attack"]
        print("You attacked your opponent! Their health is now", health_of_opponent)
    elif chosen_fighter == "defence":
        health_of_player += player_stats["defence"]
        print("You defended yourself! Your health is now", health_of_player)
    attack_or_defence = random.choice(["attack", "defence"])
    if attack_or_defence == "attack":
        health_of_player -= opponent_stats["attack"]
        print("Your opponent attacked you! Your health is now", health_of_player)
    elif attack_or_defence == "defence":
        health_of_opponent += opponent_stats["defence"]
        print("Your opponent defended themselves! Their health is now", health_of_opponent) 
if health_of_player == 0:
    print("You have been defeated! Game over.")
else:
    print("Congratulations! You have defeated your opponent!")