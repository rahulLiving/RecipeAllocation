from source.RecipeAllocator import RecipeAllocator
import argparse


__author__ = "Aditya Singh"
__version__ = "0.1.0"


def main(args):
    recipieAllocator = RecipeAllocator(path_to_data=args.path,orders_file=args.orders,stock_file=args.stocks)
    print(recipieAllocator.compute())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Executes the application with defaults if no parameters are passed')
    parser.add_argument("-p", "--path", default='./data/', help='path to the data folder')
    parser.add_argument("-o", "--orders", default='orders.json', help='JSON file with orders')
    parser.add_argument("-s", "--stocks", default='stock.json', help='JSON file with stock info')

    args = parser.parse_args()
    main(args)