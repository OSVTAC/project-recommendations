# prep.py script to prepare the Markdown files for building.
#
# Copyright (C) 2017  Christopher Jerdonek
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Contact info:
#
# The author(s) can be reached at--
#
#   Christopher Jerdonek <chris.jerdonek@gmail.com>
#

"""
Script to normalize and prepare the Markdown files prior to building.

Some of the things this script does are--

1. parse and update the section numbers of each section,
2. read the "last-approved" date, and
3. report the headers and other information via stdout.

Usage:

From the repository root, run:

    $ python scripts/prep.py

For command help, including command-line options:

    $ python scripts/prep.py -h

The script should be run with Python 3.5 or newer.
"""


import argparse
import json
import logging
import os
from pathlib import Path
import re


_log = logging.getLogger(__name__)


HEADER_PATTERN = re.compile(r'#+ ')

# The order of these names also controls the order in which the sections
# should appear in the final document.
SECTION_NAMES = [
    'copyright',
    'goals',
    'background',
    'facts-assumptions',
    'recommendations',
    'faq',
    'glossary',
]


def get_source_path(name):
    """
    Return the path to a Markdown file as a path-like object.
    """
    return Path('pages') / '{}.md'.format(name)


def write_file(text, path):
    """
    Args:
      path: a path-like object.
    """
    path = Path(path)
    _log.info('writing file: {}'.format(path))
    path.write_text(text)


def write_sections(sections, name):
    """
    Args:
      name: the base portion of the file name, for example "index" for
        index.md.
    """
    text = '\n\n'.join(sections)
    write_file(text, '{}.md'.format(name))


def lines_to_text(lines):
    text = '\n'.join(lines)
    text = text.strip()

    # End with a trailing newline.
    text += '\n'

    return text


class HeaderInfo:

    """
    Encapsulates the information needed to generate a section header line.
    """

    def __init__(self, coords, title, page):
        """
        Args:
          coords: an iterable of integers representing a section number.
            For example, (2, 3, 1) represents section 2.3.1.
          title: the section title that should follow the section number in
            the rendered text.
          page: the name of the source Markdown file containing the header
            (e.g. "background" for "background.md").
        """
        self.coords = coords
        self.page = page
        self.title = title

    def __repr__(self):
        return ('<HeaderInfo object coords={!r} title={}, page={}>'
                .format(self.coords, self.title, self.page))

    def __str__(self):
        return self.make_header_text()

    def to_json(self):
        return dict(coords=self.coords, page=self.page, title=self.title)

    def get_level(self):
        return len(self.coords)

    def make_header_text(self):
        """
        Generate and return the text portion of a header line, which
        includes the dotted section number and title, but not the header
        line prefix which has the form "###".
        """
        section = '.'.join(str(number) for number in self.coords)
        line = '{section}. {title}'.format(section=section, title=self.title)

        return line

    def make_header_line(self):
        level = self.get_level()
        header_text = self.make_header_text()

        # We precede top-level sections with "##" since we reserve "#" for
        # the overall page header.  Thus, we need to add 1.
        prefix = (level + 1) * '#'

        line = '{prefix} {header}'.format(prefix=prefix, header=header_text)

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


def transform_lines(lines, header_infos, first_section, page_name):
    """
    This function appends to the header_infos list.
    """
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
        header_info = HeaderInfo(tuple(coords), title, page_name)
        header_infos.append(header_info)

        header_line = header_info.make_header_line()

        # Precede a header line with two empty lines.
        yield ''
        yield header_line


def process_section_file(file_base, header_infos, first_section):
    """
    Parse and compute updated section numbers for a source Markdown file.

    Args:
      file_base: the base name of the file containing the section text
        (e.g. "background" for "background.md").
      header_infos: a list of HeaderInfo objects to which this function
        will add the headers it finds in the source file.
      first_section: an integer representing the first section appearing
        in the file.

    Returns: (new_text, path, has_changes).
    """
    path = get_source_path(file_base)
    _log.info('reading: {}'.format(path))
    text = path.read_text()

    # TODO: eliminate trailing whitespace.

    # Normalize to at most one empty line in a row.
    body = recursive_replace(text, '\n\n\n', '\n\n')

    lines = body.splitlines()
    lines = list(transform_lines(lines, header_infos, first_section, page_name=file_base))
    new_text = lines_to_text(lines)

    return new_text, path, (new_text != text)


def read_last_approved():
    path = Path('last-approved.txt')
    last_approved = path.read_text()
    last_approved = last_approved.strip()

    return last_approved


def parse_args():
    desc = 'Prepare the Markdown files prior to building.'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--dry-run', dest='dry_run', action='store_true',
        help="suppress overwriting the source files.")
    parser.add_argument('--no-stdout', dest='suppress_stdout', action='store_true',
        help='suppress writing to stdout.')

    ns = parser.parse_args()

    return ns


def main():
    logging.basicConfig(level=logging.INFO)

    ns = parse_args()

    total_has_changes = False
    # A list of HeaderInfo objects.
    header_infos = []
    # A dict mapping page name to page text.
    sections = {}

    for section_number, name in enumerate(SECTION_NAMES, start=1):
        new_text, path, has_changes = process_section_file(name, header_infos,
                                                first_section=section_number)
        sections[name] = new_text
        if not ns.dry_run:
            write_file(new_text, path)

        if has_changes:
            total_has_changes = True

    last_approved = read_last_approved()
    meta = dict(last_approved=last_approved, has_changes=total_has_changes,
                section_names=SECTION_NAMES)
    headers = [info.to_json() for info in header_infos]

    if ns.suppress_stdout:
        _log.info('suppressing stdout due to user option')
        return

    # Print the data to stdout so the caller has programmatic access
    # to the parsed header info.
    data = dict(_meta=meta, headers=headers, sections=sections)
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    main()
