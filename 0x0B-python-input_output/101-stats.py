#!/usr/bin/python3
"""reads from standard input and computes.

After every ten lines or the input of a keyboard (CTRL + C),
prints the following statistics:
    - Total file size.
    - Count of read status codes.
"""


def print_stats(size, status_codes):
    """Print metrics.

    Args:
        size: read file size.
        status_codes: count of status codes.
    """
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))


if __name__ == "__main__":
    import sys

    size = 0
    statusCodes = {}
    validCodes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for l in sys.stdin:
            if count == 10:
                print_stats(size, statusCodes)
                count = 1
            else:
                count += 1

            l = l.split()

            try:
                size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in validCodes:
                    if statusCodes.get(l[-2], -1) == -1:
                        statusCodes[l[-2]] = 1
                    else:
                        statusCodes[l[-2]] += 1
            except IndexError:
                pass

        print_stats(size, statusCodes)

    except KeyboardInterrupt:
        print_stats(size, statusCodes)
        raise
