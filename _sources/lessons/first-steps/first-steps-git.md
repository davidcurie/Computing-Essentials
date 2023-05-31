# First Steps with Git

```{admonition} Prerequisites
- First Steps with Bash
```

```{topic} Objectives
- Document a project
```

## First Steps extension

The _First Steps with Bash_ lesson had you move files in your filesystem in some
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

### Inspect history

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
renamed or sorted?

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

````{note}
If you are satisfied with the state of your `first-steps` folder at this point,
you can safely delete the backup of the directory we made at the beginning of
this lesson.
```bash
~/Computing-Essentials $ rm -rf first-steps.bk
```
````

## Concluding remarks

The workflow above represents one of many uses for Git. Future lessons in this series will make use of Git to establish a safe point in our iteration cycles, as later lessons will overwrite working code from beginner lessons.

In a related topic, we may use Git constructively to keep track of drafts of a
paper, so long as we agree to write it in a plain text format like $\LaTeX$ or
markdown. The next lesson discusses this in more detail.


### Git advice

Consider these final bits of advice as you develop your Git habits in this series:

- Keep commits logically structured. One collective change = one commit.
- Keep commit messages short and informative.
- Use imperative verb form in commits (`Fix bug #123`, not `Fixes bug #123` nor `Fixed bug #123`).
- Consistency is key.

Remember that your commit messages should tell a story of your progress over
time. You may decide on what an appropriate unit of change is for yourself. If
your messages are uninformative to you, the benefits of version control will be
largely underutilized. The extra time spent in crafting useful and purposeful
changes as you work will pay off when you need to change research directions or
bring other collaborators into the mix.

```{seealso}
- [Writing a Good Commit Message][git-commit-message]
- [Git Tutorial for Absolute Beginners from Zero to Hero][git-zero-to-hero] (video playlist: 16 videos)

[git-commit-message]: https://www.gitkraken.com/learn/git/best-practices/git-commit-message
[git-zero-to-hero]: https://www.youtube.com/watch?v=sH4fr8eQHaE&list=PLJGDHERh23x_4MDp0m4Arswm5VErr3tbl
```

