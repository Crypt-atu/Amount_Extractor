#!/usr/bin/env python3
"""
AUTHOR: CRYPT_ATU
VERSION: 2.0
NAME: Amount Extractor CLI (Enhanced)
"""

import re
import sys
import argparse
from decimal import Decimal, InvalidOperation
from colorama import init, Fore, Style

init(autoreset=True)

CURRENCY_SYMBOLS = list('₦$€£¥₹₽฿₩₫₪₴₲')

def show_banner():
    print(Fore.GREEN + '''
    ===========================================
    |   CRYPT_ATU - AMOUNT EXTRACTOR v2       |
    |   Extract, Calculate, Export 💸         |
    ===========================================
    ''' + Style.RESET_ALL)

def extract_amounts(text, filter_currency=None):
    pattern = r'([' + ''.join(re.escape(sym) for sym in CURRENCY_SYMBOLS) + r'])(\s?\d[\d,]*\.?\d*)'
    matches = re.findall(pattern, text)

    currency_map = {}
    for symbol, number in matches:
        if filter_currency and symbol != filter_currency:
            continue
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
        return sum(values) / len(values) if values else Decimal(0)
    else:
        raise ValueError("Unsupported operation")

def display_results(data, operation):
    output_lines = []
    for symbol, values in data.items():
        result = calculate(values, operation)
        output_lines.append(
            f"Currency: {symbol}\n"
            f"  ➤ Count: {len(values)}\n"
            f"  ➤ {operation.capitalize()}: {symbol}{result:,.2f}\n"
        )
        print(Fore.CYAN + f"Currency: {symbol}")
        print(Fore.GREEN + f"  ➤ Count: {len(values)}")
        print(Fore.YELLOW + f"  ➤ {operation.capitalize()}: {symbol}{result:,.2f}\n")
    return "\n".join(output_lines)

def main():
    parser = argparse.ArgumentParser(
        description="💸 CRYPT_ATU's Amount Extractor v2 — Extracts and calculates monetary values from text."
    )
    parser.add_argument("-o", "--operation", choices=["sum", "product", "average"], default="sum",
                        help="Calculation type: sum, product, or average (default: sum)")
    parser.add_argument("-f", "--file", type=str, help="Input text file")
    parser.add_argument("-c", "--currency", type=str, help="Filter specific currency symbol (e.g., ₦, $, €)")
    parser.add_argument("-e", "--export", type=str, help="Export results to specified .txt file")
    parser.add_argument("-b", "--banner", action="store_true", help="Show banner at start")

    args = parser.parse_args()

    if args.banner:
        show_banner()

    # Get text input
    if args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
        except Exception as ex:
            print(Fore.RED + f"[ERROR] Failed to read file: {ex}")
            sys.exit(1)
    else:
        if sys.stdin.isatty():
            print(Fore.BLUE + "Paste text input. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) + Enter to end:")
        text = sys.stdin.read()

    data = extract_amounts(text, args.currency)

    if not data:
        print(Fore.RED + "[INFO] No matching monetary values found.")
        sys.exit(0)

    result_text = display_results(data, args.operation)

    if args.export:
        try:
            with open(args.export, 'w', encoding='utf-8') as out_file:
                out_file.write(result_text)
            print(Fore.MAGENTA + f"[INFO] Results exported to {args.export}")
        except Exception as ex:
            print(Fore.RED + f"[ERROR] Failed to export results: {ex}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.RED + "\n[EXIT] Interrupted by user.")
        sys.exit(0)
