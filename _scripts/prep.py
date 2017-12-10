"""
Script to normalize and prepare the Markdown files for publication.

Some of the things this script does are--

1. generate the correct section numbers for each section,
2. generate the table of contents with hyperlinks to each section, and
3. generate both "single-page" and "multi-page" versions of the
   document.

Usage:

From the repository root, run:

    $ python _scripts/prep.py

The script should be run with Python 3.6 or newer (because it uses
f-strings, for example).
"""

# prep.py script to prepare Markdown files for publishing with Jekyll.
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

import logging
import os
import re


_log = logging.getLogger(__name__)


HEADER_PATTERN = re.compile(r'#+ ')

# See make_anchor() for the purpose of this dict.
# TODO: add more characters as needed.
ANCHOR_TRANS = {
    ' ': '-',
    '.': None,
    '&': None,
}

# These names correspond to files in the _source directory, in the
# order they should appear in the final document.
SECTION_NAMES = [
    'goals',
    'background',
    'facts-assumptions',
    'recommendations',
    'faq',
    'glossary',
]

TOC_LINK = """\
* [Introduction & Table of Contents](index) (for multi-page version)"""

SINGLE_PAGE_LINK = """\
* [Single-page version](single-page) (long, can be used for printing)"""


# This html was copied from https://creativecommons.org in the instructions
# for using CC BY-SA 4.0 for your own material.
CC_LICENSE = """\
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">
<img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" />
</a><br />This work is licensed under a
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative
Commons Attribution-ShareAlike 4.0 International License</a>.
"""


def get_source_path(name):
    """
    Return the path to a Markdown file in the _source directory.
    """
    return os.path.join('_source', f'{name}.md')


def read_file(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()

    return text


def write_file(text, path):
    _log.info(f'writing file: {path}')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def write_sections(sections, name):
    """
    Args:
      name: the base portion of the file name, for example "index" for
        index.md.
    """
    text = '\n\n'.join(sections)
    write_file(text, f'{name}.md')


def read_source_file(name):
    """
    Read a Markdown file in the _source directory.
    """
    path = get_source_path(name)
    text = read_file(path)

    return text


def lines_to_text(lines):
    text = '\n'.join(lines)
    text = text.strip()

    # End with a trailing newline.
    text += '\n'

    return text


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
    trans = str.maketrans(ANCHOR_TRANS)
    anchor = anchor.translate(trans)

    return anchor


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
        return f'<HeaderInfo object coords={self.coords!r} title={self.title}, page={self.page}>'

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
        level = self.get_level()
        header_text = self.make_header_text()

        # We precede top-level sections with "##" since we reserve "#" for
        # the overall page header.  Thus, we need to add 1.
        prefix = (level + 1) * '#'

        line = f'{prefix} {header_text}'

        return line

    def make_contents_line(self, page_name=None):
        """
        Makes a table of contents line for the current header.

        Args:
          page_name: the name of the page to which the contents entry
            should link.  Defaults to the name of the page that originally
            contained the header.

        An example with page_name None could be--

          "  * [2.2. Voting System](background#22-voting-system)"

        With page_name '', this same example would be--

          "  * [2.2. Voting System](#22-voting-system)"

        """
        if page_name is None:
            page_name = self.page

        level = self.get_level()
        indent = 2 * (level - 1) * ' '

        header_text = self.make_header_text()
        anchor = make_anchor(header_text)

        line = f'{indent}* [{header_text}]({page_name}#{anchor})'

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


def make_contents(header_infos, page_name=None):
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

        line = header_info.make_contents_line(page_name=page_name)
        lines.append(line)

    contents = lines_to_text(lines)

    return contents


def process_section_file(page_name, header_infos, first_section):
    """
    Parse and fix the section numbers in a source Markdown file.

    Args:
      page_name: the name of the page (e.g. "background" for "background.md").
      header_infos: a list of HeaderInfo objects to which this function
        will add the headers it finds in the source file.
      first_section: an integer representing the first section appearing
        in the file.
    """
    path = get_source_path(page_name)
    text = read_file(path)

    # TODO: eliminate trailing whitespace.

    # Normalize to at most one empty line in a row.
    body = recursive_replace(text, '\n\n\n', '\n\n')

    lines = body.splitlines()
    lines = list(transform_lines(lines, header_infos, first_section, page_name=page_name))
    body = lines_to_text(lines)

    write_file(body, path)

    return body


class Renderer:

    """
    Responsible for writing the top-level Markdown files.
    """

    def __init__(self, page_intro, reference_links):
        self.license_text = CC_LICENSE
        self.page_intro = page_intro
        self.reference_links = reference_links

    def write_rendered_file(self, name, intro_sections, main_sections):
        """
        Args:
          intro_sections, main_sections: the intro sections and main
            sections, respectively.  Each value should be an iterable of
            strings, one for each section.  Moreover, each string section
            should end in a single trailing newline.
          name: the base portion of the file name, for example "index" for
            index.md.
        """
        sections = [
            self.page_intro,
            *intro_sections,
            self.license_text,
            *main_sections,
            self.reference_links,
            self.license_text,
        ]
        write_sections(sections, name=name)

    def render_index_page(self, header_infos):
        intro = read_source_file('intro')
        contents = make_contents(header_infos)

        self.write_rendered_file('index', [intro, SINGLE_PAGE_LINK], [contents])

    def render_section_page(self, name, body_text):
        self.write_rendered_file(name, [TOC_LINK, SINGLE_PAGE_LINK], [body_text])

    def render_single_page_version(self, sections, header_infos):
        # Pass '' for the page_name so that section links will point to
        # the same page that is being viewed.
        contents = make_contents(header_infos, page_name='')
        main_sections = [contents] + sections

        self.write_rendered_file('single-page', [TOC_LINK], main_sections)

    def render_copyright_page(self):
        copyright_text = read_source_file('copyright')

        sections = [
            self.page_intro,
            copyright_text,
        ]
        write_sections(sections, name='copyright')


def main():
    logging.basicConfig(level=logging.INFO)

    page_intro = read_source_file('page-intro')
    reference_links = read_source_file('reference-links')
    renderer = Renderer(page_intro, reference_links)

    # A list of HeaderInfo objects.
    header_infos = []
    sections = []

    for section_number, name in enumerate(SECTION_NAMES, start=1):
        section = process_section_file(name, header_infos, first_section=section_number)
        sections.append(section)

        renderer.render_section_page(name, section)

    renderer.render_index_page(header_infos)
    renderer.render_single_page_version(sections, header_infos)
    renderer.render_copyright_page()


if __name__ == '__main__':
    main()
