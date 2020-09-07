import random

#Builds out prequel quote dictionary
quotes = {}

def add_quote(character, episode, quote):
    if quotes.get(character) == None:
        quotes[character] = {}
        quotes[character]["I"] = []
        quotes[character]["II"] = []
        quotes[character]["III"] = []
        quotes[character]["Ubiq"] = []
    quotes[character][episode].append(quote)
    return

add_quote("Anakin Skywalker", "I", "Are you an angel?")
add_quote("Anakin Skywalker", "I", "I'm a person and my name is Anakin.")
add_quote("Anakin Skywalker", "I", "Yippee!")
add_quote("Anakin Skywalker", "I", "It's working! It's working!")
add_quote("Anakin Skywalker", "I", "I'll try spinning. That's a good trick.")
add_quote("Anakin Skywalker", "I", "Now this is podracing!")
add_quote("Anakin Skywalker", "II", "So have you... more beautiful, I mean.")
add_quote("Anakin Skywalker", "II", "He's overly critical, he never listens, he doesn't understand! It's not fair!")
add_quote("Anakin Skywalker", "II", "You haven't changed a bit. You're exactly the way I remember you in my dreams.")
add_quote("Anakin Skywalker", "II", "I don't like sand. It's coarse and rough and irritating, and it gets everywhere.")
add_quote("Anakin Skywalker", "II", "Now that I'm close to you again, I'm in agony.")
add_quote("Anakin Skywalker", "II", "I'm haunted by the kiss you should never have given me. My heart is beating, hoping that kiss will not become a scar.")
add_quote("Anakin Skywalker", "II", "You are in my very soul, tormenting me. What can I do? I will do anything you ask...")
add_quote("Anakin Skywalker", "II", "It wouldn't have to be that way. We could keep it a secret.")
add_quote("Anakin Skywalker", "II", "I don't think the system works.")
add_quote("Anakin Skywalker", "II", "I will become the most powerful Jedi ever.")
add_quote("Anakin Skywalker", "II", "I will even learn to stop people from dying!")
add_quote("Anakin Skywalker", "II", "I killed them... I killed them all.")
add_quote("Anakin Skywalker", "II", "Not just the men, but the women and the children too.")
add_quote("Anakin Skywalker", "II", "They're like animals, and I slaughtered them like animals! I hate them!")

add_quote("Battle Droid", "Ubiq", "Roger Roger.")

add_quote("Beed", "I", "I don't care what universe you're from, that's gotta hurt!")

add_quote("Boss Nass", "I", "Maybe wesa being friends.")
add_quote("Boss Nass", "I", "Wesa make you bombad general.")

add_quote("C-3PO", "I", "I am C-3PO, human cyborg relations.")
add_quote("C-3PO", "II", "Die, Jedi dogs! Oh, what did I say?")

add_quote("Darth Maul", "I", "At last we will reveal ourselves to the Jedi. At last we will have revenge.")

add_quote("Dexter Jettster", "II", "Well, whattaya know!")
add_quote("Dexter Jettster", "II", "It depends... on how good your manners are... and how big your pocketbook is.")

add_quote("Dooku" , "II", "You have interfered with our plans for the last time.")
add_quote("Dooku", "II", "It is obvious that this contest cannot be decided by our knowledge of the Force, but by our skills with a lightsaber.")
add_quote("Dooku", "II", "This is just the beginning.")

add_quote("Elan", "II", "You wanna buy some deathsticks?")
add_quote("Elan", "II", "I don't wanna sell you deathsticks.")
add_quote("Elan", "II", "I want to go home and rethink my life.")

add_quote("General Grievous", "III", "General Kenobi!")

add_quote("Jango Fett", "II", "I'm just a simple man trying to make my way in the universe.")
add_quote("Jango Fett", "II", "Always a pleasure to meet a Jedi.")
add_quote("Jango Fett", "II", "We won't be seeing him again.")

add_quote("Jar Jar Binks", "I", "Mesa called Jar Jar Binks! Mesa your humble servant!")
add_quote("Jar Jar Binks", "I", "How wude!")
add_quote("Jar Jar Binks", "I", "Mesa doing nothing!")
add_quote("Jar Jar Binks", "I", "Wesa going home!!")

add_quote("Jedi Child Jack", "II", "Because someone erased it from the archive memory.")

add_quote("Jocasta Nu", "II", "If an item does not appear in our records, it does not exist.")

add_quote("Ki-Adi-Mundi", "II", "He is a political idealist, not a murderer.")

add_quote("Lama Su", "II", "Magificent, aren't they?")

add_quote("Mace Windu", "I", "You refer to the prophecy of the One who will bring balance to the force.")
add_quote("Mace Windu", "II", "We're keepers of the peace, not soldiers.")
add_quote("Mace Windu", "II", "This party's over.")

