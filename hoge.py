import sys


def function(default=''):
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return default


if __name__ == '__main__':
    print(function())
