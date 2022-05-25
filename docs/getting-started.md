# Getting Started

The exercises assume you have access to the following tools:

- A terminal
- [Git][git]
- Python 3

```{admonition} Windows
:class: warning
The default Windows PowerShell is insufficient for the lessons in this project, as the commands will use Unix syntax. Use GitBash (optional install with Windows Git), WSL/WSL2 or Windows Terminal.
```
If you are a newcomer, consider downloading the [Anaconda][anaconda]
distribution to get the latest python version and the most common packages. A
smaller but equally functional [Miniconda][miniconda] distribution exists, but
requires you to install your own packages.

```{seealso}
Beware [the difference between `conda` and `pip` ][conda-vs-pip] and why you may
choose to prefer one over the other for your package needs. If you are using
Anaconda, load `conda` packages before `pip`.
```


[git]: https://git-scm.com
[anaconda]: https://www.anaconda.com
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[conda-vs-pip]: https://pythonspeed.com/articles/conda-vs-pip/

## Optional requirements

The challenge exercises will reinforce collaborative versioning and extend
exercises from other learning resources. For these, you will need the following
additional free resources:

- [GitHub](https://github.com) account
- [Exercism](https://exercism.org) account

## Lesson Structure

The lessons will walk you through a series of tasks from some pre-defined
starting point. This starting point is defined as the state of files as they
exist in the repository for this book, under the subfolder `lessons`.

The instructions begin with you duplicating the state of files as they exist in
this repository, which is supplied as a copy-and-paste command. You are meant
to follow along with the examples sequentially, so the copy-and-paste commands
are more granular than a simple clone of this repository (which would download
all lessons and documentation at once). Additionally, cloning this repository
is not currently recommended, as the exercises will ask you to initialize your
own git folders as part of the lesson, and performing a `git init` inside of an
existing git repository leads to problems. As such, you are responsible for
organizing the output of the granular commands.

The simplest way to be responsible about the output is to start each of your
lessons with your terminal navigated to the inside of a course folder
`Computing-Essentials`. For notational brevity, the lessons assume you have
this folder located in your home directory (abbreviated `~`), but you may
consider moving this to `Documents` or another location of your choosing. This
means mentally replacing any occurrence of `~/Computing-Essentials` with
`your/path/to/Computing-Essentials`

An example lesson will start with you inside `Computing-Essentials`, running a
command to create and populate the lesson directory, and asking you to move
into the lesson directory to continue the tasks outlined in the lesson.
