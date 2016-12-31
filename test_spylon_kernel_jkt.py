"""Example use of jupyter_kernel_test, with tests for IPython."""

import unittest
import jupyter_kernel_test
import os


coverage_rc = os.path.abspath(os.path.join(os.path.dirname(__file__), ".coveragerc"))
os.environ["COVERAGE_PROCESS_START"] = coverage_rc


class SpylonKernelTests(jupyter_kernel_test.KernelTests):
    kernel_name = "spylon-kernel"
    language_name = "scala"
    # code_hello_world = "disp('hello, world')"
    completion_samples = [
        {'text': 'val x = 8; x.toL',
         'matches': {'x.toLong'}},
    ]
    code_page_something = "x?"

    # TODO: These are disabled for now since the eventloop that runs for the interpreter blocks.
    #       They work decently well for notebooks though.

    # code_hello_world = '''
    #     println("hello, world")
    #     '''
    #
    # code_stderr = '''
    #     Console.err.println("Error")
    #     '''

    complete_code_samples = ['val y = 8']
    incomplete_code_samples = ['{ val foo = 9 ']
    invalid_code_samples = ['val {}']


if __name__ == '__main__':
    unittest.main()