import os
import sys
import subprocess
from argparse import ArgumentParser, Namespace

import curses
from dotenv import load_dotenv

from consts import (
    TIMEOUT_MS,
    NOTIFICATION_TIMEOUT,
    SOUND_TIMEOUT,
    BIG_DIGITS
)
from ext import configure_parser
from ext import Logger

load_dotenv()


class Alarm:
    def __init__(self, stdscr, args, logger, time_seconds: int, message: str) -> None:
        self.stdscr = stdscr
        self.time = time_seconds
        self.original_time = time_seconds
        self.message = message
        self.args = args
        self.logger = logger

        self.setup_ui()

    def setup_ui(self):
        self.stdscr.keypad(True)
        curses.curs_set(0)
        curses.noecho()
        self.stdscr.timeout(TIMEOUT_MS)

        init_colors()

    def display_time(self):
        height, width = self.stdscr.getmaxyx()
        hours = self.time // 3600
        minutes = (self.time % 3600) // 60
        seconds = self.time % 60
        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        # ASCII time
        lines = ['' for _ in range(5)]
        for char in time_str:
            digit = BIG_DIGITS.get(char, ['       '] * 5)
            for i in range(5):
                lines[i] += digit[i] + '  '

        # center vertically
        start_y = max(0, height // 2 - len(lines) // 2)
        for i, line in enumerate(lines):
            if start_y + i < height:
                x = max(0, (width - len(line)) // 2)
                try:
                    self.stdscr.addstr(start_y + i, x, line[:width], curses.color_pair(1))
                except curses.error:
                    pass

        # message
        if self.message:
            msg_y = start_y + len(lines) + 1
            if msg_y < height:
                msg_x = max(0, (width - len(self.message)) // 2)
                try:
                    self.stdscr.addstr(msg_y, msg_x, self.message[:width], curses.color_pair(1))
                except curses.error:
                    pass

    def send_notification(self, title: str, body: str):
        try:
            subprocess.run(
                ['notify-send', title, body],
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                check=False,
                timeout=NOTIFICATION_TIMEOUT,
            )
            self.logger.log(f"Notification sent: {title} - {body}")
        except (subprocess.TimeoutExpired, FileNotFoundError) as e:
            self.logger.log(f"Notification failed: {title} - {e}")
    
    def play_alarm_sound(self):
        sound_path = os.getenv("ALARM_SOUND_PATH")
        try:
            subprocess.run(
                ['cvlc', sound_path],
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
                check=False,
                timeout=SOUND_TIMEOUT,
            )
            self.logger.log(f"Alarm sound played: {sound_path}")
            return
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

    def display_finished_screen(self):
        height, width = self.stdscr.getmaxyx()
        msg = "TIME'S UP!"
        y = max(0, height // 2)
        x = max(0, (width - len(msg)) // 2)
        
        try:
            self.stdscr.addstr(y, x, msg[:width], curses.color_pair(1))
            if self.message and y + 2 < height:
                msg_y = y + 2
                msg_x = max(0, (width - len(self.message)) // 2)
                self.stdscr.addstr(msg_y, msg_x, self.message[:width], curses.color_pair(1))
        except curses.error:
            pass

    def run(self):
        try:
            while True:
                self.stdscr.clear()

                if self.time > 0:
                    self.display_time()
                    self.time -= 1
                else:
                    self.display_finished_screen()
                    self.stdscr.refresh()

                    notification_body = f'{self.message} - Time: {self.args.time}' if self.message else f'Time: {self.args.time}'
                    self.send_notification('Alarm Finished', notification_body)
                    self.logger.log(f"Alarm finished - Time: {self.args.time}")
                    self.play_alarm_sound()
                    
                    self.stdscr.timeout(-1)
                    self.stdscr.getch()
                    break

                self.stdscr.refresh()
                key = self.stdscr.getch()
                if key == ord('q') or key == 27:
                    self.logger.log("Program cancelled by user")
                    break

        except KeyboardInterrupt:
            self.logger.log("Program interrupted by user")


def parse_time(time_str: str) -> int:
    if time_str[-1].isdigit():
        return int(time_str)

    value: str = time_str[:-1]
    unit: str = time_str[-1]
    multipliers: dict[str, int] = {'s': 1, 'm': 60, 'h': 3600}

    if unit not in multipliers:
        raise ValueError(f"Invalid time unit: {unit}")

    return int(value) * multipliers[unit]


def init_colors():
    """Initialize terminal color palette"""
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, 231, 232)


def main(args: Namespace) -> None:
    try:
        seconds: int = parse_time(args.time)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    message: str = args.message
    logger = Logger()

    if not message:
        subprocess.run(
            ['notify-send', 'Alarm Set', f'Time: {args.time}'],
            stderr=subprocess.DEVNULL
        )
    else:
        subprocess.run(
            ['notify-send', 'Alarm Set', f'{message} - Time: {args.time}'],
            stderr=subprocess.DEVNULL
        )
    logger.log(f'Alarm Set - Time: {args.time}')
    curses.wrapper(lambda stdscr: Alarm(stdscr, args, logger, seconds, message).run())


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
        parser.print_help()
        sys.exit(1)
    else:
        main(args)
