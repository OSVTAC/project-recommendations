# Contributing

This document contains instructions for suggesting changes to OSVTAC'S
recommendations using GitHub.

To do this you must be familiar with technologies like Git, GitHub,
[Markdown][markdown], and using the command-line. If you are not familiar
with these technologies, consult the repository's [`README`](README.md) file
for other ways of providing feedback to the committee.

## Repo Organization

Below is a description of how this repository is organized.

* The [`pages`](pages) directory contains the document text.

* The `files` directory is a [Git submodule][git-submodules] to a repository
  containing copies of binary files that are referenced by the
  recommendations document (e.g. PDF's):
  <https://github.com/OSVTAC/project-recommendations-files>.

* The [`scripts`](scripts) directory contains a Python script
  [`prep.py`](scripts/prep.py) for parsing the section headers, as well as
  updating them in place (e.g. if a new section is inserted in the middle).
  This script should only be run _after_ merging pull requests, so
  contributors should not normally run this script. The script is licensed
  under the GNU General Public License v3.0 or later ([SPDX][spdx-licenses]
  identifier `GPL-3.0+`).

* The [`reference-links.md`](reference-links.md) file contains all
  "reference-style" links used throughout the recommendations. The build
  script (which is not contained in this repository) appends this file to the
  end of each generated Markdown file.

Thus, pull requests will normally need to modify only files in the `pages`
directory, as well as possibly the `reference-links.md` file.


## Organizing Your Changes

You should put unrelated changes in different branches, and submit them
separately.

Moreover, do not update or attempt to fix any of the section numbers if your
changes affect the section numbering. Doing so makes it harder to locate only
the textual changes, and can also introduce needless conflicts when merging.
If your PR is merged, the section numbers and table of contents will be
updated after merging using this repository's
[`scripts/prep.py`](scripts/prep.py) script.


## Suggesting Changes

To suggest the changes in one of your branches, create a [pull
request][github-pull-request] (aka PR) from your branch on GitHub.

Note: don't expect responses from committee members on GitHub since by local
and state law, committee members aren't allowed to collaborate as a group
outside of in-person public meetings. See the [`README`](README.md) file of
this repository for more details.


## Local Workflows

There are two possible workflows you can use when preparing pull requests.
The first workflow is the simplest but doesn't let you "preview" how the
Markdown will look in a browser and as part of the larger document. The
second does let you preview your changes in a browser before submitting, but
it requires significantly more setup. The subsections below instruct you how
to follow both of these workflows.

Note that if you start with Workflow #1, it will not necessarily be easy to
"move" any changes you are working on into the Workflow #2 approach without
advanced knowledge of Git.

Finally, note that the Markdown files checked into this repository cannot
faithfully be viewed from within GitHub's UI / Markdown viewer. For example,
Markdown hyperlinks will not necessarily display or work correctly. To check
that hyperlinks are working correctly, you must preview locally (e.g. using
the second workflow described below).


### Both Workflows

For both workflows, start out by forking the repository using GitHub's UI.


### Workflow #1 (no previewing)

For this workflow, follow the instructions on GitHub's UI for cloning from
your personal fork. For example:

    $ git clone https://github.com/<your-username>/project-recommendations.git


### Workflow #2 (allows previewing)

With this workflow, you will be cloning the repository that contains the
"built" version of the files in this repository (called
[`project-recommendations-site`][recommendations-site-repo]). That repository
contains the repository you are currently viewing as a Git
[submodule][git-submodules] (i.e. separate Git repository in a subdirectory).
You will be working on this repository by working in the copy that sits as a
subdirectory of that parent repository. You will be able to connect that copy
to your personal fork using [`git remote add`][git-add-remote].

To follow this approach, follow the instructions in the
[`README`][recommendations-site-repo] file of the
`project-recommendations-site` repository:
<https://github.com/OSVTAC/project-recommendations-site>. That `README` file
also contains an overview of how the Markdown files in this repository are
built and rendered on the [OSVTAC website][osvtac-site], which can be seen
[here][recommendations-site].


[git-add-remote]: https://help.github.com/articles/adding-a-remote/
[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[github-pull-request]: https://help.github.com/articles/creating-a-pull-request/
[markdown]: https://guides.github.com/features/mastering-markdown/
[osvtac-site]: https://osvtac.github.io/
[recommendations-site]: https://osvtac.github.io/recommendations/
[recommendations-site-repo]: https://github.com/OSVTAC/project-recommendations-site
[spdx-licenses]: https://spdx.org/licenses/
