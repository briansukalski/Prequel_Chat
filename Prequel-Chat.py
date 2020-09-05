#Builds out prequel quote dictionary
quotes = {}
quotes["General Grievous"] = ["General Kenobi!"]

#Chats with user until user manually ends loop

def chat():
    usrinput = input("\n")
    print("\n" + quotes["General Grievous"][0] + "\n")
    if usrinput == "END":
        return
    chat()

chat()