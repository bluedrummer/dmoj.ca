secret_sentence = input()
clear_sentence = ""    
i = 0

while i < len(secret_sentence):
    if secret_sentence[i] in "aeiou":
        clear_sentence = clear_sentence + secret_sentence[i]
        i += 3
    else:
        clear_sentence = clear_sentence + secret_sentence[i]
        i += 1
        
print(clear_sentence)    
        
            

    