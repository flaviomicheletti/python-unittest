# `unittest` vs `unittest2` differences


## question

I would like to discuss and understand the differences between
`unittest` and `unittest2`?

Has `unittest2` been released yet?

What was the biggest motivation for developing `unittest2`?

What they are building with `unittest2` couldn't be done by improving `unittest`?

## Response

Firstly, `unittest` is a testing framework included in Python's standard library 
since version 2.1. It provides a set of tools for writing and running tests.

`unittest2` is an enhanced version of the `unittest` framework that was 
developed for Python 2.x to provide additional features and improvements to 
`unittest`. It is essentially a backport of some features from `unittest` 
in Python 3.x, and was meant to be used as a drop-in replacement for `unittest` 
in Python 2.x. `unittest2` has since been deprecated and is no longer actively
maintained.

The biggest motivation for developing `unittest2` was to bring some of the 
features of `unittest` in Python 3.x to Python 2.x. Some of these features 
include:

- SubTest functionality: This allows you to group multiple test cases into a 
  single test method, and to identify which sub-test failed if any of them fail.
- Test discovery: `unittest2` can automatically discover and run all tests 
  in a directory, whereas `unittest` requires you to manually specify the 
  test cases to run.
- Better assertion methods: `unittest2` provides additional assertion methods 
  beyond those provided by `unittest`. These include assertIn, assertIsInstance,
  assertGreater, assertRegex, and others.

While some of the features of `unittest2` have been incorporated into `unittest`
in Python 3.x, there may still be cases where `unittest2` is useful, 
particularly if you are working on a Python 2.x codebase.

As for whether the features of `unittest2` could have been added to `unittest`, 
the answer is likely yes, but it may not have been practical to do so. 
`unittest` is a part of Python's standard library, which means that changes 
to it must be carefully considered and backwards-compatible. It may have been 
easier to develop `unittest2` as a separate package, where new features could be
added more easily without affecting existing code.


## Question

So can I still focus on using `unittest` since `unittest2` is focused on 
Python 2.x and in my case I'm only interested in Python 3.x?

## Answer

Yes, if you're working with Python 3.x, you can focus on using the `unittest` 
framework that's included in the standard library. `unittest` has been improved 
and enhanced in Python 3.x, so many of the features that were added in 
`unittest2` for Python 2.x are now available in the standard `unittest` 
module in Python 3.x.

`unittest` in Python 3.x includes subtests, test discovery, and improved 
assertion methods, among other features. Additionally, the `unittest` module 
in Python 3.x has been optimized for performance, making it faster than 
`unittest` in Python 2.x.

So unless you have specific needs that aren't met by `unittest` in Python 3.x, 
you can safely use the built-in `unittest` module for your testing needs.