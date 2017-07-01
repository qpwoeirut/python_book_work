for num in range(1,100001):
    def divisible(inta = []):
        if num % inta == 0:
            print(num, 'is divisible by', inta)
    for value in range(2,100001):
        divisible(value)