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
add_quote("Anakin Skywalker", "III", "This is where the fun begins.")
add_quote("Anakin Skywalker", "III", "I agree, bad idea.")
add_quote("Anakin Skywalker", "III", "My powers have doubled since the last time we met, Count.")
add_quote("Anakin Skywalker", "III", "I shouldn't.")
add_quote("Anakin Skywalker", "III", "I shouldn't have done that, it's not the Jedi way.")
add_quote("Anakin Skywalker", "III", "His fate will be the same as ours.")
add_quote("Anakin Skywalker", "III", "You're the master. I'm just a hero.")
add_quote("Anakin Skywalker", "III", "Hold on, this whole operation was your idea.")
add_quote("Anakin Skywalker", "III", "What? How can you do this? This is outrageous, it's unfair!")
add_quote("Anakin Skywalker", "III", "You're sounding like a Separatist.")
add_quote("Anakin Skywalker", "III", "At last we'll be able to capture that monster and end this war.")
add_quote("Anakin Skywalker", "III", "Is it possible to learn this power?")
add_quote("Anakin Skywalker", "III", "I want more, and I know I shouldn't.")
add_quote("Anakin Skywalker", "III", "You know the dark side?")
add_quote("Anakin Skywalker", "III", "I will quickly discover the truth of all this.")
add_quote("Anakin Skywalker", "III", "I will do whatever you ask.")
add_quote("Anakin Skywalker", "III", "Love won't save you, Padme. Only my new powerse can do that.")
add_quote("Anakin Skywalker", "III", "Because of Obi-Wan?")
add_quote("Anakin Skywalker", "III", "Liar!")
add_quote("Anakin Skywalker", "III", "You turned her against me.")
add_quote("Anakin Skywalker", "III", "Don't lecture me, Obi-Wan. I see through the lies of the Jedi. I do not fear the dark side as you do. I have brought peace, justice, freedom, and security to my new empire.")
add_quote("Anakin Skywalker", "III", "Don't make me kill you.")
add_quote("Anakin Skywalker", "III", "If you're not with me, then you're my enemy.")
add_quote("Anakin Skywalker", "III", "You will try.")
add_quote("Anakin Skywalker", "III", "From my point of view the Jedi are evil!")
add_quote("Anakin Skywalker", "III", "You underestimate my power.")
add_quote("Anakin Skywalker", "III", "I hate you!")
add_quote("Anakin Skywalker", "III", "Where is Padme? Is she safe, is she all right?")
add_quote("Anakin Skywalker", "III", "NOOOOOOOO!!!!")

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
add_quote("Dooku", "III", "I've been looking forward to this.")
add_quote("Dooku", "III", "Good. Twice the pride, double the fall.")
add_quote("Dooku", "III", "You have hate, you have anger, but you don't use them.")

add_quote("Elan", "II", "You wanna buy some deathsticks?")
add_quote("Elan", "II", "I don't wanna sell you deathsticks.")
add_quote("Elan", "II", "I want to go home and rethink my life.")

add_quote("General Grievous", "III", "Ah, yes. The negotiator.")
add_quote("General Grievous", "III", "Your lightsabers will make a fine addition to my collection.")
add_quote("General Grievous", "III", "Time to abandon ship.")
add_quote("General Grievous", "III", "General Kenobi!")
add_quote("General Grievous", "III", "You fool! I have been trained in your Jedi arts by Count Dooku.")
add_quote("General Grievous", "III", "Surely you must realize, you are doomed.")

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
add_quote("Ki-Adi-Mundi", "III", "What about the droid attack on the Wookiees?")
add_quote("Ki-Adi-Mundi", "III", "If he does not give up his emergency powers after the destruction of Grievous, then he should be removed from office.")

add_quote("Lama Su", "II", "Magificent, aren't they?")

