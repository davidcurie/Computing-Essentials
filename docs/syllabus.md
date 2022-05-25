# Syllabus

Each lesson is outlined as a follow-along set of instructions contained in a single
document. These can be accessed from the `lessons` folder in this repository or online
at <https://github.com/davidcurie/Computing-Essentials/lessons/>.

## First Steps

### Git

- [Git-It](http://jlord.us/git-it/) tutorial
- Initialize a dummy repository
- Make some commits, and learn the basics
    - View diff of files
    - View history of commits
    - Push/pull basics
    - Pull requests and collaboration

#### Writing

- Publish a paper!


### Coding Setup

- IDE vs Jupyter notebooks
- Create a conda environment
    - Access environments within Jupyter Lab from base
- JupyText installation

### Python

## Navigate a thing

- Bash script to create a project populated with predefined folders
- Bash script to read contents of a file in another specified directory
- Bash script to restructure project folder
    - Move raw data to own folder
    - Move references in scripts to locate data in new raw folder

## Plot a thing: Part I

- Plot a simple spectrum
- Learn about indexing, plot a slice of a spectrum
- Plotting 2D arrays

## Compute a thing

- Lorentz fit to a curve
- Monte Carlo

## Clean a thing

- Opening an instrument file
- h5 data for microscopy
- USID introduction

## Plot a thing: Part II

- matplotlib styles
- Generate a figure for a paper
    - Waterfall plot (1D spectrum vs parameter)
        - Line scan
        - Evolving spectra with vertical offset
    - Heatmap (2D spectrum image)
    - NMF decomposition (Slices of a matrix)
    - Polarization

## Assemble a thing

- Refactor above examples into a pipeline
    - Top -> Bottom single-file pipeline

## Package a thing

- Classes for similarly themed operations
- Modules for similarly-themed scope
- Refactor above assembly into project-scope pipeline
    - Move files into Data/ Src/ and Figures/
- Example: [zipf project][zipf]

[zipf]: https://goodresearch.dev/zipf.html

## Practice a thing

- Example: physics project - NMF calculation
- Publishing to DOI repository

