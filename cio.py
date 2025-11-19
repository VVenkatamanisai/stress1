import os
import time

# -------- CONFIGURABLE SETTINGS -------- #
IO_FILE_SIZE_MB = 500    # File size written repeatedly
# --------------------------------------- #


def io_stress():
    """Generate heavy disk I/O."""
    filename = "io_stress.tmp"
    chunk = os.urandom(1024 * 1024)  # 1 MB block

    while True:
        with open(filename, "wb") as f:
            for _ in range(IO_FILE_SIZE_MB):
                f.write(chunk)
        os.remove(filename)


if __name__ == "__main__":
    print("Starting Disk I/O stress...")
    io_stress()
