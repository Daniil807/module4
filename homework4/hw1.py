def palindrom(string):
    if string == string[::-1]:
        return True
    else:
        return False

print(palindrom('хлеб'))