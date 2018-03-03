s = input("enter a string: ")
list = []
substr = ''
count = 0
letter = 0
max = ''

while count < len(s):
    substr = s[count]
    letter=count
    while letter < len(s) - 1:
        if s[count] <= s[letter+1]:
            substr+=s[letter+1]
        else:
            break
        letter+=1
        count+=1
    list.append(substr)
    count+=1

for i in range(len(list)):
    if len(max) < len(list[i]):
        max = list[i]

print(max)
