def split_and_join(line):
    # write your code here
    words = line.split(" ")
    modified_line = "-".join(words)
    return modified_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
