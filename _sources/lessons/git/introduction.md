# Git

```{admonition} Prerequisites
- [Git-It](http://jlord.us/git-it) tutorial
- First Steps
```

```{topic} Objectives
- Document a project
- Collaborate on a scientific paper
```

## First Steps extension

The _First Steps_ lesson had you move files in your filesystem in some
non-trivial ways. We overwrote filenames with presumably more descriptive
names, but what if we later want to edit the names further and forgot what the
original names of those files were?

One sensible thing to do would be to create a backup of the existing files as
they existed before we executed our renaming script. Creating a physical backup
as a duplicate folder on our filesystem is a good first-order effort, but this
can be wasteful if we have exceptionally large folders. <mark>A backup of your
data should exist in some location other than where you are working on the
files</mark>, but for the purposes of this example we'll demonstrate how to
document the changes that are more local to your workflow.

### Creating a Git repository

We'll begin by restarting our _First Steps_ exercise from a blank slate. Let's
backup our existing `first-steps` folder and recreate an empty `first-steps`
folder to properly document our project.

```bash
~/Computing-Essentials $ mv first-steps first-steps.bk
~/Computing-Essentials $ mkdir first-steps
```

Navigate to our new blank directory and initialize a local Git repository.

```bash
~/Computing-Essentials $ cd first-steps
~/Computing-Essentials/first-steps $ git init
Initialized empty Git repository in /Users/YOURNAME/Computing-Essentials/first-steps/.git/
```

From here on out, any changes to files or directories inside this new
`first-steps` folder will be tracked by Git, but we need to know how to ask Git
for the changes.

### Populate initial files

Let's pretend that we'll eventually make this data public. Find an appropriate
[licence][license] and place the text into a file called `LICENSE` (no
extension). We'll create a GNU GPL v3 license for this example by copying the
raw text from the license in this project's source repository and writing it to
a file called `LICENSE`.

[license]: https://choosealicense.com

```{note}
If you create a repository directly on GitHub, you can select your
own license from a dropdown menu. The following command will then be obsolete.
```

```bash
~/Computing-Essentials/first-steps $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/LICENSE > LICENSE
```

Let's also add a blank README file that we can later use to document notes to
our end users.

```bash
~/Computing-Essentials/first-steps $ touch README
```

Let's see the effects of the changes we made to our repository by running the
following command:

```bash
~/Computing-Essentials/first-steps $ git status
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        LICENSE
        README

nothing added to commit but untracked files present (use "git add" to track)
```

This means Git knows files have been added (under untracked files), but it's
our job to tell Git to start tracking these files. We can then incorporate
tracked files as snapshots of the file as they exist at the time they are added
to a commit.

### Add and commit changes

Let's make a checkpoint of the state of our folder as it exists after our
LICENSE and (blank) README. We can do this with `git add <file>` for each file
that we want to save. The command can be run once for each file, or you can
list multiple files after `add`. You can also add all files with the shortcut
notation `.` (period).

```bash
~/Computing-Essentials/first-steps $ git add .
```

Nothing on the terminal tells us if this executed properly, but we can
re-inspect our repository.

```bash
~/Computing-Essentials/first-steps $ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   LICENSE
        new file:   README
```

We see that our two files are newly added to the staging directory. We can
group these changes to our directory as one searchable collection of
modifications called a _commit_.

```bash
~/Computing-Essentials/first-steps $ git commit
```

Executing the previous command will bring up a temporary text file with some
populated information about the changes we are about to save. The first line of
this file will be displayed as a message in our log. We'll give it a short,
descriptive message; save; and close the file.

```bash
Start of first-steps lesson
# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
#
# On branch main
#
# Initial commit
#
# Changes to be committed:
# new file:   LICENSE
# new file:   README
#
```

### Inspect History

To inspect previous commits, we can look at the history with `git log`. By
default, the log will contain the full commit hash of each commit, along with
the author, the date of commit, and the commit message file like the one we
just saved in the previous step.

We can simplify the output by listing only the first line of our commit
message. If we structure our commit messages thoughtfully, these messages will
tell us a high-level overview of the changes we made as our project evolved.

```bash
~/Computing-Essentials/first-steps $ git log --oneline
5c8de16 (HEAD -> main) Start of first-steps lesson
```

```{note}
Commit hashes are unique 40-character strings but are often distinct enough in
their first several characters for Git to differentiate between two commits by their
leading header. Expect different hash abbreviations than the value you see in
this example (`5c8de16`) and future examples.
```

### Make further changes

Now that our initial progress is saved as a commit, let's repopulate our lesson
directory and save the result of that step as a new commit.

If you still have the `make-first-steps.sh` file from the previous lesson, you
may run it again to populate the `first-steps` folder with dummy files.