add_quote("Nute Gunray", "I", "My lord, is that... legal?")
add_quote("Nute Gunray", "I", "I was not aware of such failure.")
add_quote("Nute Gunray", "I", "Ah, victory!")
add_quote("Nute Gunray", "I", "This is getting out of hand. Now there are two of them!")
add_quote("Nute Gunray", "II", "Is she dead yet?")
add_quote("Nute Gunray", "II", "She can't do that! Shoot her... or something!")

add_quote("Obi-Wan Kenobi", "I", "Master, destroyers!")
add_quote("Obi-Wan Kenobi", "I", "You were right about one thing, master. The negotiations were short.")
add_quote("Obi-Wan Kenobi", "II", "What!?")
add_quote("Obi-Wan Kenobi", "II", "I have a bad feeling about this.")
add_quote("Obi-Wan Kenobi", "II", "I don't mind flying, but what you're doing is suicide!")
add_quote("Obi-Wan Kenobi", "II", "I hate it when he does that.")
add_quote("Obi-Wan Kenobi", "II", "Patience. Use the Force. Think.")
add_quote("Obi-Wan Kenobi", "II", "This weapon is your life!")
add_quote("Obi-Wan Kenobi", "II", "Why do I get the feeling you're going to be the death of me?")
add_quote("Obi-Wan Kenobi", "II", "You don't want to sell me deathsticks.")
add_quote("Obi-Wan Kenobi", "II", "You want to go home and rethink your life.")
add_quote("Obi-Wan Kenobi", "II", "Well, if droids could think, there'd be none of us here, would there?")
add_quote("Obi-Wan Kenobi", "II", "That's impossible... perhaps the archives are incomplete.")
add_quote("Obi-Wan Kenobi", "II", "That is... good news.")
add_quote("Obi-Wan Kenobi", "II", "That's... why I'm here.")
add_quote("Obi-Wan Kenobi", "II", "Oh, blast! This is why I hate flying.")
add_quote("Obi-Wan Kenobi", "II", "Good job!")
add_quote("Obi-Wan Kenobi", "II", "She seems to be on top of things.")
add_quote("Obi-Wan Kenobi", "II", "You will be expelled from the Jedi order!")
add_quote("Obi-Wan Kenobi", "II", "I have to admit that without the clones it would not have been a victory.")

add_quote("Padme Amidala", "II", "My goodness, you've grown.")
add_quote("Padme Amidala", "II", "Please don't look at me like that.")
add_quote("Padme Amidala", "II", "Are you allowed to love? I thought that was forbidden for a Jedi.")
add_quote("Padme Amidala", "II", "That sounds an awful lot like a dictatorship to me.")
add_quote("Padme Amidala", "II", "No, I call it aggressive negotiations.")

add_quote("Palpatine", "I", "I will make it legal!")
add_quote("Palpatine", "I", "I want that treaty signed.")
add_quote("Palpatine", "I", "A surprise, to be sure, but a welcome one.")
add_quote("Palpatine", "I", "We will watch your career with great interest.")
add_quote("Palpatine", "II", "I will not let this Republic that has stood for over a thousand years be aplit in two.")
add_quote("Palpatine", "II", "I love democracy.")

add_quote("Qui-Gon Jinn", "I", "The ability to speak does not make you intelligent.")
add_quote("Qui-Gon Jinn", "I", "There's always a bigger fish.")

add_quote("R2-D2", "Ubiq", "Beep-Boop.")

add_quote("San Hill", "II", "The Banking Clan will sign your treaty.")

add_quote("Sebulba", "I", "Poodu!")

add_quote("Watto", "I", "Mind tricks don't work on me - only money.")

add_quote("Yoda", "I", "Fear is the path to the dark side. Fear leads to anger... anger leads to hate... hate leads to suffering.")
add_quote("Yoda", "I", "Always two there are, no more, no less. A master and an apprentice.")
add_quote("Yoda", "II", "Much to learn, you still have.")
add_quote("Yoda", "II", "Begun, the Clone War has.")

add_quote("Zam Wessell", "II", "It was a bounty hunter called...")

add_quote("Ubiq", "Ubiq", "I have a bad feeling about this.")
add_quote("Ubiq", "Ubiq", "May the Force be with you.")

#Chats with user until user manually ends loop


def chat():

    quote_list = []

    for character in quotes.keys():
        for episode in quotes[character].keys():
            quote_list += quotes[character][episode]
    
    print("\nYou are now chatting with the characters of the critically acclaimed Star Wars prequel trilogy! To exit the chat, simply type \"END\" at any time. I have a good feeling about this!")
    
    while True:
        usrinput = input("\n")
        if usrinput == "END":
            print("\nChat ended. May the force be with you.\n")
            return
        output = quote_list[random.randint(0, len(quote_list) - 1)]
        print("\n    " + output)

chat()