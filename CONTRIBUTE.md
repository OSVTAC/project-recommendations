# Contributing

This document contains instructions for suggesting changes to OSVTAC'S
recommendations using GitHub.

To do this you must be familiar with technologies like Git, GitHub,
[Markdown][markdown], and using the command-line. If you are not familiar
with these technologies, consult the [`README`](README.md) file for other
ways of providing feedback to the committee.


## Previewing Locally

If you would like to preview your changes locally through the browser before
submitting them, it is recommended that you clone the
[project-recommendations-site][repo-recommendations-site] repository and work
on your changes as a submodule of that repository.

As background, the [OSVTAC website][osvtac-site] displays OSVTAC's
recommendations by including the project-recommendations-site repository as a
[submodule][git-submodules] of the [OSVTAC website
repository][repo-osvtac-site]. The project-recommendations-site repository
contains Markdown files for displaying the recommendations. These Markdown
files are auto-generated (aka "built") from the Markdown files in the
project-recommendations repository, which are the "source" files.

The project-recommendations-site repository contains a script for building
the Markdown files from the source Markdown files. In addition, for
convenience, the project-recommendations-site repository contains the
project-recommendations repository as a submodule.

Thus, to preview your changes to the recommendations locally, you can view
the project-recommendations-site repository in your browser using
[Jekyll][jekyll-github]. Make your changes to the project-recommendations
submodule, and then run the build script to update the html files served
locally by Jekyll. The `README` file in the project-recommendations-site
repository contains detailed instructions on how to do this.


## Organizing Your Changes

You should put unrelated changes in different branches.

Moreover, do not update or attempt to fix the section numbers if your changes
affect the section numbering. If your PR is merged, the section numbers and
table of contents will be updated after merging using this repository's
[`_scripts/prep.py`](_scripts/prep.py) script.


## Suggesting Changes

To suggest the changes in one of your branches, create a [pull
request][github-pull-request] (aka PR) from your branch on GitHub.

Note: don't expect responses from committee members on GitHub since by local
and state law, committee members aren't allowed to collaborate as a group
outside of in-person public meetings. See the [`README`](README.md) file of
this repository for more details.


[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[github-pull-request]: https://help.github.com/articles/creating-a-pull-request/
[jekyll-github]: https://jekyllrb.com/docs/github-pages/
[markdown]: https://guides.github.com/features/mastering-markdown/
[osvtac-site]: https://osvtac.github.io/
[repo-osvtac-site]: https://github.com/OSVTAC/OSVTAC.github.io
[repo-recommendations-site]: https://github.com/OSVTAC/project-recommendations-site