```bash
~/Computing-Essentials/first-steps $ cd ..
~/Computing-Essentials $ sh make-first-steps.sh
```

Otherwise, download the script again and change permissions to be executable as
before.

```bash
~/Computing-Essentials/first-steps $ cd ..
~/Computing-Essentials $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/first-steps/make-first-steps.sh > make-first-steps.sh
~/Computing-Essentials $ chmod u+x make-first-steps.sh && sh make-first-steps.sh
```

Our `first-steps` folder should now be populated with dummy files. Let's
navigate back into the directory and view the status of Git.

```bash
~/Computing-Essentials $ cd first-steps
~/Computing-Essentials/first-steps $ git status
On branch main
Untracked files:
  (use "git add <file>..." to include what will be committed)
        010122_results.txt
        010222_results.txt
        ⋮
        summary.csv
```

Here, we see numerous untracked files that we want to put under version
control. Let's add them to the staging directory all at once and commit them
with a useful message.

```bash
~/Computing-Essentials/first-steps $ git add .
~/Computing-Essentials/first-steps $ git commit -m "Populate with dummy files"
```

Here, the `-m` flag is a shorthand way of writing the commit message without
having to open and save the commit message file in an editor.

If we inspect our git repository with the `git log` command, we'll see both
commits.

```bash
~/Computing-Essentials/first-steps $ git log --oneline
633ff6f (HEAD -> main) Populate with dummy files
5c8de16 Start of first-steps lesson
```

### Complete First Steps

We can now make changes to our directory structure with the assurance that we
can undo these changes if they are destructive.

Copy your `clean-data` script from the previous exercise to this folder.

```bash
~/Computing-Essentials/first-steps $ cp ../first-steps.bk/clean-data .
```

```{note}
The extra `.` at the end is shorthand for _this directory_. We are copying a
file from a directory located one level back from where we are `../` into where
we currently are `.`
```

If you do not have a working copy of your script, you can find an example
solution [here][solution].

[solution]: https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/first-steps/clean-data

```{hint}
Remember to `chmod u+x clean-data` if you copied the file from online.
```

Once copied, let's also commit this additional script as its own incremental
change to our project.

```bash
~/Computing-Essentials/first-steps $ git add clean-data
~/Computing-Essentials/first-steps $ git commit -m "Add script to reorganize files"
```

Execute our script to rename files and move them into their new folders.

```bash
~/Computing-Essentials/first-steps $ sh clean-data
```

See the changes we made.

```bash
~/Computing-Essentials/first-steps $ git status
On branch main
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    081121_high-temp_results.txt -> high-temp/2021-08-11_high-temp_result.txt
        ⋮
        renamed:    080121_results.txt -> room-temp/2021-08-01_room-temp_results.txt
        ⋮
```


Then save these changes with a commit.

```bash
~/Computing-Essentials/first-steps $ git add .
~/Computing-Essentials/first-steps $ git commit -m "Reorganize files"
[main 73bef22] Reorganize files
276 files changed, 0 insertions(+), 0 deletions(-)
⋮
```

The extra lines after the commit confirm for us what was included in the
commit. We see above that 276 files were renamed, but no lines of text were
inserted or deleted in any files.

### Undo a change

Suppose we had improperly renamed our files in our bash script, say, because our
regex matches were improperly formatted. We could delete our files and start
again from a backup point, but if that backup point is in a hard drive in
an office down the hall this becomes a minor annoyance, especially if we are
experimenting with our script iteration.

Git provides a way for us to undo to various degrees.

#### Undo a staged change

If you haven't committed your changes, all the edits you've made across your
repository can be unstaged. Unstaging a file means that the edits since its
last commit will be discarded. Edits include file deletions, renames, and
new line writes to files. Running `git restore --staged <file>...` will
revert the file back to the state of its last commit. Runnit `git restore
--staged .` will undo all changes, including restoring deleted files and
renaming them back to their original name.

#### Resetting to a previous commit

Suppose you don't realize your blunder until after you've already committed
your mistake. You can move back in history with `git reset`. Git will complain
if you have uncommitted changes in your staging directory before running a
reset. If you have changes you want to keep, you can stash them without
resorting to a proper commit, but for now let's assume you recently committed,
have your working directory clean, and immediately realized your mistake.

A reset can be `--soft`, `--mixed`, or `--hard`.

A __soft__ reset discards the last commit but keeps the files staged as they were
just before the commit. This is useful if you want to add something extra to
the previous commit by including an additional file or removing one specific
file from among many staged files. Files will not be changed or undone with
this approach.

```{tip}
If you only want to modify the previous commit message or make a simple change
to the previous commit, consider `git commit --amend`.
```

