# challage found https://edabit.com/challenge/JzBLDzrcGCzDjkk5n

def encrypt(x):
    t = list(x)
    t.reverse()
    temp = "".join(t)
    # temp = temp.replace("")

    for y in mapping:
        temp = temp.replace(y, str(mapping[y]))
    return temp + "aca"

mapping = {
    "a" : 0,
    "e": 1, 
    "o" : 2,
    "u": 3,
}



print(encrypt("apple"))