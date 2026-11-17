#Made by Matthew Ricker
rooms = {
    "Foyer": {"East": "Living Room"}, #no item in Foyer
    "Living Room": {"North": "Dining Room", "East": "Bedroom", "South": "Kitchen", "item": "armor"},
    "Kitchen": {"North": "Living Room", "East": "Pantry", "item": "blade"},
    "Pantry": {"West": "Kitchen", "item": "healing snack"},
    "Bedroom": {"West": "Living Room", "North": "Bathroom", "item": "helmet"},
    "Bathroom": {"South": "Bedroom", "item": "bath bomb"},
    "Dining Room": {"South": "Living Room", "East": "Villain Lair", "item": "Sword"}
}

current_room = "Foyer"
villain_lair = "Villain Lair"

while True:
    movement_choice = input("Where would you like to go? Type go, then direction. Type 'exit' to leave: ").strip()
    movement_commands = movement_choice.split()

    if len(movement_commands) == 2 and movement_commands[0] == "go":
        direction = movement_commands[1].capitalize()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print(f"You walk to the {current_room}!")
        else:
            print("You cannot go that way!")
    elif movement_choice == "exit":
        print("You are exiting the game")

    else:
        print("Please enter a valid movement")
    if movement_choice == "exit":
        print("Thanks for playing!")
        break

    if current_room == "Villain Lair":
        print("You are currently in Villain Lair! Dr. G has been expecting you.")
        break
