# Git for Academic Papers

```{admonition} Prerequisites
- [Git-It](https://github.com/jlord/git-it-electron) tutorial
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
Furthermore, scientific papers are often written in $\LaTeX$, where native
_Track Changes_ features are not available.

Online collaborative $\LaTeX$ software exists at
[Overleaf](https://overleaf.com) (formerly ShareLatex), but this is an online
Git repository at heart. This service can be approximated for free with a
proper understanding of Git.

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

## Collaborating with other authors

Sending an occasional diff file is fine for when you want to present a before
and after view of your edits, but there are other flavors of updates you can
share when you involve an entire repository. 

For instance, you can grant others read-only access to your repository for them
to inspect the diff files on their own. This allows them to pick through which
changes they may want to compare.

You might also consider something similar if you want to publish the live
version of your draft at some website. This project uses the above workflow to
publish this book, written in markdown, as html.

You can also grant other people read-write access to your repository if you
want to invite changes and near real-time collaboration. This case deserves
special attention to avoid potential pitfalls.

### Host your files online

The first step in either process above is to host your repository on a server.
This can be a local server hosted in your research lab, accessible via local
intranet access, or a cloud-based server hosted by a commercial company. We'll
use GitHub for this lesson because its free for features we'll use, but other
comparable servers are GitLab and Bitbucket.

If you've completed the recommended [Git-It][git-it] tutorial, you will already
have created a GitHub account.

[git-it]: http://jlord.us/git-it

```{seealso}
[Creating a new repository on GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)
```

Even though we've created a local Git repository for our folder with the `git
init` command, we'll need to recreate a repository in GitHub and link our
existing repository to the newly-created online repository.

Follow the steps to create a repository from the GitHub documentation. By the
end, you will have a URL that points to your online repository. It will look
something like `https://github.com/UserName/RepoName.git`.

Link your local `git-paper` folder to your online repo in the following manner.

```bash
git remote add REMOTENAME URL
```

You may replace `REMOTENAME` with any name you choose to help you differentiate
where you are pushing. Repeating this step allows you to set multiple remotes
so that you can push one local Git folder to separate places by name. Most GitHub
documentation calls this remote `origin` and assumes you don't have multiple
online repos to worry about.

```bash
~/Computing-Essentials/git-paper $ git remote add origin URL
```

Replace `URL` with your Git repo. Then update the contents of the online repo
with your existing commits. The command line syntax is as follows.

```bash
git push REMOTENAME BRANCHNAME
```

Here `BRANCHNAME` is the name of the local branch you want to push. By default,
newly initialized Git repos are given a name of `main`, but if you have a repo
from before 2020 or you clone an older repo, it may be called `master`.

```{note}
When you first installed Git, you may have had the option of selecting a
default name for newly created projects. The default branch used to be
`master`, but was renamed to `main` in October 2020. If you browse
StackExchange posts from before 2020, remember to mentally replace `master`
with `main` or whatever your branch name is.
```

You can view your branch names with the command `git branch -a`. The branch you
are currently operating on is marked with an asterisk (\*).

Assuming your branch is named `main`, update your changes to your online
repository.

```bash
~/Computing-Essentials/git-paper $ git push origin main
```

Navigate to your repo URL to see your changes. You can now share this URL with
your collaborators for them to view your draft. Anyone with this URL has
read-access to this repository, meaning they can download a local copy of your
commits and see diffs on their own.

### Managing multiple authors

If you want users to be able to make edits to the online copy, you'll need to
grant them permission in GitHub.

```{seealso}
[Inviting collaborators to a personal
repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
```

When two or more users are making changes to an online repository, it is
possible for pushed changes to get out of sync. Git and GitHub will warn you if
there are conflicting updates to be applied in a commit (known as a _Merge
conflict_). This happens when someone is working on an outdated copy of an
online file.

We can resynchronize our local copies with the online version with a _pull_
command.

```bash
$ git pull origin main
```

This command does two things: it _fetches_ any updates from the origin (online)
branch and _merges_ them into the main (local) branch. If there are no
conflicts, changes will be automatically applied and your _HEAD_ pointer will
be up-to-date with the online version. If there are conflicts, you may be asked
to pick which of the two versions you want to keep, depending on your editor.

You can instead pick and choose parts of each version by manually editing the
conflicting files. The file in question will have both changes applied inside
special formatting:

```text
Some existing lines of text.

<<<<<<< HEAD
Some old text in your local copy.
=======
New text that conflicts with the part above.
<<<<<<< REMOTENAME

Some more existing lines of text that are unaffected.
```

If your editor does not help you resolve this, select the parts of the text
you'd like to keep by removing the unnecessary parts, along with the extra
formatting.

When you are pleased with your edits, you'll need to tell Git that
you are done resolving conflicts on that file. This is done with a `git add
<filename>` command.

When all of your conflicted files are staged, save them
with `git commit`. Pick a useful message that tells you which versions you've
incorporated in your changes; this will be visible to all future collaborators
who pull from your repo once you next push your changes. You can be more
detailed in the comments of your commit by writing these details on newlines in
your commit message.

```{seealso}
- [Atlassian: Syncing][atlassian-syncing]
- [Atlassian: Merge Conflicts][atlassian-merge-conflicts]

[atlassian-syncing]: https://www.atlassian.com/git/tutorials/syncing
[atlassian-merge-conflicts]: https://www.atlassian.com/git/tutorials/using-branches/merge-conflicts
```

### Workflow

<mark>Many problems in the collaborating pipeline can be avoided if you make a
habit of pulling before you push.</mark> This doesn't guarantee that you won't
have merge conflicts, but it allows you to resolve those conflicts locally
before you update them to the remote branch, meaning the work you did to
resolve the conflict will now be stored in the commit tree for others to
benefit from.

0. Pull any updates from online
1. State of affairs from previous commit (working tree clean)
2. Make changes to files
3. Stage files
4. Commit
5. Pull any updates since you've been editing
    - Resolve conflicts if necessary
6. Push changes for others to see

Notice that a `pull` command is recommended both before you start editing (so
that you are starting from an up-to-date version) and before you publish (in
case others have incorporated the same changes you were working on).
