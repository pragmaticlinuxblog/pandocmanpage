#!/usr/bin/env python3
"""
Hello world type program meant as a reference to show how to create a MAN page for your
own program or script, written in Markdown and converted with Pandoc.
"""
__docformat__ = 'reStructuredText'

import argparse


def main():
    """
    Entry point into the program.
    """
    # Create command line parameter parser object.
    parser = argparse.ArgumentParser(description="Hello world type program for greeting someone.")
    # Add optional command line parameters.
    parser.add_argument('-n', action='store', dest='user_name', default='world',
                        help='Name of the person to say hello to')
    # Perform actual command line parameter parsing.
    args = parser.parse_args()
    # Display greeting
    print('Hello, ' + args.user_name + '!')


if __name__ == '__main__':
    exit(main())


