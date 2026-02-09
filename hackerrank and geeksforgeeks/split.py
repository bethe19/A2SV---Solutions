def split_and_join(line):
    # write your code here
    line = '-'.join(line.split(" "))
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
