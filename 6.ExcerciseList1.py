'''
Generate the following output using for loop. Go until g.
a
aba
abacaba
abacabadabacaba
abacabadabacabaeabacabadabacaba

look at the output and find the pattern. Hint - add next letter in the alphabet in each row
'''

alphabet = 'abcdefg'

result = 'a'
print(result)

for letter in alphabet[1:7]:
    result += letter + result
    print(result)