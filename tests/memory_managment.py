import unittest
import psutil

from smartexecutor.core import run

def memory_intensive_task():
    """Allocate a large amount of memory to test resource management."""
    return [0] * 10**7  # Allocate ~76MB

class TestMemoryManagement(unittest.TestCase):
    def test_memory_cleanup(self):
        """Ensure no memory leaks occur after task execution."""
        process = psutil.Process()
        memory_before = process.memory_info().rss  # Resident Set Size (RSS)
        run(memory_intensive_task)
        memory_after = process.memory_info().rss
        self.assertTrue(memory_after < memory_before * 1.5)  # Memory shouldn't increase too much

