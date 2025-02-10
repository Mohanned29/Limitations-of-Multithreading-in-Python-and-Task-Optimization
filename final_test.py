import unittest
import time
import os
import types

from smartexecutor.core import run
from smartexecutor.config import Config
from smartexecutor.task_manager import TaskManager

def cpu_intensive_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_intensive_task(delay):
    time.sleep(delay)
    return "io_done"

def exception_task():
    raise ValueError("Intentional error for testing")

def generator_task(n):
    for i in range(n):
        yield i
    return "generator_complete"

def generator_task_wrapper(n):
    gen = generator_task(n)
    output = []
    try:
        while True:
            output.append(next(gen))
    except StopIteration as e:
        final = e.value
    return (output, final)


class TestSmartExecutorFull(unittest.TestCase):
    def test_cpu_bound_task(self):
        n = 10000
        expected = sum(i * i for i in range(n))
        result = run(cpu_intensive_task, n)
        self.assertEqual(result, expected)

    def test_io_bound_task(self):
        delay = 0.5
        result = run(io_intensive_task, delay)
        self.assertEqual(result, "io_done")

    def test_exception_handling(self):
        with self.assertRaises(ValueError) as context:
            run(exception_task)
        self.assertIn("Intentional error", str(context.exception))

    def test_generator_task(self):
        result = run(generator_task_wrapper, 5)
        expected_output = list(range(5))
        expected_final = "generator_complete"
        self.assertEqual(result, (expected_output, expected_final))

    def test_multiple_concurrent_tasks(self):
        delays = [0.2, 0.3, 0.1, 0.4]
        results = [run(io_intensive_task, d) for d in delays]
        self.assertEqual(results, ["io_done"] * len(delays))

    def test_multiple_tasks_with_custom_task_manager(self):
        manager = TaskManager()
        futures = []
        for i in range(6):
            if i % 2 == 0:
                futures.append(manager.submit_cpu_task(cpu_intensive_task, 5000))
            else:
                futures.append(manager.submit_io_task(io_intensive_task, 0.2))
        results = [f.result() for f in futures]
        for i, res in enumerate(results):
            if i % 2 == 0:
                expected = sum(j * j for j in range(5000))
                self.assertEqual(res, expected)
            else:
                self.assertEqual(res, "io_done")
        manager.shutdown()

    def test_config_modification_effect(self):
        original_threads = Config.MAX_THREADS
        original_processes = Config.MAX_PROCESSES
        Config.set_max_threads(2)
        Config.set_max_processes(2)
        manager = TaskManager()
        future = manager.submit_io_task(io_intensive_task, 0.1)
        result = future.result()
        self.assertEqual(result, "io_done")
        manager.shutdown()
        Config.set_max_threads(original_threads)
        Config.set_max_processes(original_processes)

    def test_logging_output(self):

        log_file = Config.LOG_FILE
        if os.path.exists(log_file):
            os.remove(log_file)
        run(io_intensive_task, 0.1)
        self.assertTrue(os.path.exists(log_file))
        with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            self.assertTrue(len(content) > 0, "Log file should not be empty.")

if __name__ == '__main__':
    unittest.main()
