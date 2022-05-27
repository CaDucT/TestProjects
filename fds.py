import os
import inspect

descriptors = set()
def print_open_fds(print_all=False):
    global descriptors
    (frame, filename, line_number, function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    fds = set(os.listdir('/proc/self/fd/'))
    new_fds = fds - descriptors
    closed_fds = descriptors - fds
    descriptors = fds

    if print_all:
        print("{}:{} ALL file descriptors: {}".format(filename, line_number, fds))

    if new_fds:
        print("{}:{} new file descriptors: {}".format(filename, line_number, new_fds))
    if closed_fds:
        print("{}:{} closed file descriptors: {}".format(filename, line_number, closed_fds))