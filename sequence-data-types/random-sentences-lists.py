'''nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")'''

nouns = []
verbs =[]
adv = []
adj = []
i = 0
count = int(input("Enter the number"))
print("Enter "+str(count)+"Nouns")
for i in range(count):
    a = input("Enter the nouns")
    nouns.append(a)
print("Enter "+str(count)+" Verb")
for i in range(count):
    a = input("Enter the verbs")
    verbs.append(a)
print("Enter "+str(count)+" Adverb")
for i in range(count):
    a = input("Enter the adverb")
    adv.append(a)
print("Enter "+str(count)+" Adjective")
for i in range(count):
    a = input("Enter the adjective")
    adj.append(a)
print(nouns)
print(verbs)
print(adv)
print(adj)

import random
print("-------------------------------")
num1 = random.randint(0,count-1)
num2 = random.randint(0,count-1)
num3 = random.randint(0,count-1)
num4 = random.randint(0,count-1)
print (adj[num1]+' '+ nouns[num2] + ' ' + verbs[num3] + ' ' + adv[num4]  )
print("--------------------------------")
