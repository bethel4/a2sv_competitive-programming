def swap_case(s):
    modifedString = ""
    for i in s:
        if i.islower():
            modifedString +=i.upper()
        else:
            modifedString +=  i.lower()
    return  modifedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
