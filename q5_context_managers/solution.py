"""
Q5: Custom Context Managers
A class-based Timer context manager and a generator-based safe file writer.
"""

import time
from contextlib import contextmanager


class Timer:
    """Class-based context manager that times a block of code."""

    def __enter__(self):
        self._start = time.perf_counter()
        return self  # allows `with Timer() as t:` and reading t.elapsed later

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self._start
        print(f"[Timer] Block took {self.elapsed:.6f} seconds")
        # Returning False (or None) means: don't suppress exceptions.
        return False


@contextmanager
def safe_file_writer(path):
    """
    Function-based context manager (generator style).
    Everything before `yield` = setup (__enter__).
    Everything after `yield` = teardown (__exit__), wrapped in try/finally
    so the file is always closed, even on error.
    """
    f = open(path, "w")
    try:
        yield f
    except Exception as e:
        print(f"[safe_file_writer] Caught exception while writing: {e!r}")
        # Not re-raising here means the exception is suppressed.
    finally:
        f.close()
        print(f"[safe_file_writer] File '{path}' closed.")


def main():
    print("--- Timer demo ---")
    with Timer() as t:
        total = sum(i * i for i in range(1_000_000))
    print(f"Sum of squares: {total}")
    print(f"Recorded elapsed time attribute: {t.elapsed:.6f}s\n")

    print("--- safe_file_writer demo (success case) ---")
    with safe_file_writer("demo_output.txt") as f:
        f.write("Hello from a custom context manager!\n")
    print("Write succeeded.\n")

    print("--- safe_file_writer demo (error case) ---")
    with safe_file_writer("demo_output.txt") as f:
        f.write("This line gets written.\n")
        raise ValueError("Simulated failure mid-write")
    print("Program continues after the exception was suppressed.\n")

    with open("demo_output.txt") as f:
        print("Final file contents:")
        print(f.read())


if __name__ == "__main__":
    main()
