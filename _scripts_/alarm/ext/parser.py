import argparse


def configure_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="alarm",
        description="a simple alarm/timer application",
        add_help=False,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  alarm -t 30s -m "30 seconds           # 30 second alarm
  alarm -t 5m -m "5 minutes"            # 5 minute alarm
  alarm -t 1h -m "1 hour"               # 1 hour alarm
  alarm -t 120 -m "Silent alarm" -s     # 2 minute silent alarm
        """
    )

    cmd_group = parser.add_argument_group("Commands")
    cmd = cmd_group
    cmd.add_argument(
        "-t", "--time",
        type=str,
        help="set the alarm time (e.g. 10s, 5m, 1h)"
    )
    cmd.add_argument(
        "-m", "--message",
        type=str,
        default="",
        help="set the alarm message"
    )
    cmd.add_argument(
        "-s", "--silent",
        action="store_true",
        default=False,
        help="disable the alarm sound"
    )
    cmd.add_argument(
        "--no-time-display",
        action="store_true",
        default=False,
        help="show only message in notification (hide time)"
    )
    cmd.add_argument(
        "-b", "--block-display",
        action="store_true",
        default=False,
        help="block monitor when timer ends (requires xscreensaver or similar)"
    )

    info_group = parser.add_mutually_exclusive_group()
    info_group.add_argument(
        "-h", "--help",
        action="store_true",
        help="show this help message and exit"
    )
    info_group.add_argument(
        "-v", "--version",
        action="store_true",
        help="show version information and exit"
    )

    return parser
