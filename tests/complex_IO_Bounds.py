import unittest
import requests
import os

from smartexecutor.core import run

def fetch_google():
    """Fetch a web page to simulate network-bound I/O."""
    response = requests.get("https://www.google.com")
    return response.status_code

def file_io_task():
    """Write and read a large file to test I/O-bound handling."""
    filename = "test_large_file.txt"
    with open(filename, "w") as f:
        f.write("A" * 10**6)  # Write 1MB of data
    with open(filename, "r") as f:
        data = f.read()
    os.remove(filename)
    return len(data)

class TestIOBoundTasks(unittest.TestCase):
    def test_network_call(self):
        """Test a network request as an I/O-bound task."""
        result = run(fetch_google)
        self.assertEqual(result, 200)

    def test_file_io(self):
        """Test file I/O as an I/O-bound task."""
        result = run(file_io_task)
        self.assertEqual(result, 10**6)  # Expecting 1MB read

