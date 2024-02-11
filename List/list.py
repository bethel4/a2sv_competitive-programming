if __name__ == '__main__':
    N = int(input())
    
myArray=[]
for _ in range(N):
    command = input().split()
    if command[0]=='insert':
        i, e= map(int, command[1:])
        myArray.insert(i, e)
    elif command[0]=='print':
         print(myArray)
    elif command[0]=='remove':
        e = int(command[1])
        myArray.remove(e)
    elif command[0]=='append':
        e=int(command[1])
        myArray.append(e)
    elif command[0]=='sort':
        myArray.sort()
    elif command[0]=='pop':
        myArray.pop()
    elif command[0]=='reverse':
        myArray.reverse()
         
