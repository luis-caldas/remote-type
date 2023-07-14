#!/usr/bin/env python3

import argparse


def main():

    argument_parser = argparse.ArgumentParser(
        description="Tool for remote typing"
    )

    # First should be the server, the next one the client
    choices = ["server", "client"]

    # Add the needed arguments
    argument_parser.add_argument(
        "type", type=str,
        choices=choices,
        help="how to start the tool"
    )

    # Parse the args
    arguments = argument_parser.parse_args()

    # Check if server or client
    if arguments.type == choices[0]:
        import server
        server.main()
    else:
        import client
        client.main()


if __name__ == "__main__":
    main()
