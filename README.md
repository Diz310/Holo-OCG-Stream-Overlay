# Hololive OCG Stream Overlay

<img width="1402" height="561" alt="Unbenannt-1" src="https://github.com/user-attachments/assets/eb150d35-635f-4e71-bd71-e12e5deab1eb" />

An Overlay for Streams of the Official Hololive Card Game that displays all the revelant information of the 2 players shown on stream.

All the graphics have been made by WeissandChill, I only wrote the script that updates the Overlay based on the users input.

There are 3 fields to input Card IDs: 
The first two are showcasing the cards next to the Oshi. The last one displays the Oshi itself.
The 2 cards next to the Oshi are meant to display important/key cards of the deck that the player is piloting.
The Oshi should be self-explanatory.
The color highlight at the bottom of the Oshi will automatically change based on the color of the chosen Oshi Card.
IMPORTANT: Do NOT input the rarity of the cards! Just the ID like in the example in the image at the very top.
The script will ALWAYS load the MIN-RARITY version of the cards.

If the Card ID that was input was not valid then the script will display the cardbacks to show that something went wrong.
For the Oshi it will show Mios birthday oshi card instead. (#nobias)
<img width="248" height="246" alt="image" src="https://github.com/user-attachments/assets/51f50324-93d1-4a0a-86db-0b1984da0f33" />


There are buttons to increase and decrease both the players life, and holopower.
The life is capped from 0-6 and holo power is capped from 0-9.

Lastly theres the Toggle for the SP Oshi skill. When the player has used their SP Oshi Skill, click this button to showcase that its not available anymore for the rest of the game.
This is how it looks when the SP Skill has been used:
<img width="255" height="62" alt="image" src="https://github.com/user-attachments/assets/7b52d6ba-d8aa-4347-811e-89f9a70cb9e8" />


At the very bottom there's a button to reset the game.
This sets both players life to 5, their holopower to 0, and resets the SP Oshi Skill.
If a player plays an Oshi with 6 starting life, you have to manually add 1 life at the start of the game.

How to use the Overlay:


Just download the zip file under releases and unpack it.
It should look like this:
<img width="656" height="132" alt="image" src="https://github.com/user-attachments/assets/7a3bed27-a3c8-43c4-8a7a-639cf417bb29" />

Then just start the exe file and it should work.
Do NOT remove any of the folders, if you do the script will stop working.
