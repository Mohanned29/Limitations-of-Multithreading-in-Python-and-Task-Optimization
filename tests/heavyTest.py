import unittest
import time
from concurrent.futures import ThreadPoolExecutor

from smartexecutor.core import run

def cpu_heavy_task(n):
    return sum(i * i for i in range(n))

def io_heavy_task():
    time.sleep(0.5)
    return "io_done"

class TestHeavyLoad(unittest.TestCase):
    def test_high_concurrency(self):
        """Submit 100 CPU-bound and 100 I/O-bound tasks simultaneously."""
        num_tasks = 100
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=20) as executor:
            cpu_futures = [executor.submit(run, cpu_heavy_task, 5000) for _ in range(num_tasks)]
            io_futures = [executor.submit(run, io_heavy_task) for _ in range(num_tasks)]

        results = [f.result() for f in cpu_futures + io_futures]

        duration = time.time() - start_time
        print(f"Executed {2*num_tasks} tasks in {duration:.2f} seconds")
        
        self.assertEqual(results.count("io_done"), num_tasks)
        self.assertTrue(duration < 30)
