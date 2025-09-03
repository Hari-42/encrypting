eingabe = input("Eingabe:")
shift = int(input("Shift:"))
check = int(input("Do you want to encrypt it type 1, decrypt? type 2:"))

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letterslist = list(eingabe)

result = ""


for letter in letterslist:

    if letter in alphabetlist:
        index = alphabetlist.index(letter)

        if check == 1:
            new_index = (index + shift) % 26

        elif check == 2:
            new_index = (index - shift) % 26

        result += alphabetlist[new_index]

    else:
        result += letter

print(result)
