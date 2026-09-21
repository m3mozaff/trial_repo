import numpy as np
import getpass


def print_numpy_array(arr):
    print("Numpy Array:")
    print(arr)


def print_username():
    """Print the current system username.

    Uses getpass.getuser() which is safe across platforms and environments.
    """
    username = getpass.getuser()
    print(f"Username: {username}")


if __name__ == "__main__":
    # demo output
    print_username()
    print("first_script.py is running")


