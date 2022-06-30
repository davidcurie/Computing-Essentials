# Next Steps with Python

```{admonition} Prerequisites
- First Steps with Python
```

```{admonition} Optional Prerequisites
- [Exercism][exercism] Python track: [Tree building](https://exercism.org/tracks/python/exercises/tree-building)

[exercism]: https://exercism.org/tracks/python/concepts
```

```{topic} Objectives
- Develop scalable approaches to analyzing data
```

We will take an example script that solves the _First Steps with Python_
exercise and improve upon it in a way that outsources the repeated steps into
functions.

## A sample solution

As a reminder of our task, we were asked to search through our sorted data and
find the maximum value for our spectrometer counts per month. The following
script does that. You may find a copy of this initial script [here][solution].

[solution]: https://github.com/davidcurie/Computing-Essentials/blob/main/lessons/first-steps/find_max.py

```python
import pandas as pd
from glob import glob

MONTHS = {1: "January",
          2: "Februrary",
          3: "March",
          4: "April",
          5: "May",
          6: "June",
          7: "July",
          8: "August",
          9: "September",
         10: "October",
         11: "November",
         12: "December"
         }

# Search through months by int, name pair in 2021.
for month, name in MONTHS.items():
    MM = f'{month:02}' # pad with leading zero
    filenames = glob(f'*/2021-{MM}-*') # get all files in this month
    data_as_list = []
    for file in filenames:
        month_entry = pd.read_csv(file, delimiter='\t', header=None)
        data_as_list.append(month_entry[1])
    try:
        month_df = pd.concat(data_as_list, axis=0, ignore_index=True)
    except ValueError:
        month_df = pd.DataFrame()
    with open('summary.csv', 'a') as outfile:
        outfile.write(f'2021 {name}, {month_df.values.max()}\n')

# Search through months by int, name pair in 2022.
for month, name in MONTHS.items():
    MM = f'{month:02}' # pad with leading zero
    filenames = glob(f'*/2022-{MM}-*') # get all files in this month
    data_as_list = []
    for file in filenames:
        month_entry = pd.read_csv(file, delimiter='\t', header=None)
        data_as_list.append(month_entry[1])
    try:
        month_df = pd.concat(data_as_list, axis=0, ignore_index=True)
    except ValueError:
        month_df = pd.DataFrame()
    with open('summary.csv', 'a') as outfile:
        outfile.write(f'2022 {name}, {month_df.values.max()}\n')
```

The basic premise of the script is as follows:

1. Create a dictionary to search by individual months by number and name
   simultaneously.
2. For each month, find files with identifiable matching criteria in the year 2021.
    
    ```python
    for month, name in MONTHS.items():
        MM = f'{month:02}' # pad with leading zero
        filenames = glob(f'*/2021-{MM}-*') # get all files in this month, 2021
    ```

   The `MM = f'{month:02}` syntax takes our dictionary index, say `1` and
   converts it to the string `01`. This allows us to match substrings that have a
   date in YYYY-MM-DD format, as we constructed in our earlier _First Steps with
   Bash_ lesson.

3. Read matching filenames and append the _counts_ column to a list.

    ```python
        for file in filenames:
            month_entry = pd.read_csv(file, delimiter='\t', header=None)
            data_as_list.append(month_entry[1])
    ```

4. Concatenate existing list to a dataframe.

    ```python
        try:
            month_df = pd.concat(data_as_list, axis=0, ignore_index=True)
        except ValueError:
            month_df = pd.DataFrame()
    ```

   In the case where the _try_ statement fails due to an empty input list (say,
   because there are no filenames with the matching month), a `ValueError` is
   raised. We can handle that error case explicitly by writing an empty
   dataframe instead. If the _try_ statement fails for other reasons not
   explicitly mentioned by an _except_ statement, the error is relayed as
   normal. We write to an empty dataframe object so that we can use other
   _dataframe_ functions in the future without raising more errors.

5. Write the maximum value from the dataframe to a file.

    ```python
        with open('summary.csv', 'a') as outfile:
            outfile.write(f'2022 {name}, {month_df.values.max()}\n')
    ```

   The `with open()` syntax takes care of properly opening and closing the file
   in memory after the commands of the indented section below. Here, we are
   opening the file in _append_ mode `'a'`, and explicitly including a
   _newline_ character `\n` in each line write. We can't open the file in
   _write_ mode `'w'` because we would overwrite the monthly maximum on each
   successive loop. The contents of the line write are formatted in
   _f-strings_, which is a python 3.6+ feature. Words inside `{}` are expanded
   to their variable representation. We use the `max()` function on our
   `month_df` dataframe of counts accumulated for that month. We also convert
   the dataframe to its numeric value representation before computing the
   maximum value so that empty dataframes don't display as an object instead of
   _Not a Number_ `nan`.

