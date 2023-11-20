#Student Number: 101305538 Name: Abaan Noman
#Student Number: 101145082 Name: Rahul Rodrigues
"""
The two features we chose to implement were:
Category 1 feature: Loading Game Settings from a File 
Category 2 feature: Number Anomaly 

Anomaly:
a. The anomaly that was added:
The anomaly that was added was the number anomaly

b. Any unique data it checks for (e.g., list of materials , colours , or no unique data was needed)
The number anomaly checks for all items in rooms that contain numbers. It then randomly selects one item and modifies 
said number by either increasing it by 1 or decreasing by 1.

c. Any changes to rooms that were made to support this anomaly (or no changes were needed)
No changes were needed. The anomaly operates by modifying the list of items in a room, which means the room's structure 
will stay the same.

Pair Programming:
1. How did you pair program? E.g., Met in - person, screenshare, VS Code Live Share.

Abaan Noman:
Answer: We pair programmed by meeting in person, screensharing on discord, and also using VS Code Live Share. We used 
various methods as they allowed us to collaborate and have a talkative experience, rather than just splitting up the work.

Rahul Rodrigues:
Answer: Our pair programming sessions were conducted through screensharing on discord, VS Code Live Share, and also meeting 
in person where we could discuss and work on the code together, ensuring constant communication between the Driver and Navigator.

2. Did you work on any parts independently, and what parts if so ? E.g., Reading the code, writing a very small component, 
doing additional research.

Abaan Noman:
Answer: While pair programming, we focused on collaborative coding, and any tasks that might be considered "individual" were worked on 
together. We intentionally avoided working on separate parts independently to ensure shared understanding and equal contribution.

Rahul Rodrigues:
Answer: No, during our pair programming sessions, we did not work on any parts independently. We followed the requirements of collaborative 
coding, as per the assignment specification, where both the Driver and Navigator actively participated in all aspects, including reading the code, 
writing components, and doing additional research.

3. What tasks came up that were not planned in Assignment 8, if any? If none, what tasks were easier or harder than expected?

Abaan Noman:
Answer: Everything went to plan and accordingly with the task list but the only unplanned thing that occured was debugging, which took up considerably
more time than we expected. It was not hard but just time consuming.

Rahul Rodrigues:
Answer: No other tasks came up that were not planned in Assignment 8. However, we did have to do some additional research with files and reading them
which was still easy.

4. About how often did you change who was driver and who was navigator?

Abaan Noman:
Answer: We stayed consistently balanced with role switching during our pair programming sessions. On average, we changed the roles of Driver and Navigator 
every 20-30 minutes to ensure equal participation and a collaborative development experience.

Rahul Rodrigues:
Answer: Role rotation between Driver and Navigator occured quite regularly in the group to promote active engagement from both of us. On average, I would
estimate that we switched roles about every 15-25 minutes so we could both get plenty of chances to experience both roles.

5. If you were to pair program in the future, what might you change?

Abaan Noman:
Answer: Looking ahead for future pair programming, I would improve our communication strategies, possibly by creating an airtight plan to keep us on schedule 
and ensuring more structured discussions. Furthermore, experimenting with different pairing techniques could contribute to an even more productive collaboration.

Rahul Rodrigues:
Answer: In future pair programming projects, I might consider taking more scheduled breaks so we can rechrage and stay focused for longer times. 
"""
import Duty
import random
import sys

