sentence = str(input("Sentence:"))
keyword = str(input("What is your keyword:"))

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sentence = list(sentence.lower())
keyword = list(keyword.lower())


if len(sentence) == len(keyword):
    print("yes")
else:
    print("no")





