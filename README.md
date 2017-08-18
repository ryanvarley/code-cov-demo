[![CircleCI](https://circleci.com/gh/ryanvarley/code-cov-demo/tree/master.svg?style=svg)](https://circleci.com/gh/ryanvarley/code-cov-demo/tree/master)

# What is code coverage?

* Percentage of lines executed by the test suite.
* Lets you see which parts of the code are not tested. Including:
    * Branches within a function.
    * Tests that wernt ran

# How can I use it?

```python
py.test --cov=./
```

This uses a package called `coverage` and a plugin `pytest-cov` to generate a coverage report whilst the test suite is ran. Pytest will give a summary of the results.

```
---------- coverage: platform darwin, python 3.6.2-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
dataframe.py           31     10    68%
helpers.py              9      0   100%
test_dataframe.py      13      0   100%
test_helpers.py        10      0   100%
---------------------------------------
TOTAL                  63     10    84%
```

The coverage output is written to a `.coverage` file which looks like:

```
!coverage.py: This is a private format, don't read it directly!{"lines":{"code-cov-demo/test_dataframe.py":[1,3,6,11,15,19,23,8,12,16,20,24,25],"code-cov-demo/dataframe.py":[1,2,5,7,11,14,17,30,33,36,45,9,12,15,19,20,23,24,28,34,46,48],"code-cov-demo/test_helpers.py":[1,3,6,10,14,15,16,17,23,7,11,20,24],"code-cov-demo/helpers.py":[1,4,8,12,16,5,9,13,17]}}
```

We can make this more readable by running `coverage html`

![coverage html report](https://user-images.githubusercontent.com/1278326/29452244-8d5d7e40-83fd-11e7-9c88-24ded3af78b4.png)

We can click on a file to see the line by line

![coverage of dataframe.py](https://user-images.githubusercontent.com/1278326/29452250-910e1b12-83fd-11e7-8777-75299a0e6b6f.png)

Green marks lines ran by the test suite, red lines aren't. We can see I haven't tested the `to_csv` function and missed the `KeyError` Branch in `merge` and the `frac` branch in `sample`. Also notice that lines 19 and 20 have no coverage, this is because they are really part of line 18.

These reports are great at highlighting areas of the codebase which need more attention and should be used by repo champs to identify where work is needed when working on a story to see if you can " an area your working on could be "boy scouted".

Another powerful feature is viewing coverage in git diffs. There are packages that do this locally, but we can make these much more useful and visible in PRs using a tool like [codecov](https://codecov.io).

# Codecov

Codecov can integrate with a CI service (travis, circle, jenkins etc) and process the coverage reports after a build. The interface provides an overview of the repo, diffs for commits and integrates with pull requests.

## Homepage

The homepage shows the coverage change with time, the latest commits and and overview of the repo like our offline html report.

![](https://user-images.githubusercontent.com/1278326/29452728-5049dab0-83ff-11e7-98a8-3a0dd2ee3334.png)

## Viewing a diff

![](https://user-images.githubusercontent.com/1278326/29454036-a2f1cd28-8403-11e7-9c87-ca4d8bfd5a15.png)


## Pull Request

Codecov integrates with pull requests to provide an overview report and status checks. There are alot of numbers here, this report should be mainly be used to obviously see red flags (files with low coverage) which you will then look at the diff for.

![](https://user-images.githubusercontent.com/1278326/29454987-3ef32db8-8407-11e7-8d80-c63f79e82cc2.png)

The first chart is a coverage reach graph, it visualises how the coverage of the repo has changed. I have found these to be unreliable when posted in PRs and disabled them in mario, but they can be used if you view the report on the website. 

![](https://user-images.githubusercontent.com/1278326/29454329-a55aaa0c-8404-11e7-8901-06869b3ee936.png)

See [here](https://docs.codecov.io/docs/graphs#section-coverage-reach) for more info.

Codecov also adds status checks to help enforce coverage on PR's

![](https://user-images.githubusercontent.com/1278326/29454601-af71199e-8405-11e7-9c68-18de13899298.png)

## Browser extension

Codecov has an extension that will overlay test coverage in github. For example, when I'm reviewing a PR diff

![](https://user-images.githubusercontent.com/1278326/29454771-5014c184-8406-11e7-9ab8-abe5ab27a1f4.png)

Test coverage is one of the easiest things to miss when reviewing a PR as its very hard to mentally link a diff of tests with the diff of changes. Codecov makes any gaps in the tests obvious, which you can request changes for.

The website still provides more information and is worth looking at, including a count of how many times each line has been executed.

# Report examples

## A test that isn't ran

I have added a new test to the code, but because I didn't prefix the function with *test* it wasn't ran by the test suite.

![A test that isn't ran](https://user-images.githubusercontent.com/1278326/29451215-ba578886-83f9-11e7-8b8a-1524ef863a08.png)

## Adding a new method with untested logic

![](https://user-images.githubusercontent.com/1278326/29455071-9fbc05b6-8407-11e7-920e-883de0cfe938.png)

Whilst I added a test, I didn't test the case where I provide a `frac` instead of `n`.


## Removing covered lines

Sometimes we delete dead code, if that code is covered you can decrease the repos coverage and fail the checks. This is OK, the checks and reports are guides for a reviewer not rules.

![](https://user-images.githubusercontent.com/1278326/29455839-a77eeefa-840a-11e7-8c8c-8b7f5f3b9bfc.png)

![](https://user-images.githubusercontent.com/1278326/29455877-d28f80fa-840a-11e7-97f1-c374c32c183e.png)

# Resources

* [Codecov - Viewing Source Code](https://docs.codecov.io/docs/viewing-source-code)
* [Codecov - Codecov Delta](https://docs.codecov.io/docs/codecov-delta)

