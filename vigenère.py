sentence = str(input("Sentence:"))
keyword = str(input("What is your keyword:"))

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sentence = list(sentence.lower())
keyword = list(keyword.lower())


def lengthner(sentence, keyword):
    if len(sentence) > len(keyword):
        word = [keyword[i % len(keyword)] for i in range(len(sentence))]
        return word
    elif len(sentence) < len(keyword):
        word = [keyword[i % len(keyword)] for i in range(len(sentence))]
        return word
    elif len(sentence) == len(keyword):
        return keyword

keyword = lengthner(sentence,keyword)

print(keyword)


