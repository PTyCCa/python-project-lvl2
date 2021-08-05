#!/usr/bin/env python3
import argparse

def main():
    """Print difference beetween two files."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)

    args = parser.parse_args()


if __name__ == '__main__':
    main()