6. Repeat for months in 2022.

## Identify repeated sections

Note that in the first draft of this script above, the code that handles the
month-by-month logic is largely identical for each year, except for the
explicit inclusion of the year in following two lines:

```python
filenames = glob(f'*/2021-{MM}-*') # get all files in this month
outfile.write(f'2021 {name}, {month_df.values.max()}\n')
```

We could group these two functions into a parent loop and iterate over each
year.

```python
# Insert code here
```

This is better because if we make changes to the logic of one month-by-month
iteration, we don't need to worry about duplicating that change in another
block of code.

The downside of this approach is that we haven't reduced operational
complexity. We now have at least 3 nested _for_ loops, while good practice aims
for no more than 2 nested loops. This rule stems from the belief that if you
are nesting loops to handle a flow-chart of cases, you are better of
redesigning your logic.

Consider the following alternative logic:

1. Get all filenames (all months, all years)
2. Sort filenames by YYYY-MM, group into sub-lists
3. Gather data for all files in a sub-list; concatenate into one dataframe
4. Pick out the max value for each criteria in the larger dataframe
5. Write these values to `summary.csv` in one step

Notice how we can loosely group this into sections that deal with gathering
files (steps 1--2), managing data (steps 3--4), and writing results (step
5).

More importantly, with enough insight we can structure these calls to be
relatively independent from one another.

### Gathering Files

Rather than explicitly searching through all files within each _month loop_ to
find only those files with a matching month integer `MM`, we can search through
all files once at the beginning of our script and store the results in a list
that we can later parse. The advantage of this is that we only run `glob()`
once, which is a system wide search through directories. We then access
specific filenames by searching through an internal Python list, which may give
us a slight computing advantage.

Let's make these calls dedicated functions.

```python
def get_all_filenames(pattern):
    all_filenames_as_list = glob(pattern)
    return all_filenames_as_list

def sort_filenames(list_of_filenames):
    pass
```

Our first function is just a one-to-one wrapper of the `glob()` function, but
having it in a dedicated function of our choosing makes it clear to us when we
call it that we are accessing all files that we wish to parse. It also allows
us to modify the logic in case we want to add flags in the future without
having to search for all cases in our script where we used the native `glob()`
functionality by itself.

The `pass` statement in the second function is a temporary placeholder that
says _do nothing_ and allows us to benchmark functions that we should come back
to.

Our `sort_filesnames()` function should take our list of filenames and
parse it into sub-lists of our choosing. This can be achieved in a couple of
ways.

1. Store this parsed list as a single object that we can pass to other
   functions and have those functions pick out the relevant parts that they need.

    ```python
    # Approach 1
    def sort_filenames(list_of_filenames):
        # Sort logic here based on some predefined pattern
        return [[sublist_1], [sublist_2], ..., [sublist_N]]
    ```

   We can then store this list of lists as an object, say `parsed_list`, and
   access each month through list indexing, as in `parsed_list[0]` to get the
   first matching month.

2. Parse the entire list of filenames on demand, only returning the specified
   match based on user input.

    ```python
    # Approach 2
    def sort_filenames(list_of_filenames, sublist_pattern):
        # Sort logic here that depends on sublist_pattern
        return sublist_match
    ```

   This approach allows for us to generalize our search criteria by specifying
   `sublist_pattern` as an extra function parameter. We might also rename the
   function to be more explicit about what it does.

    ```python
    # Approach 2
    def get_sublist_from_pattern(list_of_filenames, sublist_pattern):
        # Sort logic here that depends on sublist_pattern
        return sublist_match
    ```

If we intend to access the entire list of filenames infrequently, approach 2
might be the way to go from a resource perspective. It also is more general
because it allows for tweaking the search criteria by using a second input
parameter.

Recall that the purpose of our parsing is to be able to loop through different
months and read a select number of files. Approach 2 forces us to use this
function inside of a loop, where we may have previously defined the search
criteria. It might look like this:

