s = "azcbobobegghakl"
count = 0;
for_check = 'bob'

for i in range(len(s)):
    if s[i:i+len(for_check)] == for_check:
        count+=1

print(count)
