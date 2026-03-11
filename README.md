# Fishing simulator!

## About the proyect

This proyect started as a practice of freecoding just from a simple

phrase my partner gave me.

### "Make a realistic game"

even tho "being realistic" has a wide meaning, I decided to go for the

thing that really puts real life into something; time.

Fishing is a very time consuming thing in real life, but it feels very

rewarding when you finally manage to reel the fish you wanted.

## How the code works behing the scenes

### Start

When you run the code, the first thing you see is a "welcoming" screen, telling

you what the game is about and what you can get.

<img width="303" height="99" alt="image" src="https://github.com/user-attachments/assets/124ae95e-c0aa-4687-a8f1-b57fe6bf0fe0" />

It's very simple code, just a few prints.

After that, it gets a little more interesting.

#

## Menu

Then, the menu shows up.

> menu = int(input("Por favor selecciona una opcion:\n1.Iniciar el juego\n2.Salir\n+++ "))

Here, I used "input" to get an answer from the player, whether they wanted to start, or exit the game.

I used "int()" to convert the answer the user gave to an Integer, meaning they can only answer 1 or 2.

I stored the answer the user gave me inside the variable "menu" to be used in the next part.

#

## Verifying choice

Here, I used a few conditionals to determine what the code is going to do after the user makes their choice.

> if menu == 1:
> 
> ---> ...
> 
> elif menu == 2:
> 
> ---> ...
> 
> else:
> 
> ---> print("La opcion no es valida")

If the choice the user makes its not an option, it will display an error message.

#

## Starting the game

First thing the code does is getting the lake the player wants to go.

For that, we display a list of the current lakes stored on the dictionary "lagos".

To make this, we use a For loop.

> print("Por favor elige el lago que deseas visitar:")
> 
> count = 1
> 
> for lago in lagos:
> 
> ---> print(f"---{count}. {lago['nombre']}")
> 
> ---> count += 1
> 
> indice = int(input("+++ "))-1
> 
> lago_actual = lagos[indice]
> 
> print(f"Seleccionaste {lago_actual['nombre']}")

That's a lot of info!

Let's make it simple.

- First, we print just a simple message tho ask the player which lake they want to go.
- Then, we set the variable "count" to 1, that way when we display the list on the screen, it starts on 1 instead of 0.
- After that, the loop starts. It makes so the loop works for every "lake" inside of "lakes".
- Inside the loop, we print a list using the variable "count" and the "name" of the "lake".
- After the name of the lake is displayed, the value of "count" increases by 1, and the loop repeats 'till there are no more lakes to display.
- Then, we ask for the number of the lake the player wants to go, and store it in the variable "indice" and reduce it by 1, so it is real to the list (they start by 0).
- We use that "indice" to declare a new variable called "actual_lake" where we are going to store the values of the selected lake.
- And then, we print the name of the lake selected.

That's a lot of thing for just a simple mechanic!

#

## Main game

Here is where it gets very complicated, so im going to simplify it.

The main game is inside a while loop with a condition that checks when the player wants to exit.

Inside the loop, the player decides if they want to cast their rod or exit and select a different lake.

If they cast the rod, the program determines a probability of pulling something.

If they do, it displays the name of the fish and weight.

If they don't, the line breaks.

Very simple logic!




