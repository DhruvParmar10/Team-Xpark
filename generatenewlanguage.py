import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','#','$','!','%','@','^','&','*','1','2','3','4','5','6','7','8','9','-','+','/']
assignment = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','#','$','!','%','@','^','&','*','1','2','3','4','5','6','7','8','9','-','+','/']
dummy = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','#','$','!','%','@','^','&','*','1','2','3','4','5','6','7','8','9','-','+','/']
output = {}
stringtesting = []
randomnumberlist = []
random.shuffle(alphabets)
for i in range(0,len(dummy)):
    assignmentnumber = i
    alphabetsnumber = i
    output[assignment[assignmentnumber]] = alphabets[alphabetsnumber]

assignment.clear()
alphabets.clear()

f = open("code.txt", 'w')
f.write(str(output))
f.close()