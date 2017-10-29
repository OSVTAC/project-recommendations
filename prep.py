"""
Script to normalize and prepare the Markdown files.

The main usefulness of this script is to renumber the headers and
auto-create the table of contents.

Usage:

From the repository root, run:

    $ python prep.py

The script should be run with Python 3.6 or newer.
"""

from collections import namedtuple
import re


# Relative to the repository root.
SOURCE_PATH = 'index.md'

HEADER_PATTERN = re.compile(r'#+ ')


def make_anchor(header_text):
    """
    Create and return the anchor label for a section header.

    Args:
      header_text: the text portion of a header line, which includes the
        dotted section number and title, but not the header line prefix
        which has the form "###".

    This function was written to mimic Jekyll's / GitHub Pages'
    auto-generation of element id's for header elements. For example,
    "5.2. Incremental Approach" should return "52-incremental-approach".
    """
    anchor = header_text.lower()
    # TODO: add more characters as needed.
    anchor = anchor.replace('.', '')
    anchor = anchor.replace(' ', '-')

    return anchor


class HeaderInfo:

    """
    Encapsulates the information needed to generate a section header line.
    """

    def __init__(self, coords, title):
        """
        Args:
          coords: an iterable of integers representing a section number.
            For example, (2, 3, 1) represents section 2.3.1.
          title: the section title that should follow the section number in
            the rendered text.
        """
        self.coords = coords
        self.title = title

    def __repr__(self):
        return f'<HeaderInfo object coords={self.coords!r} title={self.title}>'

    def __str__(self):
        return self.make_header_text()

    def get_level(self):
        return len(self.coords)

    def make_header_text(self):
        """
        Generate and return the text portion of a header line, which
        includes the dotted section number and title, but not the header
        line prefix which has the form "###".
        """
        section = '.'.join(str(number) for number in self.coords)
        line = f'{section}. {self.title}'

        return line

    def make_header_line(self):
        """
        Args:
          header_info: a HeaderInfo object.
        """
        level = self.get_level()
        header_text = self.make_header_text()

        # We precede top-level sections with "##" since we reserve "#" for
        # the overall page header.  Thus, we need to add 1.
        prefix = (level + 1) * '#'

        line = f'{prefix} {header_text}'

        return line

    def make_contents_line(self):
        level = self.get_level()
        indent = 2 * (level - 1) * ' '

        header_text = self.make_header_text()
        anchor = make_anchor(header_text)

        line = f'{indent}* [{header_text}](#{anchor})'

        return line


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


def transform_lines(lines, header_infos, first_section=None):
    """
    This function appends to the header_infos list.
    """
    if first_section is None:
        first_section = 1

    level = 1
    coords = [first_section - 1]
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

        # Apply tuple() to freeze the data since we are mutating coords
        # in this function.
        header_info = HeaderInfo(tuple(coords), title)
        header_infos.append(header_info)

        header_line = header_info.make_header_line()

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


def make_contents(header_infos):
    """
    Args:
      header_infos: an iterable of HeaderInfo objects.
    """
    lines = ['## Contents', '']
    for header_info in header_infos:
        level = header_info.get_level()

        # Only render the first two levels.
        if level > 2:
            continue

        line = header_info.make_contents_line()
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

    # A list of HeaderInfo objects.
    header_infos = []
    lines = body.splitlines()
    lines = list(transform_lines(lines, header_infos))
    body = '\n'.join(lines)

    contents = make_contents(header_infos)

    text = '\n\n'.join((intro, contents, body)) + '\n'

    with open(SOURCE_PATH, 'w', encoding='utf-8') as f:
        f.write(text)


if __name__ == '__main__':
    main()
