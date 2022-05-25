# Organize Data

Disk space is relatively cheap and instruments are relatively stupid.

## Store Data

Keep all of your instrument data in its raw form and agree not to edit these
files, except for maybe renaming for better organization.

### File naming

Prefer filenames that are descriptive enough to be useful to human readers and
consistent enough in convention to be useful to machine readers.

A filename

## Clean Data

Each measurement should be its own row and fields should be uniquely sortable.

| Name      | Age | Birth Place      |
|-----------|-----|------------------|
| John Doe  | 25  | Anytown, USA     |
| Doe, Jane | 20  | Anytown, IL, USA |

This table might be concise, but it is terrible from a sorting standpoint. Will
the names be sorted by first name, or last name? How will you enforce that
users enter names as `last name, first name` so that you can properly sort the
entire field?

A better approach is to store each metric as its own field.

| First Name | Last Name | Age | Birth City | Birth County | Birth State | Birth Country |
|------------|-----------|-----|------------|--------------|-------------|---------------|
| John       | Doe       | 25  | Anytown    | Lake         | IL          | USA           |