```python
# Looping with approach 2
for month in list_of_months:
    sublist_pattern = some_criteria
    files_by_month = get_sublist_from_pattern(list_of_filenames, sublist_pattern)
    # Read data from matched files and continue for loop logic
```

Here, `some_criteria` would need to be defined for each loop (preferably by
another function). Additionally, we have to set up some iterable for us to loop
over before we can filter the filenames by month. This means that although
approach 2 is extensible, it requires us to create a `list_of_months` to
iterate over and `some_criteria` for us to tailor the generalized function to
our desired loop case. This means that if we later decide to group our searches
by academic semester instead of by month, we'll need to remember to update how
we generate our `list_of_months` iterable and our `some_criteria` call.

Approach 1 returns an iterable object that is intimately tied to our search
criteria, meaning that we don't need to set up any further lists to loop
through, so long as we took the time to carefully construct the subsets that we
want.

```python
# Looping with approach 1
parsed_list = sort_filenames(list_of_filenames)
for files_by_month in parsed_list:
    # Read data from each list of files_by_month
    # Continue for loop logic
```

From an extensibility standpoint, approach 1 is slightly better because it
takes care of all of the pattern matching during the sorting processes, whereas
approach 2 requires us to generate a sorting criteria on each loop and then
apply that sorting criteria to the parent list of filenames on each loop.

|           | Approach 1                       | Approach 2                                               |
|-----------|----------------------------------|----------------------------------------------------------|
| Objective | Sort once, access later          | Sort on demand                                           |
| Pros      | Ties search criteria to iterable | Extensible for matching other search patterns            |
| Cons      | Not extensible                   | Adjustments to search pattern require changes in 2 spots |

We'll adopt the generalizability of approach 2 into approach 1 by coding in our
matching criterion in approach 1 as a callable function.

```python
# Improved approach 1
def search_criteria(pattern)
    pass

def sort_filenames(list_of_filenames, sublist_pattern):
    # Use search_criteria(sublist_pattern) logic to parse list
    return [[sublist_1], [sublist_2], ... , [sublist_N]]
```

### Managing Data

Once we have a subset of lists grouped by desired criteria, we can generalize a
function to operate on all files in that list.

We'll make use of the `map(function, list)` function, which applies `function`
to each item in `list`. This is a shortened way of writing the following:

```python
# Equivalent of map(function, my_list)
for item in my_list:
    function(item)
```

For our list of sub-lists, we can read each file in our sub-list into a
dataframe and concatenate all dataframes from the sub-lists into one dataframe
with the `pd.concat()` function.

```python
month_df = pd.concat(map(pd.read_csv, sublist))
```

As we'll need to repeat this dataframe creation for each sub-list in our parsed
list, we'll put it in a for loop and append each dataframe to a list.

```python
def import_files_into_dataframe(files_as_list):
    list_of_dataframes = []
    for sublist in parsed_list:
        month_df = pd.concat(map(pd.read_csv, sublist))
        list_of_dataframes.append(month_df)
    return list_of_dataframes
```

We can now pick out the max value from each dataframe in a simple way.

```python
def get_max_values(list_of_dataframes):
    list_of_max_values = []
    for dataframe in list_of_dataframes:
       month_max = dataframe.max()
       list_of_max_values.append(month_max)
    return list_of_max_values
```

### Writing Results

Our results lie in the `list_of_max_values` result from the `get_max_values()`
function. We can more simply write all lines of this dataframe to a single
file, meaning we only need to open and close it once instead of opening and
closing the file in each for loop.

```python
with open('summary.csv', 'a') as outfile:
    outfile.write(list_of_max_values)
```

## Make it idempotent

A script should yield the same results if called on the same conditions. In our
case, the write statement is appending data to our `summary.csv` file.

We initially opened in _append_ mode because opening in _write_ mode would
overwrite the results of the previous month with those from the current month
during each new loop.

There are two potential solutions to this problem:

1. Write all of the columns of the dataframe in one step, overwriting the
existing contents from previous runs.
2. Append only new data to the results.

## More Resources

- [How to Program a Game! (in Python)][pygame] (Video: 1:10:06)
- [Professional Code Refactor! (Cleaning Python Code & Rewriting it to use
Classes)][pygame-refactor] (Video: 1:02:29)
- [Refactoring Guru][refactoring-guru]

[pygame]: https://youtu.be/-8n91btt5d8
[pygame-refactor]: https://youtu.be/731LoaZCUjo
[refactoring-guru]: https://refactoring.guru/refactoring
