print("".join(input() for _ in range(4)))
# print the a string that is made out of 4 input()
print("".join(chr(ord(x) + 1) for x in input()))
# print a string where every char of the input is incremented by one in ASCII
print([x for x in input() if x in 'aeiou'])
# prints a list of all the vowels that the input contains
