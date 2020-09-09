import io
import sys
import unittest


class HelloTest(unittest.TestCase):
    def test_hello(self):
        output_capture = io.StringIO()
        sys.stdout = output_capture

        import hello
        hello

        sys.stdout = sys.__stdout__
        self.assertEqual(output_capture.getvalue(), 'Hello World\n')


if __name__ == "__main__":
    unittest.main()
