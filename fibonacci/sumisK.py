def MinFibonacciNumbers(k):
        count = 0
        fib = [1,1]
        while fib[-1]+fib[-2] <= k:
            fib.append(fib[-1]+fib[-2])

        while k > 0:
            i = len(fib)-1
            while fib[i] > k:
                i -= 1
            k -= fib[i]
            count += 1
        return count

k = 7
print(MinFibonacciNumbers(k))
