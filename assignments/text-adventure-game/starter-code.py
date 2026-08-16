# Text Adventure Game Starter Code

rooms = {
    "start": {
        "description": "You are at the entrance of a mysterious cave. A torch glows nearby.",
        "exits": {"north": "forest", "east": "ruins"},
        "items": ["torch"],
    },
    "forest": {
        "description": "The forest is dense and quiet. You hear a river nearby.",
        "exits": {"south": "start", "east": "lake"},
        "items": ["key"],
    },
    "ruins": {
        "description": "Ancient stone walls rise around you. A hidden door is in the corner.",
        "exits": {"west": "start"},
        "items": ["map"],
    },
    "lake": {
        "description": "A calm lake reflects the moonlight. A golden chest rests on a rock.",
        "exits": {"west": "forest"},
        "items": ["treasure"],
    },
}

player = {
    "location": "start",
    "inventory": [],
    "health": 3,
}


def show_room(room_name):
    room = rooms[room_name]
    print(f"\nYou are in the {room_name}.")
    print(room["description"])
    print("Available exits:", ", ".join(room["exits"].keys()) or "none")
    if room["items"]:
        print("You see:", ", ".join(room["items"]))


def get_player_choice():
    choice = input("\nWhat do you want to do? ").strip().lower()
    return choice


def play_game():
    print("Welcome to the Adventure Game!")
    print("Type commands like 'north', 'east', 'take key', or 'quit'.")

    while True:
        show_room(player["location"])

        choice = get_player_choice()

        if choice == "quit":
            print("Thanks for playing!")
            break

        # TODO: Add movement logic
        # TODO: Add item collection logic
        # TODO: Add win/lose conditions
        print("This is a starter template. Finish the game logic here!")
        break


if __name__ == "__main__":
    play_game()
