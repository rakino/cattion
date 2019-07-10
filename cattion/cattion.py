#! /usr/bin/env python3

import style

def main():
    rawData = input("")
    ducData = rawData.rstrip().lower().split(" ")

    # Change the expression you input into a matrix as a specific style and print it.
    process(ducData, style.style)

def process(data, dic):
    """This function is aimed at changing the input expression and outputing it.
    One word will be changed and output each time."""
    for word in data:
        # The "style" is a 5*5 matrix, the easiest way (maybe the only way) to output is to divide a letter into 5 single lines, then print each line of each letter...
        for i in range(5):
            for letter in word:
                print(dic[letter][i], end = ' ')
            print()

        print()

main()
