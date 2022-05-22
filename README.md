A project to house lessons on Unix, git, and python that may be useful for
engineers, mathematicians, computer scientists, or physicists.

# Computing Essentials

A good workflow necessarily involves a reproducible analysis from raw data to
published figure that is clear to outside inspectors and is easy to maintain. A
healthier workflow automates this analysis and avoids duplication wherever
possible. The best workflows are generic enough to allow for this process to
evolve with the scope of the project and the number of collaborators.

The lessons in this project help promote a good workflow by supplying tangible
examples of automation useful to researchers and by supplying exercises to
reinforce that understanding. Optional challenges exist for those who wish to
further refine these skills.

## Introduction

The structural tone of these lessons is motivated by the following guidelines:

- [Code and Data for the Social Sciences: A Practitioner's Guide](https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf)
- [Best Practices for Scientific Computing](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745)
- [Good Enough Practices in Scientific Computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)

The above ideas are encapsulated nicely in a practical guide similar in scope to this project:

- [The Good Research Code Handbook](https://goodresearch.dev)

This project attempts to supplement the above handbook with examples that bring
a beginner up to speed with the above-mentioned guidelines. The lessons are
structured around skill objectives that expand on results from previous
lessons.

## Getting Started

The exercises assume you have access to the following tools:

- A terminal[^terminal]
- [Git][git]
- Python 3

If you are a newcomer, consider downloading the [Anaconda][anaconda]
distribution to get the latest python version and the most common packages. A
smaller but equally functional [Miniconda][miniconda] distribution exists, but
requires you to install your own packages.

> See [the difference between `conda` and `pip` ][conda-vs-pip] and why you may
> choose to prefer one over the other. If you use Anaconda to manage your
> environments, remain consistent and stick with `conda` whenever possible.

[^terminal]: Windows PowerShell is insufficient. GitBash (optional install with Windows Git) is sufficient.

[git]: https://git-scm.com
[anaconda]: https://www.anaconda.com
[miniconda]: https://docs.conda.io/en/latest/miniconda.html
[conda-vs-pip]: https://pythonspeed.com/articles/conda-vs-pip/

### Optional requirements

The challenge exercises will reinforce collaborative versioning and extend
exercises from other learning resources. For these, you will need the following
additional free resources:

- [GitHub](https://github.com) account
- [Exercism](https://exercism.org) account

## Lessons

Each lesson is outlined as a follow-along set of instructions contained in a single
document. These can be accessed from the `lessons` folder in this repository or online
at <https://github.com/davidcurie/Computing-Essentials/lessons/>.

Beginners: [Start here](lessons/first_steps)

Already comfortable with the basics? View the [syllabus](doc/src/syllabus) here to see which lessons
are most useful to you.

### First Steps

#### Git

- [Git-It](http://jlord.us/git-it/) tutorial
- Initialize a dummy repository
- Make some commits, and learn the basics
    - View diff of files
    - View history of commits
    - Push/pull basics
    - Pull requests and collaboration

##### Writing

- Publish a paper!


#### Coding Setup

- IDE vs Jupyter notebooks
- Create a conda environment
    - Access environments within Jupyter Lab from base
- JupyText installation

#### Python

### Navigate a thing

- Bash script to create a project populated with predefined folders
- Bash script to read contents of a file in another specified directory
- Bash script to restructure project folder
    - Move raw data to own folder
    - Move references in scripts to locate data in new raw folder

### Plot a thing: Part I

- Plot a simple spectrum
- Learn about indexing, plot a slice of a spectrum
- Plotting 2D arrays

### Compute a thing

- Lorentz fit to a curve
- Monte Carlo

### Clean a thing

- Opening an instrument file
- h5 data for microscopy
- USID introduction

### Plot a thing: Part II

- matplotlib styles
- Generate a figure for a paper
    - Waterfall plot (1D spectrum vs parameter)
        - Line scan
        - Evolving spectra with vertical offset
    - Heatmap (2D spectrum image)
    - NMF decomposition (Slices of a matrix)
    - Polarization

### Assemble a thing

- Refactor above examples into a pipeline
    - Top -> Bottom single-file pipeline

### Package a thing

- Classes for similarly themed operations
- Modules for similarly-themed scope
- Refactor above assembly into project-scope pipeline
    - Move files into Data/ Src/ and Figures/
- Example: [zipf project][zipf]

[zipf]: https://goodresearch.dev/zipf.html

### Practice a thing

- Example: physics project - NMF calculation
- Publishing to DOI repository
