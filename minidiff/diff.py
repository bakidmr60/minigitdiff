# usage: python3 diff.py test/test1.py test/test2.py
import sys


def diff_tool():
    first_file = sys.argv[1]
    second_file = sys.argv[2]

    with open(first_file) as f:
        first_file_lines = f.readlines()

    with open(second_file) as f:
        second_file_lines = f.readlines()

    diffs = "Differences:\n\n"

    start_indices = []
    end_indices = []
    hasdiff = False

    max_len = max(len(first_file_lines), len(second_file_lines))

    for i in range(max_len):
        line1 = first_file_lines[i] if i < len(first_file_lines) else None
        line2 = second_file_lines[i] if i < len(second_file_lines) else None

        if line1 != line2 and not hasdiff:
            hasdiff = True
            start_indices.append(i)
        elif line1 == line2 and hasdiff:
            hasdiff = False
            end_indices.append(i - 1)

    if hasdiff:
        end_indices.append(max_len - 1)

    for i in range(len(end_indices)):
        start = start_indices[i]
        end = end_indices[i]

        diffs += f"Lines {start}:{end}:\n"

        diffs += f"{first_file}:\n"
        for j in range(start, end + 1):
            if j < len(first_file_lines):
                diffs += f"- {first_file_lines[j].rstrip()}\n"

        diffs += f"{second_file}:\n"
        for j in range(start, end + 1):
            if j < len(second_file_lines):
                diffs += f"+ {second_file_lines[j].rstrip()}\n"

        diffs += "\n"

    print(diffs)


diff_tool()