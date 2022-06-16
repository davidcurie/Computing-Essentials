# First Steps with Bash

```{admonition} Prerequisites
- Bash terminal installed on your machine
```

```{topic} Objectives
- Become familiar with terminal execution.
- Learn regular expression syntax.
```

## Terminal

Using a terminal doesn't need to be a daunting experience. Even with minimal
exposure and a basic comprehension of core concepts, we can understand simple
one-line commands enough to save us hours of tedious file management.

Our goal in this lesson is not to be fluent enough to have a conversation with
our computer, but to learn the basic vocabulary enough to ask for directions.

The most common file system management tools we will need in the terminal is
for bulk transport of files and for pattern matching.

The basic syntax for commands is `cmd -<options> <arguments>`. Options are
also sometimes called _flags_ and alter the default behavior of a command. You
can set default options for basic commands on your machine by creating an
_alias_ of the command and storing that alias in a runtime configuration for
bash known as `.bashrc`.

```sh
#.bashrc
alias ls='ls -FGh'  # set default flags for ls command
```

### File management

#### ls and cd

View the contents of your current working directory with `ls`.

```bash
~ $ ls
```

To view hidden files, pass the `-a` flag to view _all_ files. Hidden files
normally begin with a `.` and are not usually displayed in GUI system file
managers. This is a developer's way of protecting end-users from accidentally
deleting important stuff. We will encounter some hidden files with `git` when
we create local repositories.

#### mv and cp

Moving and copying files follow a simple format.

```bash
~ $ mv path/to/original/file.txt path/to/new/file.txt
```

```bash
~ $ cp path/to/original/file.txt path/to/copied/file.txt
```

For a move command, the original file is deleted from its original location, so
be mindful that if you mistype the output directory, you may have trouble
finding your file. Neither of these commands gives feedback when they run
successfully, but they do throw an error when you attempt to move to a location
that doesn't already exist.

```{tip}
Most terminals have a history feature where you can view the last commands
entered on the terminal without having to scroll all the way up in your
terminal screen. These are commonly accessed by pressing the <kbd>up</kbd> and
<kbd>down</kbd> arrows on your keyboard.
```

You can enter interactive mode in either of these commands by passing the `-i`
flag. This will prompt you to confirm before any potentially dangerous overwrites.

```bash
~ $ mv -i original.txt new/directory/original.txt
```

#### mkdir

If a directory doesn't yet exist, create it with `mkdir`

```bash
~ $ mkdir -p a/series/of/new/nested/directories/
```

Here, the `-p` flag generates all of the parent directories in the specified
path if they do not already exist. We can also generate multiple directories at
once with parameter expansion shortcuts.

```bash
~ $ mkdir -p directory{A,B,10}
```

The above command generates `directoryA`, `directoryB`, and `directory10` by
supplying each of the values in `{}` to the rest of the string. We can specify
ranges by `{1..10}` and even compound iterations with `{{A..Z}{0..3}}`. The
latter expression will expand to `A1`, `A2`, `A3`, `B1`, `B2`, ..., `Z1`, `Z2`,
`Z3`.

#### rm

Remove files with `rm`, enter interactive mode with `-i`, and delete
recursively all files in a directory with `-r`.

```bash
~ $ rm -ri directory* 
```

Here, the `*` is a wildcard expansion for all characters after the pattern
directory. This will match all directories that start with the pattern
`directory`. The `-r` flag will delete all files inside a directory, but to
delete the directory itself, pass the `-d` flag.

```bash
~ $ rm -d directory*
```

### Find and Replace

The tool we will demonstrate in this lesson is `sed` (short for _streamline
editor_), but other useful tools are `awk` and `perl`.

The basic syntax for `sed` is as follows:

```bash
sed -options 's/find/replace/' input_file
```

Here, `find` and `replace` are placeholders for regular expressions used to
match your desired text; the contents of the first `find` are replaced with
`replace`. `sed` also accepts piped input, so we can test simple strings with
`sed` to learn its behavior.

