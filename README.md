# Random number guesser!

## About the Project

This script is a practice of different skills like loops, conditionals and flow control.

## How the Code Works Behind the Scenes

### Start
When you run the script, the program asks you to choose the range of the numbers being randomized.

### Menu
Next, the menu appears. I used `input()` to capture the player's choice to either start or exit. I then used `int()` to convert the input into an integer, restricting the options to 1 or 2. This choice is stored in the `menu` variable for the next step.

### Verifying Choice
I used conditionals to determine the program's flow based on the user's selection. If the input doesn't match an option, an error message is displayed.

### Starting the Game
The program first identifies which lake the player wants to visit by displaying a list from the `lagos` dictionary using a `for` loop:
- A message asks the player for their destination.
- A `count` variable is set to 1 so the displayed list starts at 1 instead of 0.
- The loop iterates through every "lake" in the collection.
- After the player chooses a number, the value is stored in `indice` and decreased by 1 to align with Python's zero-based indexing.
- Finally, the selected lake is stored in `actual_lake` and its name is printed.

### Main Game
To keep it simple:
- The core logic runs inside a `while` loop that checks if the player wants to continue.
- Inside, the player chooses to either cast their rod or leave for another lake.
- If they cast the rod, the program calculates the probability of a catch.
- On a success, it displays the fish's name and weight.
- If they fail, the line breaks and the cycle repeats.




