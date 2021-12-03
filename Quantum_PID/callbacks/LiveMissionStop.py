#!/usr/bin/env python3
#!/usr/bin/env python2

import argparse
import time
import numpy
import struct
import matplotlib .pyplot as plt


def main(Command):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Callback for Live Mission Commands')
    parser.add_argument('MissionParams', help='')
    args = parser.parse_args()
    main(args.MissionParams)



