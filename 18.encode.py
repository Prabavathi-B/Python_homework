'''
You have a message that you want to send to your friend. 
You don't want others to see the message.You code the message and send it.
The alg to code is - split each word in half and reverse it (eg cricket becomes ketccri),
if the word ends with a vowel, split at the 
last letter and reverse (eg cinema becomes acinem), if the word has numbers, 
spell the number but add A as first and last letters(8 pm becomes AeightA pm ).
 Write an app that can code and decode the message.
'''

message = "This is a secret message 8 pm".lower()

words = message.split()
encoded_words = []

for word in words:
    if word[-1] in 'aeiou':
        encoded_words.append(word[-1] + word[:-1])

    elif any(char.isdigit() for char in word):
        word = word.replace('1', 'one').replace('2', 'two').replace('3', 'three').replace('4', 'four').replace('5', 'five').replace('6', 'six').replace('7', 'seven').replace('8', 'eight').replace('9', 'nine').replace('0', 'zero')
        word = 'A' + word + 'A'
        encoded_words.append(word)
        
    
    else:
        encoded_words.append(word[len(word)//2:] + word[:len(word)//2])

encoded_message = ' '.join(encoded_words)
print("Encoded message:", encoded_message)