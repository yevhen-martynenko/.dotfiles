import subprocess
import time
import sys
from argparse import ArgumentParser, Namespace

from ext.parser import configure_parser

# TODO: Add curses-based real-time countdown UI


def parse_time(time_str: str) -> int:
    """Parse time string like '10s', '5m', '1h' into seconds"""
    if time_str[-1].isdigit():
        return int(time_str)

    value: str = time_str[:-1]
    unit: str = time_str[-1]
    multipliers: dict[str, int] = {'s': 1, 'm': 60, 'h': 3600}
    return int(value) * multipliers[unit]


def main(args: Namespace) -> None:
    seconds: int = parse_time(args.time)
    message: str = args.message

    subprocess.run(['notify-send', 'Alarm Set', f'{message} - Time: {args.time}'])
    print(f"Alarm set for {seconds} seconds ({args.time})")
    
    time.sleep(seconds)
    
    subprocess.run(['notify-send', 'Alarm Ended', f'{message} - Time: {args.time}'])
    subprocess.run(['cvlc', './assets/alarm.mp3'])


if __name__ == "__main__":
    parser: ArgumentParser = configure_parser()
    args: Namespace = parser.parse_args()
    
    if args.help:
        parser.print_help()
        sys.exit(0)
    elif args.version:
        print("alarm version 0.1")
        sys.exit(0)
    elif not args.time:
        print("Error: Time is required. Use -t/--time option\n", file=sys.stderr)
        sys.exit(1)
    else:
        main(args)
