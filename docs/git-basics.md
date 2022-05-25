---
date: Mon May 16 14:45:28 CDT 2022
author: David Curie
title: Git Basics
subject: Computing Essentials
keword: git
---

# Git Basics

## Why Git?

Git is to file systems what _Track Changes_ is to Word. As a project evolves,
files get moved to other folders, figures get updated, and documentation gets
rewritten. Git provides a way to track a project's provenance through
user-created system snapshots called _commits_.

Sharing documents in the cloud is good for real-time collaboration when the
number of people contributing is small. For files whose contents depend on
values defined in other addressable files, a shared document loses its ability
to manage the complete scope of changes. Shared online folders might better
suit this scenario, but many synchronized folders lack an easy way to inspect
the history of changes. Users may then be mistakenly tempted to duplicate
files at various iteration points. This approach is wasteful and ripe for
abuse.

![Version control helps organize iterations](images/phd101212s.png "PhD comic of cluttered filenames")

## Basic Commands

```sh
git add .
```
Add all updates files to the staging directory.
