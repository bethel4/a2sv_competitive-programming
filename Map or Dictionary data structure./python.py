
phone_book = {}

n = int(input())

for _ in range(n):
    entry = input().split()
    name, phone_number = entry[0], entry[1]
    phone_book[name] = phone_number

while True:
    try:
        query = input()
        if query in phone_book:
            print(f"{query}={phone_book[query]}")
        else:
            print("Not found")
    except EOFError:
        break
