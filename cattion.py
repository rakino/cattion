#! /usr/bin/env python3

import style

def main():
    rawData = input("")
    ducData = rawData.rstrip().lower().split(" ")

    process(ducData, style.style)

def process(data, dic):
    for word in data:
        for i in range(5):
            for letter in word:
                print(dic[letter][i], end = ' ')
            print()
        print()

main()
