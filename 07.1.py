Sentence = str(input ("Enter your sentence: "))
LowerCase = Sentence.lower()
Vowels = ['a','e','i','o','u']
Consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
CountOfVowels = 0
CountOfConsonants = 0

for Sentence in LowerCase:
    if Sentence in Vowels:
        CountOfVowels = CountOfVowels + 1
    if Sentence in Consonants:
        CountOfConsonants = CountOfConsonants + 1

CountofWords = LowerCase.split (" ")

print ("Number of Vowels :" ,CountOfVowels)
print ("Number of Consonants :" ,CountOfConsonants)
print ("Number of Words :",len(CountofWords))