What do you think the result of the following command will be?

```bash
~ $ echo "the cat in the hat" | sed 's/a/u/'
```
````{dropdown} *Click to reveal*
```bash
the cut in the hat
```
````

If the above answer surprises you, remember that `sed` only finds the first
occurrence of a match and then moves on. If you want it to apply to all
_global_ occurrences, include the extra flag as `sed 's/find/replace/g'`.

By default, the result is directed to STDOUT, but we can reroute this to a
file with `>` (overwrite) or `>>` (append).

```bash
~ $ cat input.txt | sed 's/find/replace/' >> output.txt
```

### Regular Expressions

We can match more complicated patterns. Some examples:

| Example    | Meaning                                                   |
|------------|-----------------------------------------------------------|
| `^c`       | only occurrences of _c_ that begin a newline              |
| `txt$`     | the exact sequence _txt_ that occurs at the end of a line |
| `[aeiou]`  | any single character in the list _a, e, i, o, u_          |
| `[^aeiou]` | any single character except _a, e, i, o, u_               |
| `a?`       | zero or one of _a_                                        |
| `a+`       | one or more or _a_                                        |
| `a{3}`     | exactly 3 of _a_                                          |
| `a{3,}     | 3 or more of _a_                                          |
| `.`        | any character                                             |

Under extended regex syntax (`-E` flag), you may also use capturing groups by
enclosing your desired matching expression in `()`. This allows you to
rearrange groups of matches in your `replace` syntax by referencing the
matching groups.

```{seealso}
[Regex101](https://www.regex101.com): helpful interactive construction syntax
```

### Example

Look closely at the following example:

```bash
~ $ echo "Smith, John" | sed -E 's/(^.*), (.*$)/\2 \1/' 
```

We are exploiting the format of `Last, First` to group together a syntax that
looks for `chars` + `,` + ` ` + `chars`. The first matching group is defined as
`^.*` (all characters from the start of the string), but only as it exists up
to the next search criteria, which is a comma. We then explicitly include in
our search the space after the comma and define another matching group `.*$`
(all characters until end of string).

Our `replace` expression is `\2 \1`, meaning _display the second matching group in
my previous expression, then a space, then the first matching group_. The result
of this command is `John Smith`

If we want to write changes directly to our input file, we can operate _inline_
with the `-i` flag and specify an extension for a backup file.

```bash
# Search and replace input.txt, create input.txt.bk, overwrite original
~ $ sed -i '.bk' 's/find/replace/' input.txt
```

```bash
# Search and replace input.txt, no backup, overwrite original
~ $ sed -i '' 's/find/replace/' input.txt
```

## Instructions

Navigate to `~/Computing-Essentials` in a terminal and execute the following commands:

```bash
~/Computing-Essentials $ curl https://raw.githubusercontent.com/davidcurie/Computing-Essentials/main/lessons/first-steps/make-first-steps.sh > make-first-steps.sh
~/Computing-Essentials $ chmod u+x make-first-steps.sh && ./make-first-steps.sh
```

The above commands download and execute a script that will create and populate
a folder for this lesson.

```{caution}
Be mindful about blindly executing scripts you find online. Inspect any files
you download with a text editor before executing from sources you don't trust.
```

The new folder has many data files simulating measurements taken over many
months. Each measurement is a simple spectrum represented by a series of
(`wavelength    intensity`) pairs.

Move to the newly created folder and view the contents with `ls`:

```bash
~/Computing-Essentials $ cd first-steps
~/Computing-Essentials/first-steps $ ls
```

### Rename files

These files were named by your colleague without careful consideration and
subsequently lumped into one directory. One immediately obvious problem we face
is that the files do not sort naturally by date. Renaming these dates by hand
would be tedious, but we can solve this problem with some regular expression
matching.


```{topic} Task
Change all dates in the filenames from MMDDYY to YYYYMMDD.
```

### Organize files

We may also notice that some of the data files have special acquisition
parameter circumstances that make them distinct from other files. Consider it
good practice to have identifying remarks in the filename; aim to keep the
level of remarks from most-to-least general going from left-to-right in the
filename. We may anticipate an analysis that makes use of data acquired with
similar parameters.

To make it easier for us to find this data when we need it, let's restructure
the directory to move similarly acquired data into an identifiable folder for
easier browsing.

We'll also keep the verbose filenames as a measure of
redundancy even though the information will now be duplicated in the folder
structure. Let's also agree on a naming slug so that all files have a
similarly-patterned name for any further pattern matching we may do in the
future.

```{topic} Task
- Move data into low-temperature and high-temperature folders.
- Include low-temp descriptor in regular filenames for extra clarity.
```

### Identify special files

Maintenance makes routine cleaning stops around the lab to pick up waste. When
someone comes in to collect waste, the stray light from the hallway causes the
counts in the detector to increase slightly. Normally, these operations happen
at night when nobody is collecting data, but you remember that some of the
acquisitions were running overnight. Unfortunately, the timestamps of these
acquisitions were lost when you pulled this data from a backup drive, as the
file timestamps now reflect when you last imported them from the archive.

This is not a problem. You know you can look for patterns in your files to
detect values greater than some threshold. You know for certain that during the
month of March you did not have any overnight runs, so you can look for typical
spectrometer values for all runs in this date range.

For now, let's assume you already figured out that the maximum signal you were
getting did not go above 356 counts in this time. Use this as a discriminator
to find the data, and thus the night(s), that you were collecting data when
someone entered the room.

You may use the `grep` command to find the file. The general syntax is

```bash
~ $ grep -l 'pattern' file1 file2 ...
```


```{topic} Task
Find files that have above-average spikes in their spectra.
```

### Write a script

You decide that you don't want to learn these commands every six months when
you get a large enough dataset to have to sit down and clean. You can assemble
the commands into a plain text file and make them executable from the shell by
invoking the filename. Typical filenames usually end in `.sh` for bash
execution, but the extension may be left off entirely if you follow the steps
below.

Create and edit a file called `clean-data`. At the top of the file, insert a
_shebang_ that tells the terminal what program you will eventually want to
handle the execution of this file. For now, this will be `bash`. We do this
with the following:

```bash
#! /bin/bash
# Author: Your name
# Description: Simple sentence of what this file will do

# Insert terminal commands here
```

The _Author_ and _Description_ notes are not strictly necessary, but if you
plan to share this with your colleagues, you may want credit for your insight
(or blame for your lack of insight). It is good practice to briefly mention the
objectives of the script for the benefit of those who may expand on your script
next, including you six months from now.

After you copy your commands and save your file, you'll need to tell your
machine that this file is executable. Do so with the following command.

```bash
~/Computing-Essentials/first-steps $ chmod u+x clean-data
```

The `chmod` command changes modifications so that the current user `u` has an
additional execution permission `+x` on the following file. You can tell if
this was done properly by inspecting the file with `ls -l` from the current
directory.

You should see ten flags to the left of the filename, along with other file
data. The left-most flag is either `-` or `d` to indicate a _file_ or
_directory_. The next nine flags are _read_, _write_, and _execute_
permissions for user, group, and other, respectively. Note that _user_ refers
to the currently logged-in user on the machine.

If the above command was executed properly, you should see `-rwx` as the first
four flags of `clean-data`. From here, you can invoke the file from the
terminal at the same working directory as you completed these exercises.

```bash
~/Computing-Essentials/first-steps $ sh clean-data
```

```{topic} Task
Write a simple script to complete the above tasks in one step.
```

```{admonition} Challenge
:class: important
Allow for the script to accept an argument from the command line to represent
the directory for which the organization should take place. This would allow
you to exclude files that you already organized.

Example usage: `sh clean-data unsorted/*.txt`

Intended result: only rename and move .txt files that exist in an unsorted
directory
```
