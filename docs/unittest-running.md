# unittest

## What would be the different ways to run the unittest through the terminal?

There are several ways to run unittest test cases through the terminal,
depending on your needs and preferences. Here are some of the most 
common options:

1. Using `python -m unittest`:

   The simplest way to run unittest tests from the terminal is to use the
   `python -m unittest` command followed by the name of the module containing 
   your test cases. For example, to run tests defined in a file named 
   `test_module.py`, you can use the following command:

        python -m unittest test_module

2. Using test discovery:

   If your project has multiple test modules and you want to run all the tests, 
   you can use test discovery. To use test discovery, navigate to the directory 
   containing your tests and run the following command:

        python -m unittest discover

    This command will discover all the test modules in the current directory 
    and its subdirectories, and run all the tests in those modules.

3. Using TestLoader:

   Another way to run unittest tests is to use the `TestLoader` class. This 
   allows you to programmatically load and run tests. You can create a 
   TestLoader instance and use it to load the test cases from a test module, 
   then run the tests using a `TextTestRunner`. Here is an example:

        import unittest

        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(test_module)
        runner = unittest.TextTestRunner()
        runner.run(suite)

4. Using a test runner:

   If you prefer to use a graphical user interface to run your tests, you can 
   use a test runner such as nose or pytest. These test runners provide 
   additional features such as test coverage analysis and test output 
   formatting. To use nose, for example, you can install it using pip, then run 
   your tests using the `nosetests` command:

        pip install nose
        nosetests


## How does `python -m unittest discover -v` command discover folder structure?

The command `python -m unittest discover -v` is used to discover and run all 
tests in a project using the unittest testing framework. It uses a default test 
discovery mechanism to locate and load test cases and test suites. The discovery 
process starts at the directory specified as the start directory and recursively 
searches for modules that match the `test*.py` pattern.

When you run `python -m unittest discover -v`, the unittest framework first 
looks for a start directory from which to start searching for tests. If no 
directory is specified, it uses the current working directory. It then looks 
for all Python files in the start directory and its subdirectories that match 
the `test*.py` pattern. These files are assumed to contain tests.

Once it has found the test files, the unittest framework loads the tests from 
these files and runs them. It looks for test cases and test suites defined 
using the unittest framework's testing classes and methods, and it runs them 
in the order in which they are defined.

The -v option is used to enable verbose output, which provides more detailed 
information about the tests being run, such as the test case and method names, 
the outcome of each test, and any errors or failures.

In summary, the `python -m unittest discover -v` command discovers the folder 
structure by searching for Python files that match the `test*.py` pattern in 
the specified or current working directory and its subdirectories. It then 
loads and runs the tests defined in these files using the unittest framework's 
testing classes and methods.


## Especific folder/script

To run the tests using unittest, you can use the discover command to discover 
and run all test cases in the tests folder and its subdirectories. Here's an 
example command to run all tests with discover:

   python -m unittest discover tests

This command will run all tests in the `tests` folder and its subdirectories. 
By default, discover looks for files that match the pattern `test*.py` and 
runs all test cases defined in those files. If you want to run tests only in 
specific packages, you can use the -s option to specify the directory 
containing the package. For example, to run only the tests in `package1`, 
you can run:

   python -m unittest discover -s tests/package1

This will discover and run all tests in the `tests/package1` directory. 
If you want to run a specific test module or test case, you can use the `-p` 
option to specify the file pattern. For example, to run only the tests in 
`test_module1.py` in package1, you can run:

   python -m unittest discover -s tests/package1 -p test_module1.py


## Especific test case inside your test file

If you want to run a specific test case inside your test file, you can use 
the `-k` option and provide the test case name or pattern. For example, if 
you have a test case called `test_addition` inside your `test_module1.py` 
file, you can run only that test case using the command: 

   python -m unittest discover -s tests/package1 -p test_module1.py -k test_addition 

In this command, the `-k` option specifies the test case name or pattern that 
you want to run. You can use any substring of the test case name or a regular 
expression to match multiple test cases. 

For example, if you have two test cases called `test_addition` and `
test_subtraction` inside your `test_module1.py` file, you can run both test 
cases using the command: 

   python -m unittest discover -s tests/package1 -p test_module1.py -k test_ 

In this command, the `-k` option specifies a pattern that matches any test 
case name that contains the substring `test_`, which will match both `
test_addition` and `test_subtraction`. 

I hope that helps! Let me know if you have any further questions. 