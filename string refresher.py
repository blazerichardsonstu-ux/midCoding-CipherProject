name = input("what is your name")
print(name.upper()) 
print(name.lower())
print(name.title()) 

food = input("type your favorite food")
print(food.strip()) 

word = input("give me a word")
print(len(word)) 
print(word[0])
print(word[-1]) 

sentence = "i like cats"
new_sentence = sentence.replace('cats', 'dogs') 
print(new_sentence) 

word2 = input("give me a word") 
letter = input("give me a letter from that word")
print(word2.find(letter))  

word3 = input(" give me yet another word") 
print(word3.count("a")) 

word4 = input(" GIVE ME ANOTHER WORD! please:)") 
lebron = word4[0:4]
print(lebron) 

word5 = input("give Me another word, but a cool one") 
hello = word5[-3:]
print(hello)

word6 = input("give me a word, but with at least 5 letters") 
print(word6[2:]) 
print(word6[2:-2]) 
print(word6[-2:]) 

sentence2 = input("give me a sentence") 
print(sentence2.upper()) 
print(sentence2.lower())
print(len(sentence2))
print("contains 'pyton': "pyton" in sentence2)