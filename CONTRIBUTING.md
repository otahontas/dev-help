## How to contribute

If you're reading this, it means you saw something that is not right or you want to add a new feature. That's great, we are already glad that you can contribute.

## Submitting Issues
We have templates for submitting new issues, that you can fill out. For example if you found a bug, use the following [template to report a bug](../../issues/new?template=bug_report.md).

## Submitting changes

When you've made some changes you are happy with please send a [GitHub pull request](../../pull/new/master) to `master` branch with a clear list of what you've done (read more about [pull requests](https://help.github.com/en/articles/about-pull-requests)).

Please follow our git branches model and coding conventions (both below), and make sure all of your commits are atomic (preferably one feature per commit). 

Always write a clear log message for your commits, and if there is an issue open, reference that issue. This guide might help: [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/).

Once submitted, we'll check the pull request.

### Project structure, testing and code conventions

We have a handful of rules about how we do testing, which code conventions we follow and how new additions (such as components to frontend or routes to backend) should be structured. Please check documentation for the part you're contributing to before submitting your pull request.

### Git Branches

We use `master` branch as the main development branch and create releases from it every now and then.

When submitting changes, give your branch a short descriptive name (like the names between the `<>` below) and prefix the name with something representative for that branch:
  - `feature/<feature-name>` - used when an enhancement or new feature was implemented
  - `docs/<what-the-docs>` - missing docs or keeping them up to date
  - `bugfix/<caught-it>` - solved a bug
  - `test/<testing-that-naughty-bug>` - adding missing tests 
  - `refactor/<that-name-is-confusing>` - well we hope we don't mess anything and we don't get to use this
  - `hotfix/<oh-no>` - for when things needed to be fixed yesterday
  
  Thanks!
