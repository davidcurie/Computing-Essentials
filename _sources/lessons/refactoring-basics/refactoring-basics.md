# Refactoring Basics

```{admonition} Prerequisites
- Next Steps with Python
- [Exercism][exercism] Python track: [Classes](https://exercism.org/tracks/python/concepts/classes)

[exercism]: https://exercism.org/tracks/python/concepts
```

```{topic} Objectives
- Make use of tests to better prevent destructive edits in future revisions
```

We will reorganize our directory to better handle more scripts and data. We'll
further refine our `find_max.py` script to work with our new changes.

## Summary of Revisions

If you haven't made your own edits, an updated version of `find_max.py` as
expanded upon from the previous lesson can be found [here][find_max_revised].

[find_max_revised]: https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/next_steps/find_max_revised.py 

The example script provided above is outlined by the following core logic:

- Specify files to search
- Get all filenames into a list
- Group that list by some identifier (i.e. by month)
- Operate on that grouped list

A stripped-down version of the script looks like the following:

```python
# LOGIC FOR GATHERING FILES

def get_all_filenames(pattern):

def sort_filenames(list_of_filenames, key=project_YYYYMM):

# LOGIC FOR MANAGING DATA

def import_files_into_dataframe(parsed_list):

def get_max_values(list_of_dataframes):

# INTENDED SEQUENCE OF OPERATIONS

files_to_search = '*/*'
files_as_list = get_all_filenames(files_to_search)
grouped_files = sort_filenames(files_as_list)
df_list = import_files_into_dataframe(grouped_files)
df_max_vals = get_max_values(df_list)
with open('summary.csv', 'w') as outfile:
    df_max_vals.to_csv(outfile, header=None)
```

These logic of these core functions is made extensible by other helper
functions.

```python
def _get_date_from(filename):
    """Return (YYYY, MM, DD) from filename string"""
    # Assumes filename: YYYY-MM-DD_other_text
    YYYYMMDD = os.path.basename(filename).split('_')[0]
    YYYY, MM, DD = YYYYMMDD.split('-')
    return YYYY, MM, DD

def _project_YYYY(filename):
    """Return YYYY from filename string"""
    return int(_get_date_from(filename)[0])

def _project_YYYYMM(filename):
    """Return YYYY-MM string from filename string"""
    return '-'.join(_get_date_from(filename)[0:2])

def _project_YYYYMMDD(filename):
    """ Return YYYY-MM-DD string from filename string"""
    return '-'.join(_get_date_from(filename))

def _import_data(file):
    return pd.read_csv(file, delimiter='\t', header=None)
```

Notice that these helper functions are named with a leading underscore. This is
a convention to tell other programmers that these are meant to be called by
other functions in our script but not to be called directly by the end-user.

The purpose of the helper functions in this example is to make the core
functions easier to read.

In the updated script, the `sort_filenames()` function makes use of a
`group_by()` function in the `itertools` library, which is part of the standard
Python library. This saves us from having to define our own grouping mechanism,
but we need to start with a sorted list and specify how to group that list.
Rather than hard-coding the sorting criteria logic directly inside the
`sort_filenames()` function, we can define a sorting key (sometimes also called
a _list projection_) that handles the logic.

The list projections used here are functions that return some sortable value
from a filename. A sortable value is either a number or a string, where strings
are sorted in alphanumeric order (0--9A--Za--z). In our case, we assume that the
string `YYYY-MM-DD` appears in the beginning of the filename. We then find a way to
return some subset of that string. If we want to sort or group by `YYYY`, we
find a way to return just these characters. Since our initial task is to group
by month, we want to `YYYY-MM` string from the filename. The year is included
to avoid grouping months from different years together.

Updating the sorting algorithm is then as simple as updating the sorting key in
the `group_by()` function. We don't want to have to edit the guts of the
`sort_filenames()` function each time we want to update the logic used by
`group_by()` function inside, so we pass in a parameter to `sort_filenames()`
and let `group_by()` access the contents of that parameter.

```python
def sort_filenames(filenames, key=MyValue):
    # group_by logic that makes use of the value of `key`
```

This indicates that the default sorting key is `MyValue` unless otherwise
specified at runtime. Running `sort_filenames(filenames)` would automatically
make use of `MyValue`, but if you wanted to change this at runtime, you could
invoke `sort_filenames(filenames, key=MyOtherValue)`.

