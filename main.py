import argparse

def main():
    parser = argparse.ArgumentParser(description='Fetch content from a URL.')
    parser.add_argument('url', help='URL to fetch content from')
    parser.add_argument('-t', help='Fetch only thumbnail')

    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    main()
