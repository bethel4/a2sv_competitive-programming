if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uniquearr= sorted(list(set(arr)))
    print(uniquearr[len(uniquearr)-2])
    
