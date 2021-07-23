american_word = " "

while american_word != "quit!":
    american_word = input()
    if american_word == "quit!":
        break
    if len(american_word) > 4:
        if american_word[-2:] == "or" and american_word[-3] not in "aeiouy":
            print(american_word[0:-2] + "our")
        else:
            print(american_word)
            
    else:
        print(american_word)      