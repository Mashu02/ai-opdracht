# Opdracht 1 - Piramide

# met 2 for loops
def two_loops():
    x = int(input("Hoe groot? "))
    for y in range(x):
        print(y * "*")
    for star2 in range(x, 0, -1):
        print(star2 * "*")


# met 2 while loops
def while_loops():
    x1 = int(input("Hoe groot? "))
    num = 1
    num2 = x1 - 1
    while num != x1 + 1:
        print(num * "*")
        num += 1

    while num2 != 0:
        print(num2 * "*")
        num2 -= 1


# Opdracht 2 - Tekstcheck

def string_check():
    zin1 = str(input("Geef een string: "))
    zin2 = str(input("geef nog een string: "))
    index = 0

    for x in range(len(zin1)):
        if x == len(zin2):
            break

        if zin1[x] == zin2[x]:
            index += 1

    return index



# Opdracht 3 - Lijstcheck

#gepakt van ai fa 3
def count(lst):
    x = {}  #lege dic
    for i in lst:   #for loop over de lst
        if i not in x:  #als het niet in de dic staat
            x[i] = 1    # dan komt de key met value 1
        else:
            x[i] += 1   # zo wel dan telt het met zo vaak de value voor komt
    return x

#gepakt van ai fa 3
def rnge(lst):
    rnge = max(lst) - min(lst)  #max lst - min lst
    return rnge


# Opdracht 4 - Palindroom

def palindroom():
    txt = input("Geef een woord: ")
    if txt[::-1] == txt:
        #start bij het einde en ga door tot begin en neem stappen van -1
        print("Het woord is een palindroom")
    else:
        print("het is geen palindroom")

# ik heb gewoon opgezocht "how to reverse a string"
# BRON: https://www.w3schools.com/python/python_howto_reverse_string.asp



# Opdracht 5 - Sorteren

#gepakt van ai fa 2
def my_sort(lst):
    for n in range(len(lst)):
        swapped = False
        for i in range(0, len(lst) - 1 - n):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if swapped == False:
            break
    return lst


# Opdracht 6 - Gemiddelde berekenen
def gem(lst):
    return sum(lst) / len(lst)


# Opdracht 7 - Random

# Opdracht 8 - Compressie


# Opdracht 9 - Cyclisch verschuiven


# Opdracht 10 - Fibonaci


# Opdracht 11 - Caesarcijfer !!WERKT NIET GOED MET SPATIE, CODE KLOPT NIET!!
# deze code kan wss veel beter
alfabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z"]
letters = []
cijfers = []
newrotnew = []
cijfers2 = []
letters2 = []

def ceasarcijfers():
    x = input("Geef een tekst: ")
    rot = input("Geef de rotatie: ")


    for letter in x:
        letters.append(letter)
    for x in letters:
        index = alfabet.index(x)
        cijfers.append(index)
    for newrot in cijfers:
        rotrot = int(newrot) + int(rot) + 1
        newrotnew.append(rotrot)
    for singlenum in newrotnew:
        x = alfabet[singlenum]
        letters2.append(x)
#werkt niet met spaties, heb geen zin meer



# Opdracht 12 - FizzBuzz
def num():
    for numbers in range(1, 100):
        if numbers % 15 == 0:
            print("FizzBuzz")
            continue
        elif numbers % 5 == 0:
            print("Buzz")
            continue
        elif numbers % 3 == 0:
            print("Fizz")
            continue

        print(numbers)