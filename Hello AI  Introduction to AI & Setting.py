

chat = True
print("Agent : Hi I am a agent")

while chat is True :

    inp = input("You :")

    if "hello" in inp :
       print("Agent : Hi")

    elif "how are you" in inp :
       print("Agent : I am fine , how about you")

    elif inp == "exit" :
       chat = False