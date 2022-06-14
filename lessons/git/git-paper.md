# Git for Scientific Papers

```{admonition} Prerequisites
- [Git-It](http://jlord.us/git-it) tutorial
- First Steps with Git
```

```{topic} Objectives
- Track changes on a paper
- Collaborate on a paper
```

We've seen how Git tracks files and subfolders in a repository, but we can hack
this workflow for simpler tasks like tracking changes in a text document.
With online Git protocols, we can collaborate and edit documents in
ways that supersede storing a paper in a synchronized online folder or using
familiar _Track Changes_ features in Google Docs or Microsoft Word.
Furthermore, scientific papers are often written in $\LaTex$, where native
_Track Changes_ features are not available.

Online versioning of collaborative $\LaTex$ documents exist at
[Overleaf](https://overleaf.com) (formerly ShareLatex), which are basically
online Git repositories at heart. These services can be replicated for free
with a proper understanding of Git.

Here we practice local versioning of a text document to present meaningful
changes to advisors, co-authors, or editors.

## Writing a scientific paper

A healthily maintained series of commits on a single file already tells a story
of the changes that were made over time, but these messages should only provide a
high-level overview of the progress. We can investigate the granular changes in
each commit or compare changes from two arbitrary commits in a way that
replicates a _Track Changes_ feature in other proprietary editors.

We'll start by creating a new repository for our paper.

```bash
~/Computing-Essentials $ mkdir git-paper && cd git-paper
~/Computing-Essentials/git-paper $ git init
```

We'll then add a blank document and set it under version control. For this
example, we'll use a plain markdown file called `main.md` for our draft.

```bash
~/Computing-Essentials/git-paper $ touch main.md
~/Computing-Essentials/git-paper $ git add . && git commit -m "Initial commit"
[main (root-commit) 53a9abb] Initial commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 main.md
```

### Track changes

We'll start by overwriting the contents of `main.md` with a dummy file that
will represent our first draft. You can inspect the file before you download it
[here][draft1].

[draft1]:
https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/git/draft_1.md

```bash
~/Computing-Essentials $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/git/draft_1.md > main.md
```

Then commit these changes to our repository:

```bash
~/Computing-Essentials/git-paper $ git add main.md && git commit -m "Add opening paragraph"
```

We'll repeat this for two more drafts.

```bash
~/Computing-Essentials $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/git/draft_2.md > main.md
~/Computing-Essentials/git-paper $ git add main.md && git commit -m "Add conclusion paragraph"
```

```bash
~/Computing-Essentials $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/git/draft_3.md > main.md
~/Computing-Essentials/git-paper $ git add main.md && git commit -m "Rewrite introduction"
```

We can mimic the _Track Changes_ feature of Word by looking at the difference
of two files in Git. The general syntax for this purpose is:

```bash
 $ git diff [<options>] <commit>...<commit> -- [<path>]
```

The `commit` values represent the _start_ and _end_ commits you want the
difference between and `[<path>]` is the file(s) to inspect.

#### Compare two earlier drafts

To view the difference between the first draft and the second draft, we need to
first know the commits where those drafts were contained.

```bash
~/Computing-Essentials/git-paper $ git log --oneline
6872fc1 (HEAD -> main) Rewrite introduction
69800c3 Add conclusion paragraph
c951ed4 Add opening paragraph
53a9abb Initial commit
```

In our example, the drafts are stored at `HEAD~2` and `HEAD~1` for the first
and second draft, respectively. We can see the line-by-line changes between the
files displayed on the terminal.

```bash
~/Computing-Essentials $ git diff HEAD~2...HEAD~1 -- main.md
```

Here, we can see that the commit message logically corresponded to an
additional paragraph appended to our first draft by noticing the newline
additions.

#### Compare all changes

If we want to see how the most recent draft has changed since a particular
commit, we can leave off one of the `<commit>` specifiers; Git will
automatically compare against `HEAD`.

```bash
~/Computing-Essentials/git-paper $ git diff HEAD~2... -- main.md
```

We see the results of _Add conclusion paragraph_ and _Rewrite introduction_
commits.

#### Save changes to file

The terminal output is helpful if we want to see for ourselves the changes
between versions, but if our advisor asks us to see the changes, we may decide
to write this to a file.

We can redirect the output to a file with `> filename.ext`

```bash
~/Computing-Essentials $ git diff HEAD~2 main.md > v1-v3_comparison.txt
```

We can then share the file `v1-v3_comparison.txt` file instead of `main.md` as
it exists in its draft 3 form. More importantly, we don't need to worry about
keeping every iteration of draft, changes, and corrections from each editor
because we know that these diff files can be generated from inside Git. This
means we can safely delete the `v1-v3_comparison.txt` file after we've sent it,
which keeps our directory clean.

### Collaborating with other authors