def main():
    """
    The main function is mostly just here to setup the game and keep it running in a loop.
    It has a specific order of events that it follows.
    There are a lot of comments in here to help you understand what is going on, but 
    feel free to remove them if they impede your reading of the code.
    """

    # First, we set up all of the game data. 
    # This could have been done using the init() function's optional parameters,
    # but this should make it easier for you to modify it later.

    # These 'helper functions' just clean up the main function and make it more readable.
    # We need to add rooms to the game and we need to register what anomalies are possible.
    add_rooms()
    register_anomalies()

    # Check if a file name is provided as a command line argument
    if len(sys.argv) > 1:
        # If a file name is provided, try to load settings from the file
        load_settings_from_file(sys.argv[1])
    else:
        # If no file name is provided, use default settings
        initialize_default_settings()

    # Initialize the game with all of the data we've just set up.
    Duty.init()

    # This is the main game loop. It will run until the game_running variable is set to False.
    game_running = True
    while game_running:
        # The game keeps track of time while the player is idle, so it is possible we will need
        # to create multiple anomalies at a time the next time the player types a command.
        # `number_of_anomalies_to_create` also takes our probability setting into account.
        n_anomalies = Duty.number_of_anomalies_to_create()

        # We create one anomaly at a time, and we'll write a small helper function to clean up the main function.
        for _ in range(n_anomalies):
            # Keep looping until we can create the anomaly, just in case one of them fails
            anomaly_created = False
            while not anomaly_created:
                anomaly_created = create_anomaly()
            

        # This will update the game status to check if we've lost the game or reached the end.
        # Update returns True if the game should keep going or False if it should end after this loop.
        game_running = Duty.update()

        # Display shows all of the game data. If update() determined the game should end, display() will show the end screen.
        Duty.display()

        # This will pause the loop and wait for the user to type something, running the appropriate commands
        # to handle their actions.
        Duty.handle_input()

def initialize_default_settings():
    """
    Helper function containing default settings for the game.
    """
    Duty.set_setting("debug", False)  # Setting this to True will show additional information to help you debug new anomalies
    Duty.set_setting("timescale", 60)
    Duty.set_setting("probability", 0.1)
    Duty.set_setting("min_seconds_between_anomalies", 10 * 60)

def add_rooms():
    """
    Adds all of the rooms to the game. 
    Duty.add_room() takes a string for the name of a room and a list of strings for the items in the room.
    """
    Duty.add_room("Living Room", ["42\" TV Playing Golf", "Black Leather Sofa", "Circular Metal Coffee Table", "Wooden Bookshelf with 3 Shelves"])
    Duty.add_room("Kitchen", ["Gas Stove", "Retro Red Metal Refrigerator", "Oak Wooden Table", "4 Wooden Chairs"])
    Duty.add_room("Bedroom", ["Queen Size Bed", "Oak Wooden Nightstand", "Oak Wooden Dresser", "Oak Wooden Desk", "Oak Wooden Chair"])
    Duty.add_room("Bathroom", ["Toilet with Oak Seat", "Chrome Sink", "Shower with Blue Tiles", "Medicine Cabinet"])

def register_anomalies():
    """
    Each anomaly we want to add to the game must be "Registered". 
    This is so the game knows what anomalies are possible.
    They will all be stored in UPPERCASE to make it easier to compare them later.
    """
    Duty.register_anomaly("CAMERA MALFUNCTION")
    Duty.register_anomaly("MISSING ITEM")
    Duty.register_anomaly("ITEM MOVEMENT")
    Duty.register_anomaly("NUMBER ANOMALY")

def create_anomaly() -> bool:
    """
    This little helper function handles the control flow for three steps:
    1. Choose a random room that does not have an anomaly, because rooms can only have one anomaly.
    2. Choose a random anomaly from the list of registered anomalies.
    3. Create the anomaly in the room.

    Return True if an anomaly was created, False if no anomaly was created.
    """

    # Choose a random room that does not have an anomaly
    room = Duty.get_random_unchanged_room()

    # Pick a random anomaly from the list of registered anomalies
    # Note: It is possible that some anomalies you create can't work in every room.
    # Maybe you will need additional logic to make sure the anomaly makes sense in the room.
    anomaly = Duty.get_random_anomaly()
    # Camera Malfunction is actually a special one.
    # It will not show this camera when clicking through if 
    # It sees CAMERA MALFUNCTION as the anomaly name
    if anomaly == "CAMERA MALFUNCTION":
        # All anomalies are stores as all uppercase
        # Since a camera malfunction means no items are shown, we pass an empty list
        return Duty.add_anomaly("CAMERA MALFUNCTION", room, [])
    elif anomaly == "MISSING ITEM":
        # We pass the name of the room to these functions to separate out the logic
        return missing_item(room)
    elif anomaly == "ITEM MOVEMENT":
        return item_movement(room)
    elif anomaly == "NUMBER ANOMALY":
        return number_anomaly(room)
    else:
        print(f"ERROR: Anomaly {anomaly} not found")
        return False

