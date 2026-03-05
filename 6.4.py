def times_word():
    text = input("Type your text: ")
    word = {}
    word.update(text)
    for i in range (len(word)):
        print(i)
    return word

times_word()