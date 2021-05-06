
import argparse
import sys

def calc(args):
    if args.op == 'add':
        return args.first_no + args.second_no

    elif args.op == 'sub':
        return args.first_no - args.second_no

    elif args.op == 'mul':
        return args.first_no * args.second_no

    elif args.op == 'div':
        return args.first_no / args.second_no

    else:
        return "Something Went Wrong!"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--first_no',
                        type=eval,
                        default= 0,
                        help= "enter first no:")
    parser.add_argument('--second_no',
                        type=eval,
                        default= 0,
                        help= "enter second no")
    parser.add_argument('--op',
                        type=str,
                        default= 'add' ,
                        help= "enter operator")
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))