#!/usr/bin/env python3

# Created by DJ Watson
# Created on November 2019
# this program prints all possible rgb values


def main():
    counter_r = 0
    counter_g = 0
    counter_b = 0

    # process and output
    for counter_r in range(0, 256):
        for counter_g in range(0, 256):
            for counter_b in range(0, 256):
                print("RGB: {},{},{}".format(counter_r, counter_g, counter_b))


if __name__ == "__main__":
    main()
