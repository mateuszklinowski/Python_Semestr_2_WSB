import random
import string

#Zad1
def create_histogram_from_string(string):
    dictionary = {}
    string = sorted(string);
    for char in string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1
    return dictionary

random_hist = create_histogram_from_string("zxcvbnmlkjhgfdsaqwrtyuiop")
print("Zad.1 histogram: \n")
print(random_hist)
print("\n-----------------------\n")

#Zad2
def r_lookup(dictionary,value):
    for key in dictionary:
        if dictionary[key] == value:
            return key
    raise ValueError

def histForWords():
    words_f = open("words.txt", encoding="utf-8")
    line = words_f.readline()
    words = {}
    while line:
        word =  line.strip()
        words[word] = random.randint(0,10)
        line = words_f.readline()
    return words

print("Zad.2 znajdź słowo\n")
print("Found %s", histForWords()["doctoral"])
print("\n-----------------------\n")

#Zad3
def create_hist_from_filename(filename):
    file = open(filename, 'rb')
    hist = {}
    while True:
        char = file.read(1)
        if not char: break
        asc = ord(char)
        if hist.get(asc):
            hist[asc] += 1
        else:
            hist[asc] = 1
    file.close()
    return hist


hist = create_hist_from_filename('words.txt')
print("Zad.3 histogram z pliku \n")
print(hist)
print("\n-----------------------\n")