def missing_item(room: str) -> bool:
    """
    Removes a random item from the room. This is a pretty straightforward one.
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Choose a random item to remove. (random.randint())
    3. Make a copy of the list of items and remove the item from the copy. (list slicing)
    4. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """
    items = Duty.get_room_items(room)
    item_index_to_remove = random.randint(0, len(items)-1)
    new_items = items[:]
    new_items.pop(item_index_to_remove)
    
    # add_anomaly returns True if the anomaly was created, False if it was not.
    return Duty.add_anomaly("MISSING ITEM", room, new_items)

def item_movement(room: str) -> bool:
    """
    Re-arranges two items in a room. This one is a little more complicated.
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Choose two random items to swap. (random.randint())
    3. Make a copy of the list of items and swap the two items. (list slicing)
    4. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """

    items = Duty.get_room_items(room)

    # If there is only one item in the room, we can't move anything!
    if len(items) < 2:
        return False

    # Find two random items to swap
    item_to_move = random.randint(0, len(items)-1)
    item_to_move_to = random.randint(0, len(items)-1)

    # Make sure the two items are not the same
    while item_to_move == item_to_move_to:
        item_to_move_to = random.randint(0, len(items)-1)

    # Make a copy to avoid accidentally modifying the original item list
    new_items = items[:]

    # The below swap is also possible with the line: new_items[item_to_move], new_items[item_to_move_to] = new_items[item_to_move_to], new_items[item_to_move]
    item_a = new_items[item_to_move]
    item_b = new_items[item_to_move_to]
    new_items[item_to_move] = item_b
    new_items[item_to_move_to] = item_a

    return Duty.add_anomaly("ITEM MOVEMENT", room, new_items)

def number_anomaly(room: str) -> bool:
    """
    Changes an item with a number in it so that it displays a different number that is one higher or lower at random.
    1. Get the list of items in the room. (Duty.get_room_items())
    2. Choose an item with a number.
    3. Change the number to be one higher or lower at random.
    4. Create the anomaly with the new list of items. (Duty.add_anomaly())
    """

    items = Duty.get_room_items(room)

    # Find items with numbers
    items_with_numbers = []
    for item in items:
        if any(char.isdigit() for char in item):
            items_with_numbers.append(item)


    if not items_with_numbers:
        # Return False if there are no items with numbers in the room
        return False 

    # Choose a random item with a number
    item_to_change  = random.choice(items_with_numbers)

    # Isolate the number from the item
    original_number = ""
    for char in item_to_change:
        if char.isdigit():
            original_number += char

    # Create a new number that is one higher or lower at random
    new_number = str(int(original_number) + random.choice([-1, 1]))

    # Replace the original number with the new number
    modified_item = item_to_change.replace(original_number, new_number)

    # Create the anomaly with the new list of items
    new_items = []
    for item in items:
        if item == item_to_change:
            new_items.append(modified_item)
        else:
            new_items.append(item)

    return Duty.add_anomaly("NUMBER ANOMALY", room, new_items)


def load_settings_from_file(file_path):
    """
    Load game settings from a text file.
    The file should contain lines in the format: key=value
    """
    with open(file_path, 'r') as file:
        for line in file:
            keyword, value = line.strip().split('=')
            Duty.set_setting(keyword.strip(), eval(value.strip()))  # Use eval to convert value to appropriate type

main()