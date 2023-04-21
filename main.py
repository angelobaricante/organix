from components import recognize_speech


text = recognize_speech()

while text != "wow":
    print("It's not wow!!!!!!")
    text = recognize_speech()

