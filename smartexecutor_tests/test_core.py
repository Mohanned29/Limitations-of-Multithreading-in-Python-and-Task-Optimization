import unittest
import time
from smartexecutor.core import run

def cpu_bound_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_bound_task(delay):
    time.sleep(delay)
    return "I/O task completed"

class TestCore(unittest.TestCase):
    def test_cpu_bound_task(self):
        result = run(cpu_bound_task, 10000)
        self.assertEqual(result, sum(i * i for i in range(10000)))

    def test_io_bound_task(self):
        result = run(io_bound_task, 1)
        self.assertEqual(result, "I/O task completed")

if __name__ == '__main__':
    unittest.main()
