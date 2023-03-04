import random
from datetime import datetime

def generate_random_alphabet() -> str:
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    index = random.randrange(26)
    return alphabets[index]

# datetime object containing current date and time
current_time = datetime.now()
file_name = str(current_time).replace(' ', '-')


file = open(f'{file_name}.txt', 'w+')

lines_to_be_generated = 20
chars_per_line = 13

for i in range(lines_to_be_generated):
    for j in  range(chars_per_line):
        file.write(generate_random_alphabet())
        if j != chars_per_line - 1:
            file.write(' ')
    if i != lines_to_be_generated - 1:
        file.write('\n')