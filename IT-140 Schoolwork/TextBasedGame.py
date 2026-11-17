#Made by Matthew Ricker
def player_status():
    print(f"You are currently in the {current_room}. Your inventory: {inventory}")
def hp_status():
    print(f"Your health: {player_hp} Dr. G health: {villain_hp}")

rooms = {
    "Foyer": {"East": "Living Room"}, #no item in Foyer
    "Living Room": {"North": "Dining Room", "East": "Bedroom", "South": "Kitchen", "item": "armor"},
    "Kitchen": {"North": "Living Room", "East": "Pantry", "item": "blade"},
    "Pantry": {"West": "Kitchen", "item": "healing snack"},
    "Bedroom": {"West": "Living Room", "North": "Bathroom", "item": "helmet"},
    "Bathroom": {"South": "Bedroom", "item": "bath bomb"},
    "Dining Room": {"South": "Living Room", "East": "Villain Lair", "item": "sword"}
}

current_room = "Foyer"
villain_lair = "Villain Lair"
inventory =  []


while rooms[current_room]:
    print(f"You are currently in the {current_room}")
#item and inventory mapping
    if "item" in rooms[current_room]:
        room_item = rooms[current_room]["item"]
        print(f"You find a {room_item}!")

        choice = input("Would you like to grab it? (y/n) ").strip()  # generates user input on grabbing item or leaving item in room
        if choice == "y":
            inventory.append(room_item)
            print(f"You grabbed {room_item}!")
            del rooms[current_room]["item"]  # removes item from room to prevent getting more than one item
            player_status()
        elif choice == "n":
            print("Item remains in the room, you can pick it up anytime")
            player_status()
        else:
            print("Please enter y or n ")  #sets limits to y or n as validation input
            player_status()
            continue  #continues the inner loop to make valid y or n choices
    else:
        print("There are no items in this room.")
        player_status()

#Movement coding
    movement_choice = input("Where would you like to go? Type go, then direction. Type 'exit' to leave: ").strip()  #Player decides direction here
    movement_commands = movement_choice.split() #to allow for 'go' recognition and input bound

    if len(movement_commands) == 2 and movement_commands[0] == "go": #If player only enters 'East' instead of 'go East' it will not work
        direction = (movement_commands[1]).capitalize()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print(f"You walk to the {current_room}!")
        else:
            print("You cannot go that way!")

    else:
        print("Please enter a valid movement")  #bounds validation to ensure user input is valid and reminds player to enter within bounds
    if movement_choice == "exit":  #option to leave the game
        print("Thanks for playing!")
        break

    if current_room == "Villain Lair":
        print("You are currently in Villain Lair! Dr. G has been expecting you.")  #ends the first loop to the villain lair
        break
#variables for fight with Dr. G
player_hp = 60
villain_hp = 60
sword_health = 3
armor_health = 5
helmet_health = 3
blade_health = 4
player_turn = 1
while current_room == "Villain Lair":
    print(f"These are your items: {inventory}") #A reminder of all the items in inventory
    item_pick = input("Dr. G is waiting for your turn, which item are you choosing? Pick carefully, only one item per turn. Type 'exit' to leave: ")  #Makes this a turn-based RPG style game
    if item_pick == "exit":
        item_pick.capitalize()
        print("Thanks for playing!")
        break

    if item_pick in inventory and player_turn > 0:  #Setting input validation to something player has in inventory
        if item_pick == "sword" and sword_health > 0:
            item_pick.capitalize()
            villain_hp -= 25
            sword_health -= 1
            if sword_health == 0:
                inventory.remove("sword")
            print("You hit him for 25 damage!")
            hp_status()
            player_turn -= 1
        elif item_pick == "armor":
            item_pick.capitalize()
            player_hp += 25
            inventory.remove("armor")
            print("You gained 25 HP")
            hp_status()
            player_turn -= 1
        elif item_pick == "helmet":
            item_pick.capitalize()
            player_hp += 20
            inventory.remove("helmet")
            print("You gained 20 HP")
            hp_status()
            player_turn -= 1
        elif item_pick == "blade" and blade_health > 0:
            item_pick.capitalize()
            villain_hp -= 10
            blade_health -= 1
            if blade_health == 0:
                inventory.remove("blade")
            print("You hit him for 10 damage!")
            hp_status()
            player_turn -= 1
        elif item_pick == "healing snack":
            item_pick.capitalize()
            player_hp += 50
            inventory.remove("healing snack")
            print("Wow, you gained 50 HP!")
            hp_status()
            player_turn -= 1
        elif item_pick == "bath bomb":
            item_pick.capitalize()
            villain_hp -= 50
            inventory.remove("bath bomb")
            print("CRITICAL!! You hit him for 50 damage!")
            hp_status()
            player_turn -= 1
    elif item_pick not in inventory:
        print("Choose a valid item from the inventory list.") #Bounds validation for items in inventory
        continue

    if player_turn == 0 and villain_hp > 0:  #ensures that a turn is given to Dr. G, validating the turn-based game style. Also ensures that Dr. G cannot make attack after HP is at 0
        print("Dr. G makes his attack by swinging his cane! You took 20 damage")
        player_hp -= 20
        player_turn += 1
        print(f"Your health: {player_hp} Dr. G health: {villain_hp}")

    if player_hp <= 0:  #When player dies, gives the option to retry
        death_choice = input("You died! Retry? (y/n): ")
        if death_choice == "y":
            current_room = "Villain Lair"
            player_hp = 60
            villain_hp = 60
            continue
        if death_choice == "n":
            print("Thanks for playing!")
            break

    if villain_hp <= 0:  #When player wins the game
        print("You defeated Dr. G! Congrats on winning the game!")
        break
