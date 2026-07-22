import os
print(os.getcwd())
file=open("text.txt", "r")
text=file.read()
file.close()
#text file lowercase
text=text.lower()
words=text.split()
#Remove punctuation
text=text.replace(".", "")
text=text.replace(",", "")
text=text.replace("?", "")
text=text.replace("!", "")
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word]= 1
#result
print("word count:\n")

for word, count in word_count.items():
           print(word,":", count)