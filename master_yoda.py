#MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    wordlist = text.split()
    reverse = wordlist[::-1]
    return ' '.join(reverse)

print(master_yoda('I am gone')) 

