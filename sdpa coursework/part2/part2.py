import numpy as np
import random

def main():
    odd = []
    even = []
    houses = random.sample(range(0,100), 10) # you can change 10 to your target number
    for i in houses:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    odd.sort(reverse=True)
    even.sort(reverse=False)
    print(houses)
    print(odd)
    print(even)
    odd.extend(even)
    array = np.asanyarray(odd, dtype = int)
    print(houses)
    print(odd)
    print(array)
# sorting algorithm O(n) n depends on how many houses you want to sort
if __name__ == "__main__":
    main()