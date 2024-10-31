input_string=input("Input a lowerCamel case string: ")
word=[]
before=[]
after=[]
for char in input_string:
    word.append(char)
for x in range (len(word)):
    if word[x].isupper():
        index=x
        print(index)
        break
for y in range(index):
    before.append(word[y])
for z in range(index,len(word),1):
    after.append(word[z])

first=''.join(before)
second=''.join(after)
print('_'.join([first,second.lower()]))