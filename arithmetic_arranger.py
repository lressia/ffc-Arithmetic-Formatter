"""
Arithmetic Formatter
"""

import re


def arithmetic_arranger(a, b=False):
    if len(a) <= 5:
        for number in a:
            letter = re.findall("[a-zA-Z]", number)
            num1 = re.findall("^[0-9]*", number)
            sing = re.findall("[+|-]", number)
            num2 = re.findall("[+|-]\s([0-9]*\S)", number)
            # print(str[0])
            if len(letter) == 0:
                if len(num1[0]) <= 4 or len(num2[0]) <= 4:
                    if b is True:
                        if sing[0] == "+":
                            result = int(num1[0]) + int(num2[0])
                            print("\t\t", num1[0], "\n", sing[0], "\t\t", num2[0], "\n", "-"*10, "\n", result)
                        elif sing[0] == "-":
                            result = int(num1[0]) - int(num2[0])
                            print("\t\t", num1[0], "\n", sing[0], "\t\t", num2[0], "\n", "-"*10, "\n", result)
                        elif sing[0] == "*" or "/" or "**" or "%" or "//":
                            print("Error: Operator must be '+' or '-'.")
                    else:
                        print("\t\t", num1[0], "\n", sing[0], "\t\t", num2[0], "\n", "-"*10)
                else:
                    print("Error: Numbers cannot be more than four digits.")
            else:
                print("Error: Numbers must only contain digits.")
    else:
        print("Error: Too many problems.")



