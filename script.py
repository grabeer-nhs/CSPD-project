import unittest
from io import StringIO
import sys


def print_numbers():
    """Print numbers from 1 to 100"""
    for i in range(1, 101):
        print(i)


class TestPrintNumbers(unittest.TestCase):
    """Unit tests for print_numbers function"""
    
    def test_print_numbers_output(self):
        """Test that print_numbers outputs numbers 1-100"""
        # Capture stdout
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Call the function
        print_numbers()
        
        # Restore stdout
        sys.stdout = sys.__stdout__
        
        # Get the output and split by lines
        output = captured_output.getvalue().strip().split('\n')
        
        # Verify we have 100 lines
        self.assertEqual(len(output), 100)
        
        # Verify each line contains the correct number
        for i, line in enumerate(output, start=1):
            self.assertEqual(int(line), i)
    
    def test_print_numbers_range(self):
        """Test that output covers the range 1-100"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        print_numbers()
        
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip().split('\n')
        numbers = [int(line) for line in output]
        
        # Verify the range
        self.assertEqual(numbers[0], 1)
        self.assertEqual(numbers[-1], 100)
        self.assertEqual(set(numbers), set(range(1, 101)))


if __name__ == '__main__':
    unittest.main()
