"""
Script to normalize and prepare the Markdown files.

The main usefulness of this script is to renumber the headers and
auto-create the table of contents.

Usage:

From the repository root, run:

    $ python prep.py

The script should be run with Python 3.6 or newer.
"""

import re


# Relative to the repository root.
SOURCE_PATH = 'index.md'

HEADER_PATTERN = re.compile(r'#+ ')


def recursive_replace(target, old, new):
    while old in target:
        target = target.replace(old, new)

    return target


def increment_coords(coords):
    last = coords.pop()
    last += 1
    coords.append(last)


def parse_header_line(line):
    """
    Return (level, header_text).

    Args:
      line: a line of the form "### 1.1. Scope".
    """
    prefix, text = line.split(maxsplit=1)
    level = len(prefix) - 1

    return level, text


def make_header_line(level, coords, title):
    prefix = (level + 1) * '#'
    section = '.'.join(str(number) for number in coords)
    line = f'{prefix} {section}. {title}'

    return line


def transform_lines(lines, header_lines):
    level = 0
    coords = []
    for line in lines:
        match = HEADER_PATTERN.match(line)
        if match is None:
            yield line
            continue

        # Otherwise, we have a header line.
        new_level, header_text = parse_header_line(line)

        # Strip the dotted number portion from the beginning.
        title = header_text.lstrip(' 0123456789.\\')

        if new_level > level:
            coords.append(1)
        else:
            if new_level < level:
                coords = coords[:new_level]
            increment_coords(coords)
        level = new_level

        header_line = make_header_line(level, coords, title)
        header_lines.append(header_line)

        # Precede a header line with two empty lines.
        yield ''
        yield header_line


def parse_sections(text):
    """
    Return (intro, body).
    """
    divider = '\n## '
    sections = text.split(divider)

    # Skip the current contents.
    intro = sections[0]
    body = '## ' + divider.join(sections[2:])

    return intro, body


def make_anchor(header_text):
    """
    Create and return the anchor label for a section header.

    Args:
      header_text: the text portion of a header line, which should include
        the dotted section number and the title, but not the header line
        prefix which has the form "###".

    This function was written to mimic Jekyll's / GitHub Pages'
    auto-generation of element id's for header elements. For example,
    "5.2. Incremental Approach" should return "52-incremental-approach".
    """
    anchor = header_text.lower()
    # TODO: add more characters as needed.
    anchor = anchor.replace('.', '')
    anchor = anchor.replace(' ', '-')

    return anchor


def make_contents_line(header_text, level):
    prefix = 2 * (level - 1) * ' '
    anchor = make_anchor(header_text)
    line = f'{prefix}* [{header_text}](#{anchor})'

    return line


def make_contents(header_lines):
    lines = ['## Contents', '']
    for line in header_lines:
        level, header_text = parse_header_line(line)
        # Only render the first two levels.
        if level > 2:
            continue

        line = make_contents_line(header_text, level=level)
        lines.append(line)

    contents = '\n'.join(lines)

    return contents


def main():
    with open(SOURCE_PATH, encoding='utf-8') as f:
        text = f.read()

    # TODO: eliminate trailing whitespace.

    # Normalize to at most one empty line in a row.
    text = recursive_replace(text, '\n\n\n', '\n\n')

    intro, body = parse_sections(text)

    header_lines = []
    lines = body.splitlines()
    lines = list(transform_lines(lines, header_lines))
    body = '\n'.join(lines)

    contents = make_contents(header_lines)

    text = '\n\n'.join((intro, contents, body)) + '\n'

    with open(SOURCE_PATH, 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    main()
