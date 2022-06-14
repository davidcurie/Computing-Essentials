---
date: Mon May 16 14:45:36 CDT 2022
author: David Curie
title: Syllabus
subject: Programming
---

# Computing Essentials

A short workshop on computing skills useful for an experimental physicist.

0. Getting Started
    - Download git
    - Create GitHub account
    - GitIt tutorial
    - Ensure you have python 3.6+
        - Anaconda or Miniconda distribution
    - `conda` vs `pip`
    - Jupytext
    - Create Exercism account
        - Complete first exercise on each python concept
    - Tools of the trade
        - Code editor (PyCharm, VS Code, Xcode, Vim)
        - Terminal (Windows: Git Bash, Mac:Terminal)
        - Code + visualizer (JupyterLab -> App)
1. Git practices for collaboration
    - Commit practices
        - Rebase vs fast-forward
    - Git for scientific papers
    - Git for scientific projects
    - Git for this workshop's exercises
        - Advanced git usage for patching
2. Python First Steps: NumPy and Matplotlib
    - Basic math notation in Python
    - Indexing arrays
    - Plot a specified function
    - Plot a spectrum from a .csv file
    - Plot a spectrum from a .dat file
    - Plot a series of related spectra that relate to increasing power
    - Plot a waterfall spectra for a line scan
3. Data organization basics
    - Clean data practices
    - Documentation and data provenance
    - Folder structure for projects
    - Unit testing during development
    - Functional programming guidelines
    - SciPy and other operations
        - Remove cosmic rays from a spectrum
        - Fit a double-Lorentz oscillator to ODMR spectra
4. Python wrangling for microscopy
    - Building classes for data visualization
        - USID format
    - Good plotting practices
    - Open .h5 file and plot the image
        - Plot spectra from 500 nm and above (using limits and array conditionals)
    - Re-factoring into modules for better exporting
    - Generate a composite figure that plots a heatmap, spectrum, and linescan from a folder of files
    - Apply an NMF decomposition to a hyperspectral dataset and plot the results
5. Data organization for multi-parameter database
    - Shell-based manipulations
        - Bulk renaming
        - Moving
    - signac folder structure
    - Archiving in databases
6. Coding in real life
    - Design and share your own application
    - Ex: Populate Excel spreadsheet with a list of new students from a roster
        - Take my TA example and make it better
    - Ex: Design a lesson plan for this course
        - Use git to establish an initial commit describing lesson outline
        - Provide your own solution as a patch
        - Rebase any updates to your intial outline that you rewrote during your solution
    - Ex: Monte Carlo simulation

7. Dashboard/ Jupyter Widgets
    - Create interactive plot for your colleague


## More Info

- Code and Data for the Social Sciences: A Practitioner's Guide - <https://web.stanford.edu/~gentzkow/research/CodeAndData.pdf>
- Best Practices for Scientific Computing - <https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745>
- Good Enough Practices in Scientific Computing - <https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510>
- On writing clean Jupyter notebooks - <https://towardsdatascience.com/on-writing-clean-jupyter-notebooks-abdf6c708c75>
- \[Archived post on Pycroscopy\] - <https://github.com/pycroscopy/pycroscopy/blob/phoenix/docs/USID_pyUSID_pycroscopy.pdf>
- Matplotlib Usage Guide - <https://matplotlib.org/stable/tutorials/introductory/usage.html>
- Data Fitting in Python: Part I - <http://emilygraceripka.com/blog/14>
- Data Fitting in Python: Part II - <http://emilygraceripka.com/blog/16>
- Removing Spikes from Raman Spectra with Anomaly Detection: Whitaker-Hayes Algorithm in Python - <https://towardsdatascience.com/removing-spikes-from-raman-spectra-8a9fdda0ac22>
- Monte Carlo Integration In Python For Noobs (15:31) - <https://youtu.be/WAf0rqwAvgg>
- NumPy Tutorial (2022): For Physicists, Engineers, and Mathematicians (1:32:41) - <https://youtu.be/DcfYgePyedM>
- SciPy Tutorial (2022): For Physicists, Engineers, and Mathematicians (1:33:28) - <https://youtu.be/jmX4FOUEfgU>
