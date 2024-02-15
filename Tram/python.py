n = int(input())
stops = [list(map(int, input().split())) for _ in range(n)]

def tram(n, stops):
    max_passenger = stops[0][1]
    current_passenger = stops[0][1]

    for stop in stops[1:]:  # Start from the second stop (index 1)
        current_passenger = current_passenger - stop[0] + stop[1]
        max_passenger = max(max_passenger, current_passenger)

    return max_passenger

result = tram(n, stops)
print(result)