Having adjustable parameters grouped into the function call makes it much
easier to make future edits without having to investigate the
sometimes-complicated logic buried in functions.

```{tip}
Aim to generalize functions by allowing variables that you foresee will change
in specific cases to be encapsulated as an optional function parameter. Give
default parameter values to control the assumed behavior of the function.
```

## More Refactoring

We've made our script easier to inspect in the future by outsourcing the key logic
into functions, but we haven't made our project easier to inspect as a whole.

### Cleaning the Directory

If you've been following along with the lessons so far, your `first-steps/`
directory might look something like the following:

```bash
first-steps/
    ├──high-temp/
    ├──room-temp/
    └──LICENSE
    └──README
    └──clean-data
    └──environment.yml
    └──find_max.py
    └──summary.csv
    └──to-clean.txt
```

Suppose we want to divide our project into a `data/` `results/` and `scripts/`
folder. These changes might break the way some of our scripts access files, so
we'll commit our directory structure to log our housecleaning in Git.

```bash
(first-steps) ~/Computing-Essentials/first-steps $ git add . && git commit -m "Start of housecleaning"
```

Create these folders and move files until you get a directory structure like
the following:

```bash
first-steps/
    ├──data/
        └──high-temp/
        └──room-temp/
        └──to-clean.txt
    ├──results/
        └──summary.csv
    ├──scripts/
        └──clean-data
        └──find_max.py
    └──LICENSE
    └──README
    └──environment.yml
```

The `clean-data` and `find_max.py` files need to be edited in the way they
search for data. When looking for all data files, we previously used a wildcard
search `*/*` meaning _all directories_/_all files_ **relative to the working
directory of where this script is executed**. Relative to the new location of
the script, that path looks something like `../data/*/*`.

```{topic} Task
Update the search criteria for `clean-data` and `find_max.py` so that they may
be run from the `scripts/` directory. Check that these produce the expected
results, say, for `find_max.py` and that the results are written to their new
location.
```

```{topic} Task
Log the changes corresponding to the newly organized directory and the modified
script files in Git as a commit with a message such as "Reorganize directory
into folders"
```

### Using Tests

The file given at the beginning of the lesson is a functioning copy of a
script that meets the current objectives. Sometimes the objectives of our
script evolve in ways that aren't obvious to predict when first defining
functions.

Unit tests allow for us to make iterative changes to our code while we
restructure its logic and check to see that it still meets the core
requirements that we set out with.

```{seealso}
For a more lucid discussion on why unit tests are important and how to
implement them, see <https://goodresearch.dev/testing.html>.
```

It's good practice to have a set of tests for each script. We'll make a
separate `tests/` folder to house each test, and name our tests after the
script they are meant to inspect.

```{topic} Task
A set of tests for the file linked at the beginning of the lesson can be found
in [this directory][find_max_test]. Make your own `tests/` folder and copy the
contents of the example directory into your `tests/` folder.

[find_max_test]:
https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/refactoring-basics/tests/
```

The tests may be run from the main project directory with the following line:

```bash
(first-steps) ~/Computing-Essentials/first-steps $ python -m pytest tests/find_max_test.py
```

```{topic} Task
Check to make sure that all of the tests pass. Then commit the contents of the
`tests/` folder to your repository.
```

Notice that in the `find_max_test.py` file, each function starts with the word
_test_ and describes the performed test. This makes it easier to inspect which
tests failed.

The tests are only as valuable as the insight you have when designing the
tests. Often when refactoring, you'll make errors that cause tests to fail.
Make note of those errors and design a test to catch that error in the future.

Here are two test suggestions that might motivate further changes to our
`find_max.py` script.

```{topic} Task
Write a unit test that checks whether `sort_filenames()` continutes to sort by
month when there are spaces in the filenames. Then implement changes to
`sort_filenames()` so that filenames with spaces don't break the workflow.
```

```{topic} Task
Write a unit test that checks whether `sort_filenames()` continutes to sort by
month when the YYYY-MM-DD substring is not the first part of the filename. Then
implement changes to `sort_filenames()` so that filenames with spaces don't
break the workflow.
```

```{topic} Challenge
:class: important
Rewrite the modified `find_max.py` script given in this lesson to use
_Classes_.
```

