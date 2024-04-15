import argparse

from handlers import handle_command

def main():
    parser = argparse.ArgumentParser(description='Fetch content from a URL.')
    parser.add_argument('url', help='URL to fetch content from')
    parser.add_argument('-t', action='store_true', help='Fetch only thumbnail')
    parser.add_argument('-b', action='store_true', help='Fetch the best stream')
    parser.add_argument('-l', action='store_true', help='Fetch the lowest stream')
    parser.add_argument('-i', action='store_true', help='get video info') # incomplete
    parser.add_argument('-a', action='store_true', help='list every stream') # incomplete

    args = parser.parse_args()

    handle_command(args)


if __name__ == "__main__":
    main()
