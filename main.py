# This is a sample Python script.
from environs import Env
import volumes
env = Env()
env.read_env('volumes/.env')
code1: str = env('my_test_code')


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'pidooor, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print (code1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
