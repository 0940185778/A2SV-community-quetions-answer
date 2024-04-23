def chocolate_consumption(n, bars):
    alice_bars = 0
    bob_bars = 0
    alice_time = 0
    bob_time = 0
    left = 0
    right = n - 1
 
    while left <= right:
        if alice_time <= bob_time:
            alice_time += bars[left]
            alice_bars += 1
            left += 1
        else:
            bob_time += bars[right]
            bob_bars += 1
            right -= 1
 
    return alice_bars, bob_bars
 
 
n = int(input())
bars = list(map(int, input().split()))
 
alice_bars, bob_bars = chocolate_consumption(n, bars)
print(alice_bars, bob_bars)