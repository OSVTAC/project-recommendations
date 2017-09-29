"""
Script to normalize and prepare the Markdown files.

The main usefulness of this script is to renumber the headers.

Usage:

From the repository root, run:

    $ python prep.py

The script should be run with Python 3.6 or newer.
"""

import re


# Relative to the repository root.
SOURCE_PATH = 'index.md'

# Start with "#" to exclude the document title.
HEADER_PATTERN = re.compile(r'#(?P<prefix>#+) (?P<remainder>.*)')


def recursive_replace(target, old, new):
    while old in target:
        target = target.replace(old, new)

    return target


def increment_coords(coords):
    last = coords.pop()
    last += 1
    coords.append(last)


def make_header(coords, title):
    prefix = (len(coords) + 1) * '#'

    if coords == [1]:
        assert title == 'Contents'
        section = ''
    else:
        # Subtract one because we skipped numbering the Contents.
        new_coords = [coords[0] - 1]
        new_coords.extend(coords[1:])
        section = '.'.join(str(number) for number in new_coords)
        section += '. '

    line = f'{prefix} {section}{title}'

    return line


def tranform_lines(lines):
    level = 0
    coords = []
    for line in lines:
        match = HEADER_PATTERN.match(line)
        if match is None:
            yield line
            continue

        # Otherwise, we have a header line.
        prefix = match['prefix']
        remainder = match['remainder']
        # Strip the dotted number portion from the beginning.
        title = remainder.lstrip(' 0123456789.\\')

        new_level = len(prefix)
        if new_level > level:
            coords.append(1)
        else:
            if new_level < level:
                coords = coords[:new_level]
            increment_coords(coords)
        level = new_level

        # Precede a header line with two empty lines.
        yield ''
        yield make_header(coords, title)


def main():
    with open(SOURCE_PATH, encoding='utf-8') as f:
        text = f.read()

    # TODO: eliminate trailing whitespace.

    # Normalize to at most one empty line in a row.
    text = recursive_replace(text, '\n\n\n', '\n\n')

    lines = text.splitlines()
    lines = tranform_lines(lines)
    text = '\n'.join(lines) + '\n'

    with open(SOURCE_PATH, 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    main()
