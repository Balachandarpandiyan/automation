# To Calculate the Total number of vowels

str='Guvi Geeks Network Private Limited '
Vowels='aeiou'
str = str.lower()
res = {}
for ind, char in enumerate(Vowels):
    res[char] = str.count(char)
    # print(str.count(char))
print(res)








