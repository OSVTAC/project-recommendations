# Contributing

This document contains instructions for making, previewing, and suggesting
changes to OSVTAC'S recommendations via GitHub.

You must be familiar with Git, Markdown, and using the command-line.


## Fork the repository

First, fork the repository to your personal account on GitHub.

Then, clone your fork to your local machine:

    $ git clone https://github.com/<your-username>/project-recommendations.git
    $ cd project-recommendations
    $ git submodule update --init

The `git submodule` command is present because the repository uses a Git
[submodule][git-submodules] to store binary files referenced by the
recommendations (e.g. PDF's).


## Previewing Locally

You can preview the repository (including any changes you are working on) on
your local machine through your browser using the command-line tool
[Jekyll][jekyll-github], which we describe below. Jekyll is what GitHub uses
to render [GitHub Pages](https://pages.github.com/).

The repository is configured in the [`_config.yml`](_config.yml) file to use
GitHub's ["slate"](https://github.com/pages-themes/slate) theme locally. This
theme was chosen because it is very similar to the theme of OSVTAC's site,
which OSVTAC uses to display these recommendations.


### Setup

Running Jekyll requires [Ruby][ruby], so first install a current version of
Ruby. As of August 2017, the latest stable version of Ruby was 2.4.1.

You can check what version of Ruby you are currently using by running:

    $ ruby --version

We recommend using [RVM][rvm] to install and manage the versions
of Ruby installed on your machine. Instructions for installing RVM are on
the RVM [home page][rvm], with more detailed instructions (e.g. for different
platforms) on the [Installing RVM][rvm-install] page.

[rvm]: https://rvm.io/
[rvm-install]: https://rvm.io/rvm/install

With RVM, you can list all of your
installed Ruby versions with:

    $ rvm list

Next, install Jekyll and the theme's dependencies, etc. From the repository
root:

    $ bundle install

The `bundle` command above installs each of the needed Ruby gems (project
dependencies), using the version numbers specified in
[`Gemfile.lock`](Gemfile.lock).


### Running Locally

To run and preview the site locally, run the following from the
repo root:

    $ bundle exec jekyll serve

This writes the generated pages to a subdirectory called `_site`.

Then browse to: [http://127.0.0.1:4000](http://127.0.0.1:4000).


## Making Changes

Files in the repository are written in [Markdown][markdown].

You should group unrelated changes separately in different branches.


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
[ruby]: https://www.ruby-lang.org
