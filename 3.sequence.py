
'''
Get a input. Create a sequence of numbers from that input using the above alg.
Find the largest number in the sequence
'''
input_number = int(input("Enter a number: "))
sequence = [input_number]

while input_number != 1:
    if input_number % 2 == 0:
        input_number = input_number // 2
    else:
        input_number = 3 * input_number + 1
    sequence.append(input_number)

largest_number = max(sequence)
print(f"The largest number in the sequence starting from {sequence[0]} is {largest_number}")