add_quote("Mace Windu", "I", "You refer to the prophecy of the One who will bring balance to the force.")
add_quote("Mace Windu", "II", "We're keepers of the peace, not soldiers.")
add_quote("Mace Windu", "II", "This party's over.")
add_quote("Mace Windu", "III", "You are on this council, but we do not grant you the rank of master.")
add_quote("Mace Windu", "III", "Take a seat, young Skywalker.")
add_quote("Mace Windu", "III", "It's settled, then.")
add_quote("Mace Windu", "III", "It's very dangerous putting them together.")
add_quote("Mace Windu", "III", "I sense a plot to destroy the Jedi.")
add_quote("Mace Windu", "III", "A Sith Lord?")
add_quote("Mace Windu", "III", "We must move quickly if the Jedi order is to survive.")
add_quote("Mace Windu", "III", "The Senate will decide your fate.")
add_quote("Mace Windu", "III", "He's too dangerous to be kept alive.")

add_quote("Medical Droid", "III", "She has lost the will to live.")

add_quote("Nute Gunray", "I", "My lord, is that... legal?")
add_quote("Nute Gunray", "I", "I was not aware of such failure.")
add_quote("Nute Gunray", "I", "Ah, victory!")
add_quote("Nute Gunray", "I", "This is getting out of hand. Now there are two of them!")
add_quote("Nute Gunray", "II", "Is she dead yet?")
add_quote("Nute Gunray", "II", "She can't do that! Shoot her... or something!")
add_quote("Nute Gunray", "III", "The war is over! Lord Sidious promised us peace... we only want-")

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
add_quote("Obi-Wan Kenobi", "III", "Oh, this is going to be easy.")
add_quote("Obi-Wan Kenobi", "III", "Flying is for droids.")
add_quote("Obi-Wan Kenobi", "III", "Always on the move...")
add_quote("Obi-Wan Kenobi", "III", "We need to be going up, not down!")
add_quote("Obi-Wan Kenobi", "III", "Oh, it's you!")
add_quote("Obi-Wan Kenobi", "III", "Chancellor Palpatine, Sith Lords are our specialty.")
add_quote("Obi-Wan Kenobi", "III", "Wait a minute, how did this happen? We're smarter than this!")
add_quote("Obi-Wan Kenobi", "III", "Not to worry, we are still flying half a ship.")
add_quote("Obi-Wan Kenobi", "III", "Another happy landing.")
add_quote("Obi-Wan Kenobi", "III", "Oh no, I'm not brave enough for politics.")
add_quote("Obi-Wan Kenobi", "III", "He's right, it's a system we cannot afford to lose.")
add_quote("Obi-Wan Kenobi", "III", "Is he not the chosen one? Is he not to destroy the Sith and bring balance to the Force?")
add_quote("Obi-Wan Kenobi", "III", "It may turn out to be just a wild bantha chase.")
add_quote("Obi-Wan Kenobi", "III", "Hello there!")
add_quote("Obi-Wan Kenobi", "III", "Your move.")
add_quote("Obi-Wan Kenobi", "III", "Oh, I don't think so.")
add_quote("Obi-Wan Kenobi", "III", "So uncivilized.")
add_quote("Obi-Wan Kenobi", "III", "I can't watch any more.")
add_quote("Obi-Wan Kenobi", "III", "Anakin is the father, isn't he?")
add_quote("Obi-Wan Kenobi", "III", "You have done that yourself.")
add_quote("Obi-Wan Kenobi", "III", "Anakin, my allegiance is to the republic, to democracy!")
add_quote("Obi-Wan Kenobi", "III", "Only a Sith deals in absolutes.")
add_quote("Obi-Wan Kenobi", "III", "I will do what I must.")
add_quote("Obi-Wan Kenobi", "III", "I have failed you, Anakin. I have failed you.")
add_quote("Obi-Wan Kenobi", "III", "Anakin, Chancellor Palpatine is evil!")
add_quote("Obi-Wan Kenobi", "III", "Well then you are lost!")
add_quote("Obi-Wan Kenobi", "III", "It's over, Anakin! I have the high ground.")
add_quote("Obi-Wan Kenobi", "III", "Don't try it.")
add_quote("Obi-Wan Kenobi", "III", "You were the chosen one! It was said that you would destroy the Sith, not join them! Bring balance to the Force, not leave it in Darkness!")
add_quote("Obi-Wan Kenobi", "III", "You were my brother, Anakin. I loved you.")

