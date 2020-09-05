import random

#Builds out prequel quote dictionary
quotes = {}

def add_quote(character, episode, quote):
    if quotes.get(character) == None:
        quotes[character] = {}
        quotes[character]["I"] = []
        quotes[character]["II"] = []
        quotes[character]["III"] = []
    quotes[character][episode].append(quote)
    return

add_quote("Anakin Skywalker", "I", "Are you an angel?")
add_quote("Anakin Skywalker", "I", "I'm a person and my name is Anakin.")
add_quote("Anakin Skywalker", "I", "Yippee!")
add_quote("Anakin Skywalker", "I", "It's working! It's working!")
add_quote("Anakin Skywalker", "I", "I'll try spinning. That's a good trick.")
add_quote("Anakin Skywalker", "I", "Now this is podracing!")


add_quote("Battle Droid", "I", "Roger Roger.")

add_quote("Beed", "I", "I don't care what universe you're from, that's gotta hurt!")

add_quote("Boss Nass", "I", "Maybe wesa being friends.")
add_quote("Boss Nass", "I", "Wesa make you bombad general.")

add_quote("C-3PO", "I", "I am C-3PO, human cyborg relations.")

add_quote("Darth Maul", "I", "At last we will reveal ourselves to the Jedi. At last we will have revenge.")

add_quote("General Grievous", "III", "General Kenobi!")

add_quote("Jar Jar Binks", "I", "Mesa called Jar Jar Binks! Mesa your humble servant!")
add_quote("Jar Jar Binks", "I", "How wude!")
add_quote("Jar Jar Binks", "I", "Mesa doing nothing!")
add_quote("Jar Jar Binks", "I", "Wesa going home!!")

add_quote("Mace Windu", "I", "You refer to the prophecy of the One who will bring balance to the force.")

add_quote("Nute Gunray", "I", "My lord, is that... legal?")
add_quote("Nute Gunray", "I", "I was not aware of such failure.")
add_quote("Nute Gunray", "I", "Ah, victory!")
add_quote("Nute Gunray", "I", "This is getting out of hand. Now there are two of them!")

add_quote("Obi-Wan Kenobi", "I", "Master, destroyers!")
add_quote("Obi-Wan Kenobi", "I", "You were right about one thing, master. The negotiations were short.")

add_quote("Palpatine", "I", "I will make it legal!")
add_quote("Palpatine", "I", "I want that treaty signed.")
add_quote("Palpatine", "I", "A surprise, to be sure, but a welcome one.")
add_quote("Palpatine", "I", "We will watch your career with great interest.")

add_quote("Qui-Gon Jinn", "I", "The ability to speak does not make you intelligent.")
add_quote("Qui-Gon Jinn", "I", "There's always a bigger fish.")

add_quote("R2-D2", "I", "Beep-Boop.")
add_quote("R2-D2", "II", "Beep-Boop.")
add_quote("R2-D2", "III", "Beep-Boop.")

add_quote("Sebulba", "I", "Poodu!")

add_quote("Watto", "I", "Mind tricks don't work on me - only money.")

add_quote("Yoda", "I", "Fear is the path to the dark side. Fear leads to anger... anger leads to hate... hate leads to suffering.")
add_quote("Yoda", "I", "Always two there are, no more, no less. A master and an apprentice.")


#Chats with user until user manually ends loop


def chat():

    quote_list = []
    iterations = 0

    for character in quotes.keys():
        for episode in quotes[character].keys():
            quote_list += quotes[character][episode]
    
    usrinput = input("\n")
    if usrinput == "END":
        print("Chat ended. May the force be with you.")
        return
    output = quote_list[random.randint(0, len(quote_list) - 1)]
    print("\n" + output)

    chat()

chat()