#!/usr/bin/env python3
"""
AUTHOR: CRYPT_ATU
VERSION: 1.5
NAME: Amount Extractor CLI (Upgraded)
"""

#Import Calls
import re
import sys
import argparse
from decimal import Decimal, InvalidOperation
from colorama import init, Fore, Style

#Establish Colorama
init(autoreset=True)

currency_symbols = list('₦$€£¥₹₽฿₩₫₪₴₲')

def extract_amounts(text):
    pattern = r'([' + ''.join(re.escape(sym) for sym in currency_symbols) + r'])(\s?\d[\d,]*\.?\d*)'
    matches = re.findall(pattern, text)

    currency_map = {}
    for symbol, number in matches:
        clean_number = number.replace(',', '').strip()
        try:
            amount = Decimal(clean_number)
            currency_map.setdefault(symbol, []).append(amount)
        except InvalidOperation:
            continue
    return currency_map

def calculate(values, operation):
    if operation == 'sum':
        return sum(values)
    elif operation == 'product':
        result = Decimal(1)
        for val in values:
            result *= val
        return result
    elif operation == 'average':
        return sum(values) / len(values) if values else 0
    else:
        raise ValueError("Unsupported operation")

def display_results(data, operation):
    for symbol, values in data.items():
        result = calculate(values, operation)
        print(Fore.CYAN + f"Currency: {symbol}")
        print(Fore.GREEN + f"  ➤ Count: {len(values)}")
        print(Fore.YELLOW + f"  ➤ {operation.capitalize()}: {symbol}{result:,.2f}\n")

def main():
    parser = argparse.ArgumentParser(
        description="💸 Amount Extractor CLI by CRYPT_ATU. Extracts and calculates money values from any text."
    )
    parser.add_argument("-o", "--operation", choices=["sum", "product", "average"], default="sum",
                        help="Type of calculation: sum, product, or average (default: sum)")
    parser.add_argument("-f", "--file", type=str, help="Text file containing data")
    args = parser.parse_args()

    # Read text input
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as e:
            print(Fore.RED + f"[ERROR] Cannot read file: {e}")
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print(Fore.BLUE + "Paste your text and press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to end:")
        text = sys.stdin.read()

    # Process and output
    data = extract_amounts(text)
    if not data:
        print(Fore.RED + "[INFO] No monetary values found.")
        sys.exit(0)
    
    display_results(data, args.operation)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[EXIT] Interrupted by user.")
        sys.exit(0)
