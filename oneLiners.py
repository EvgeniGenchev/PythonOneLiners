# print the a string that is made out of 4 input()
print("".join(input() for _ in range(4)))

# print a string where every char of the input is incremented by one in ASCII
print("".join(chr(ord(x) + 1) for x in input()))

# prints a list of all the vowels that the input contains
print([x for x in input() if x in 'aeiou'])

# prints a list of numbers from 1 to 1000 that can be divided by 3.
print([num for num in range(1, 1000) if num % 3 == 0])

# prints a boolean list on whether or not the input list values are bigger than 0
print([True if num > 0 else False for num in [int(num) for num in input().split()]])

# prints whether or not word is palindrome
print("Palindrome" if word == word[::-1] else "Not palindrome")

# prints if an year is leap or not
print("Leap" if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Ordinary")

# prints all the uppercasing permutations of a word 
# import itertools as it : i do not consider the import part of the one liner 
print(list(map(''.join, it.product(*((c.upper(), c.lower()) for c in word)))))

#number sum thigy?
print(sum(int(input(f"Number {n}: ")) for n in range(int(input("How many numbers: ")))))
