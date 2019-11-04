def text_analyzer(text=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    
    """
    if text == None:
        text = input("What is the text to analyze ? ")
    print("The text contains " + str(len(text)) + " characters:")
    upper = 0
    lower = 0
    punct = 0
    space = 0
    for letter in text:
        if letter.isupper() == True:
            upper = upper + 1
        elif letter.islower() == True:
            lower = lower + 1
        elif letter == ' ':
            space = space + 1
        elif letter.isnumeric() == True:
            continue
        else:
            punct = punct + 1
    print(str(upper) + " upper letters")
    print(str(lower) + " lower letters")
    print(str(punct) + " punctuation marks")
    print(str(space) + " spaces")
        