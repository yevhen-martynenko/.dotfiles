import os
import time
from datetime import datetime


class Logger:
    def __init__(self, file_path: str="logs/main.log"):
        self.start_time = time.time()
        self.file_path = file_path

        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def log(self, message: str, level: str="INFO"):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        elapsed = time.time() - self.start_time
        log_line = f"[{now}] [{level}] {{{elapsed:.3f}s}}: {message}\n"

        with open(self.file_path, "a", encoding="utf-8") as file:
            file.write(log_line)
