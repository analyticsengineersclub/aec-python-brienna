# Example commands: 
#     python calc.py add 1 2
#     python calc.py sub 10 5
#     python calc.py mult 5 5

import argparse

parser = argparse.ArgumentParser(description = "CLI Calculator.")

subparsers = parser.add_subparsers(help = "sub-command help", dest="command")

add = subparsers.add_parser("add", help = "add integers")
add.add_argument("ints_to_sum", nargs="*", type=int)

sub = subparsers.add_parser("sub", help='subtract integers')
sub.add_argument("ints_to_sub", nargs=2, type=int)

mult = subparsers.add_parser("mult", help = "multiply integers")
mult.add_argument('ints_to_mult', nargs=2, type=int)

div = subparsers.add_parser("div", help = "divide integers")
div.add_argument('ints_to_div', nargs="*", type=int)

def aec_subtract(ints_to_sub):
    arg_1 = ints_to_sub[0]
    arg_2 = ints_to_sub[1]
    our_sub = arg_1 - arg_2
    if our_sub < 0: 
        our_sub = 0
    print(f"The subtracted result is: {our_sub}")
    return our_sub

def aec_add(ints_to_sum):
    our_sum = sum(ints_to_sum)
    print(f"The sum of values is: {our_sum}")
    return our_sum

def aec_mult(ints_to_mult):
    our_mult = ints_to_mult[0] * ints_to_mult[1]
    print(f"The multiplied result is: {our_mult}")
    return our_mult

def aec_div(ints_to_div):
    if len(ints_to_div) > 2: 
        raise TypeError("Too many arguments.")
    elif ints_to_div[1] == 0: 
        raise ZeroDivisionError
    else: 
        our_div = ints_to_div[0] / ints_to_div[1] 
        print(f"The divided result is: {our_div}")
        return our_div


if __name__ == "__main__":
    # Parse arguments from command line
    args = parser.parse_args()

    # Carry out operations according to passed arguments
    if args.command == "add":
        aec_add(args.ints_to_sum)
    elif args.command == "sub":
        aec_subtract(args.ints_to_sub)
    elif args.command == "mult":
        aec_mult(args.ints_to_mult)
    elif args.command == "div":
        aec_div(args.ints_to_div)

