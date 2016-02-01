from __future__ import print_function

import sys


def count_rows(grid):
    rows = []
    for y in xrange(len(grid)):
        row = []
        count = 0
        for x in xrange(len(grid[0])):
            c = grid[y][x]
            if c == "*":
                count += 1
            elif count > 0:
                row.append(count)
                count = 0
        if count or not(row):
            row.append(count)
        rows.append(row)
    return rows


def print_rows(rows):
    print("Rows:")
    max_set_count = max(map(lambda x: len(x), rows))
    for row in rows:
        while len(row) < max_set_count:
            row = [" "] + row
        print(" ".join(map(str, row)))


def count_cols(grid):
    cols = []
    for x in xrange(len(grid[0])):
        col = []
        count = 0
        for y in xrange(len(grid)):
            c = grid[y][x]
            if c == "*":
                count += 1
            elif count > 0:
                col.append(count)
                count = 0
        if count or not(col):
            col.append(count)
        cols.append(col)
    return cols


def print_cols(cols, offset=0):
    print("Cols:")
    max_set_count = max(map(lambda x: len(x), cols))
    for i in xrange(max_set_count - 1, -1, -1):
        for col in cols:
            col = col[::-1]
            if len(col) > i:
                print(col[i], end=" ")
            else:
                print(" ", end=" ")
        print("")


def print_bounds(rows, cols):
    """Ignore this mess."""
    max_set_count_rows = max(map(lambda x: len(x), rows))
    max_row_str = max(map(lambda x: len(str(max(x))), rows))

    row = rows[0]
    while len(row) < max_set_count_rows:
        row = [" "] + row
    offset = len(" ".join(map(lambda x: ("{:>" + str(max_row_str) + "}").format(x), row)))

    max_set_count_cols = max(map(lambda x: len(x), cols))
    for i in xrange(max_set_count_cols - 1, -1, -1):
        print(" " * offset, end="")
        for col in cols:
            col = col[::-1]
            if len(col) > i:
                print(("{:>" + str(max_row_str) + "}").format(col[i]), end=" ")
            else:
                print(("{:>" + str(max_row_str) + "}").format(" "), end=" ")
        print("")

    for row in rows:
        while len(row) < max_set_count_rows:
            row = [" "] + row
        print(" ".join(map(lambda x: ("{:>" + str(max_row_str) + "}").format(x), row)))


def main():
    grid = []
    for line in sys.stdin:
        grid.append(line[:len(line) - len(line) % 5])

    rows = count_rows(grid)
    cols = count_cols(grid)
    print_bounds(rows, cols)

    return 0


if __name__ == "__main__":
    sys.exit(main())
