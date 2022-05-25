A project to house lessons on Unix, git, and python that may be useful for
engineers, mathematicians, computer scientists, or physicists.

# Computing Essentials Source

Lessons and documents for Computing Essentials live here. View the documentation in your browser at <https://davidcurie.github.io/Computing-Essentials/index.html>. The book is built with [jupyter-book][jupyter-book] and uses a modified [Furo][furo] theme for sphinx.

[jupyter-book]: https://jupyterbook.org/en/stable/intro.html
[furo]: https://github.com/pradyunsg/furo 

## Building the book

Clone and navigate to this repo on your local computer. Then create and activate a new environment:

```sh
conda env create -n ce --file environment.yml
conda activate ce
```

Build the book from the root of the directory:

```sh
jupyter-book build .
```

Use `jupyter-book build . --all` to force a full rebuild.

## Building the book to PDF

```sh
jupyter-book . --builder pdflatex
```
