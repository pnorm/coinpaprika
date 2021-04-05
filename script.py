# Standard Python libraries
import argparse

# local application imports
from calculator import Calculator
from client import Client
from date_validation import *
from symbols import fetch_symbols, check_if_symbol_available


def main():
    parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='''\
    This script processes historical data from external API about
    cryptocurrencies and give us desirable results.
    Default cryptocurrency for calculating results is bitcoin (btc-bitcoin).
    ''')

    # Subparsers are invoked based on the value of the first positional argument
    # e.g python script.py average-price-by-month
    subparser = parser.add_subparsers(dest="command")

    # Positional arguments
    average_price_by_month = subparser.add_parser(
        'average-price-by-month',
        help='calculate average price of currency by month for given period,')
    consecutive_increase = subparser.add_parser(
        'consecutive-increase',
        help='find longest consecutive period in which price was increasing,')
    export = subparser.add_parser(
        'export',
        help='export data for given period in one format csv or json,')

    # average-price-by-month/consecutive-increase/export
    # triggers the appropriate subparser
    # Optional arguments
    average_price_by_month.add_argument(
            "-s", "--start-date", dest="start_date", nargs="?",
            default="2020-10", type=str, action="store",
            help="Starting date")
    average_price_by_month.add_argument(
            "-e", "--end-date", dest="end_date", nargs="?", default='2021-04',
            type=str, action="store", help="Ending date")
    average_price_by_month.add_argument(
            "-c", "--coin", dest="coin", nargs="?", default="btc-bitcoin",
            type=str, action="store", help="Type of coin")

    consecutive_increase.add_argument(
            "-s", "--start-date", dest="start_date", nargs="?",
            default="2020-01-01", type=str, action="store",
            help="Starting date")
    consecutive_increase.add_argument(
            "-e", "--end-date", dest="end_date", nargs="?",
            default="2021-04-30", type=str, action="store", help="Ending date")
    consecutive_increase.add_argument(
            "-c", "--coin", dest="coin", nargs="?", default="btc-bitcoin",
            type=str, action="store", help="Type of coin")

    export.add_argument(
            "-s", "--start-date", dest="start_date", nargs="?",
            default="2020-01-01", type=str, action="store",
            help="Starting date")
    export.add_argument(
            "-e", "--end-date", dest="end_date", nargs="?",
            default="2021-04-30", type=str, action="store", help="Ending date")
    export.add_argument(
            "-c", "--coin", dest="coin", nargs="?", default="btc-bitcoin",
            type=str, action="store", help="Type of coin")
    export.add_argument(
            "-fo", "--format", dest="format", nargs="?", default="csv",
            type=str, action="store", help="Format of the file. JSON or CSV")
    export.add_argument(
            "-fn", "--file", dest="filename", nargs="?",
            default="unnamed", type=str, action="store",
            help="Name of the file you want to export")

    # Parse arguments
    args = parser.parse_args()

    # Run commands depending on positional argument
    if args.command == 'average-price-by-month':
        # Coin validation
        fetch_symbols()
        check_if_symbol_available(args.coin)

        # Converting and validating date
        start_date = date_pattern(args.start_date, "%Y-%m")
        end_date = date_pattern(args.end_date, "%Y-%m")

        # Convert end date, e.g. 2020-02-01 -> 2020-02-29
        end_date = convert_end_date(end_date)

        # Check if start date before end date
        check_if_start_before_end(start_date, end_date)

        # Creating instance of calculator
        calc = Calculator(start_date, end_date, args.coin)

        # Calculating average price by month
        avg_prices = calc.calculate_average_price_by_month()

        # Priting dates and average prices
        print(f"Date \t Average Price ($)")
        for d, price in avg_prices.items():
            print(f"{d:8} {price:.5f}")

    elif args.command == 'consecutive-increase':
        # Coin validation
        fetch_symbols()
        check_if_symbol_available(args.coin)

        # Converting and validating date
        start_date = date_pattern(args.start_date)
        end_date = date_pattern(args.end_date)

        # Check if start date before end date
        check_if_start_before_end(start_date, end_date)

        # Creating instance of calculator

        # Longest consecutive increasing period

        # Printing result

    elif args.command == 'export':
        # Coin validation
        fetch_symbols()
        check_if_symbol_available(args.coin)

        # Converting and validating date
        start_date = date_pattern(args.start_date)
        end_date = date_pattern(args.end_date)

        # Check if start date before end date
        check_if_start_before_end(start_date, end_date)

        # Export depending on format


if __name__=="__main__":
    main()
