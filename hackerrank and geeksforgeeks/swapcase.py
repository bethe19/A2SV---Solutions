def swap_case(s):
    new_s = ''
    for i in s:
        if i >= 'a' and i<='z':
            new_s+= i.upper()
        else:
            new_s += i.lower()

    return new_s

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)