# Fishing simulator!

## About the project

This project started as a practice of free-coding just from a simple phrase my partner gave me.

### "Make a realistic game"

even tho "being realistic" has a wide meaning, I decided to go for the thing that really puts real life into something; time.

Fishing is a very time consuming thing in real life, but it feels very rewarding when you finally manage to reel the fish you wanted.

## How the code works behing the scenes

### Start

#

When you run the code, the first thing you see is a "welcoming" screen, telling

you what the game is about and what you can get.

<img width="303" height="99" alt="image" src="https://github.com/user-attachments/assets/124ae95e-c0aa-4687-a8f1-b57fe6bf0fe0" />

It's very simple code, just a few prints.

This is how it looks displayed in the terminal:

<img width="538" height="88" alt="imagen_2026-03-10_190732155" src="https://github.com/user-attachments/assets/c7225fdb-43ee-4302-922e-f0f97c2db5e9" />

After that, it gets a little more interesting.



### Menu

#

Then, the menu shows up.

<img width="683" height="19" alt="imagen_2026-03-10_190337665" src="https://github.com/user-attachments/assets/7ce6dbca-7f29-4b0f-b349-b204a076cb5d" />

Here, I used "input()" to get an answer from the player, whether they wanted to start, or exit the game.

I used "int()" to convert the answer the user gave to an Integer, meaning they can only answer 1 or 2.

I stored the answer the user gave me inside the variable "menu" to be used in the next part.



### Verifying choice

#

Here, I used a few conditionals to determine what the code is going to do after the user makes their choice.

<img width="139" height="62" alt="imagen_2026-03-10_190524433" src="https://github.com/user-attachments/assets/b7b515e6-e50a-47f3-bcd4-7d0c767dc21d" />

If the choice the user makes its not an option, it will display an error message.

This is how it looks displayed in the terminal:

<img width="232" height="71" alt="imagen_2026-03-10_190821674" src="https://github.com/user-attachments/assets/e40849fb-2b74-430c-b7b9-9bec296744be" />



### Starting the game

#

First thing the code does is getting the lake the player wants to go.

For that, we display a list of the current lakes stored on the dictionary "lagos".

To make this, we use a For loop.

<img width="406" height="155" alt="imagen_2026-03-10_190612188" src="https://github.com/user-attachments/assets/a32e1392-6126-4d8a-9205-1836b1ee5ba2" />

That's a lot of info!

Let's make it simple.

- First, we print just a simple message to ask the player which lake they want to go.
- Then, we set the variable "count" to 1, that way when we display the list on the screen, it starts on 1 instead of 0.
- After that, the loop starts. It makes so the loop works for every "lake" inside of "lakes".
- Inside the loop, we print a list using the variable "count" and the "name" of the "lake".
- After the name of the lake is displayed, the value of "count" increases by 1, and the loop repeats 'till there are no more lakes to display.
- Then, we ask for the number of the lake the player wants to go, and store it in the variable "indice" and reduce it by 1, so it is real to the list (they start by 0).
- We use that "indice" to declare a new variable called "actual_lake" where we are going to store the values of the selected lake.
- And then, we print the name of the lake selected.

That's a lot of thing for just a simple mechanic!

And you only see this through the terminal:

<img width="310" height="86" alt="imagen_2026-03-10_190927074" src="https://github.com/user-attachments/assets/f14c36ad-f50c-4953-a18e-e738e27ed4c9" />



### Main game

#

Here is where it gets very complicated, so im going to simplify it.

- The main game is inside a while loop with a condition that checks when the player wants to exit.

- Inside the loop, the player decides if they want to cast their rod or exit and select a different lake.

- If they cast the rod, the program determines a probability of pulling something.

- If they do, it displays the name of the fish and weight.

- If they don't, the line breaks.

- Then, the cycle repeats.

Very simple logic!




