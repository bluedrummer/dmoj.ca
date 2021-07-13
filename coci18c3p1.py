text = input()
count_of_honi = 0
new_text = ""
new_text2 = ""
new_text3 = ""
for c in text:
    if c in "HONI":
        new_text =  new_text + c
 
for i in range(0, len(new_text)):
    if i == 0:
       new_text2 = new_text2 + new_text[i]
    else:
        if new_text2[len(new_text2) - 1] != new_text[i]:
            new_text2 = new_text2 + new_text[i]
temp_text = ""    
for i in range(0, len(new_text2)):
    if temp_text == "":
        if new_text2[i] == "H":
            temp_text = "H"
    elif temp_text == "H":
        if new_text2[i] == "O":
            temp_text = temp_text + "O"   
    elif temp_text == "HO":
        if new_text2[i] == "N":
            temp_text = temp_text + "N"
    elif temp_text == "HON":
        if new_text2[i] == "I":
            count_of_honi += 1
            temp_text = ""
    
    
    
    
        


print(count_of_honi)
        