add_quote("Padme Amidala", "II", "My goodness, you've grown.")
add_quote("Padme Amidala", "II", "Please don't look at me like that.")
add_quote("Padme Amidala", "II", "Are you allowed to love? I thought that was forbidden for a Jedi.")
add_quote("Padme Amidala", "II", "That sounds an awful lot like a dictatorship to me.")
add_quote("Padme Amidala", "II", "No, I call it aggressive negotiations.")
add_quote("Padme Amidala", "III", "Have you ever considered that we may be on the wrong side?")
add_quote("Padme Amidala", "III", "Hold me, like you did by the lake on Nboo, so long ago, when there was nothing but our love, no politics, no plotting, no war.")
add_quote("Padme Amidala", "III", "So this is how liberty dies... with thunderous applause.")
add_quote("Padme Amidala", "III", "Anakin, all I want is your love.")

add_quote("Palpatine", "I", "I will make it legal!")
add_quote("Palpatine", "I", "I want that treaty signed.")
add_quote("Palpatine", "I", "A surprise, to be sure, but a welcome one.")
add_quote("Palpatine", "I", "We will watch your career with great interest.")
add_quote("Palpatine", "II", "I will not let this Republic that has stood for over a thousand years be aplit in two.")
add_quote("Palpatine", "II", "I love democracy.")
add_quote("Palpatine", "III", "Get help! You're no match for him. He's a Sith Lord.")
add_quote("Palpatine", "III", "Good, Anakin, Good... Kill him. Kill him now.")
add_quote("Palpatine", "III", "Do it!")
add_quote("Palpatine", "III", "It is only natural. He cut off your arm, and you wanted revenge.")
add_quote("Palpatine", "III", "Leavea him or we'll never make it!")
add_quote("Palpatine", "III", "Soon I will have a new apprentice, one far younger and more powerful.")
add_quote("Palpatine", "III", "Good is a point of view, Anakin.")
add_quote("Palpatine", "III", "The Sith and the Jedi are similar in almost every way.")
add_quote("Palpatine", "III", "Did you ever hear the tragedy of Darth Plagueis the wise?")
add_quote("Palpatine", "III", "I thought not. It's not a story the Jedi would tell you.")
add_quote("Palpatine", "III", "He could use the Force to influence the midi-chlorians to create... life.")
add_quote("Palpatine", "III", "He had such a knowledge of the dark side that he could even keep the ones he cared about from dying.")
add_quote("Palpatine", "III", "The dark side of the Force is a pathway to many abilities some consider to be unnatural.")
add_quote("Palpatine", "III", "It's ironic.")
add_quote("Palpatine", "III", "He could save others from death, but not himself.")
add_quote("Palpatine", "III", "Not from a Jedi.")
add_quote("Palpatine", "III", "Are you going to kill me?")
add_quote("Palpatine", "III", "I can feel your anger. It gives you focus, makes you stronger.")
add_quote("Palpatine", "III", "I am the Senate!")
add_quote("Palpatine", "III", "It's treason, then.")
add_quote("Palpatine", "III", "Power! Unlimited power!")
add_quote("Palpatine", "III", "To cheat death is a power only one has achieved, but if we work together, I know we can discover the secret.")
add_quote("Palpatine", "III", "Henceforth, you shall be known as Darth... Vader.")
add_quote("Palpatine", "III", "Once more the Sith shall rule the galaxy!")
add_quote("Palpatine", "III", "Commander Cody, the time has come.")
add_quote("Palpatine", "III", "Execute Order 66.")
add_quote("Palpatine", "III", "When my new apprentice Darth Vader arrives, he will take care of you.")
add_quote("Palpatine", "III", "The attempt on my life has left me scarred and deformed.")
add_quote("Palpatine", "III", "In order to ensure our security and continuing stability, the Republic will be reorganized into the first Galactic Empire!")
add_quote("Palpatine", "III", "I have waited a long time for this moment, my little green friend.")

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
add_quote("Yoda", "III", "Train yourself to let go of everything you fear to lose.")
add_quote("Yoda", "III", "Go, I will. Good relations with the Wookiees, I have.")
add_quote("Yoda", "III", "Not if anything to say about it, I have.")
add_quote("Yoda", "III", "If so powerful you are, why leave?")
add_quote("Yoda", "III", "Into exile I must go. Failed, I have.")

add_quote("Youngling", "III", "Master Skywalker, there are too many of them. What are we going to do.")

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