A __mixed__ reset is the default reset and keeps files as they were after you
edited them but before you added them to the staging directory. This preserves
the changes you made up to the commit you are checking out but lets you
restructure your staging directory from scratch. This is useful if you have
mostly good code but you need to tweak a file or series of files before staging
them again (this time with the new and improved edits).

A __hard__ reset goes one step further and discards all changes in that commit.
This is useful if you made breaking changes and want to get back to a working
state, defined as the state of affairs created by the previous commit as
measured from the one you are checking out.

```{warning}
After a hard reset, any uncommitted changes will be discarded. This means if
you have files that you keep uncommitted because you don't yet want them
tracked or because you are waiting to commit them in a logical order, they will
also be discarded when you run `git reset --hard <commit>`.
```

Think of a working session as the following timeline of events:

1. State of affairs from previous commit (working tree clean)
2. Make changes to files
3. Stage files
4. Commit

The results of steps 1--3 are stored in every commit with a commit hash. We can
access each step of a commit with a reset:

```bash
git reset --soft <commit> # Go to step 3 of specified commit
git reset --mixed <commit> # Go to step 2 of specified commit
git reset --hard <commit> # Go to step 1 of specified commit

git reset <commit> # Default settings, go to step 2 of specified commit
```

The `<commit>` hash can be found in the log and may be abbreviated to 7
characters.

If you want to move back a specified number of commits from the current HEAD,
you can replace the commit hash with `HEAD~N`.

#### Checkout a previous commit

If we want to inspect the state of our repository at a previous point but keep
our existing changes documented on our main branch, we can `git checkout`
previous files or commits. This is useful if you want to prepare your
filesystem for a new branch or feature and you want it to take effect from some
previous starting point.

From a filesystem point of view, `git checkout <commit>` is
identical to `git reset --hard <commit>` except that `git checkout` leaves alone the
branch you started from when you ran this command. A warning will inform you
that you are in a _detached head_ state, which means that this is only one part
of an intended two-part process. The second process is to commit the changes
you want to a new branch.

We will stay away from checking out entire commits, but we will see `git checkout`
again when we want to grab files from other branches or from earlier commits
when we don't want to undo everything along the way.

```{seealso}
[The difference between checkout and reset][checkout-reset]  
[The difference between reset --soft, --mixed, --hard][resets]

[resets]: https://stackoverflow.com/questions/3528245/whats-the-difference-between-git-reset-mixed-soft-and-hard
[checkout-reset]: https://stackoverflow.com/questions/3639342/whats-the-difference-between-git-reset-and-git-checkout
```

#### Example

Let's inspect our directory at this point in the lesson.

```bash
~/Computing-Essentials/first-steps $ git log --oneline
73bef22 (HEAD -> main) Reorganize files
6adfa40 Add script to reorganize files
633ff6f Populate with dummy files
5c8de16 Start of first-steps lesson
~/Computing-Essentials/first-steps $ ls
LICENSE      README       clean-data   high-temp/   room-temp/   summary.csv
```

We can see that our `high-temp/` and `room-temp/` directories exist and that
none of our original filenames are cluttering our main directory. Let's
assume that the files were renamed and sorted correctly.

We can also see from the log that our _Reorganize files_ step has already been
committed. Let's undo the results of our organization script `clean-data`.

**Question**: From the information provided above, what command can we run that would
completely revert our directory where the files exist but the filenames are not
renamed or sorted.

````{dropdown} Click to reveal
```bash
~/Computing-Essentials/first-steps $ git reset --hard HEAD~1
```

**Explanation**: Commit `6adfa40` already had a state of affairs where the
files were populated in the directory and the script was written but not yet
executed. We want to discard all changes that were made in the final commit
(`HEAD`), so we reset to Step 1 of commit `HEAD~1` (one commit prior).
````

#### Undoing a reset

What if you reset to a previous commit but realize you went back one commit too
far?

All is not lost. You can reset to a _forward_ position in the commit history
just the same as you can reset to a backward position. All you need is the
commit hash of where you want to advance.

Let's move back to our state of affairs before our reset. For clarity, we want
the files renamed and sorted back into their folders. We'll assume we are at
commit `6adfa40`, which is one commit behind our desired `73bef22`.

Much like `HEAD~N` was a shorthand for _go back N commits_, `HEAD@{N}` is
shorthand for _go ahead N commits_, so long as it exists and follows from the
current branch.

```bash
~/Computing-Essentials/first-steps $ git reset --hard HEAD@{1}
```

## Writing a scientific paper

In a related topic, we may use Git constructively to keep track of drafts of a
paper, so long as we agree to write it in a plain text format like $\LaTeX$ or
markdown. Let's walk through a typical workflow

We'll start by creating a new folder for our paper.

```bash
~/Computing-Essentials/first-steps $ cd ..
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




