import unittest

from smartexecutor.core import run

def hanging_task():
    while True:
        pass

def crashing_task():
    raise RuntimeError("Intentional crash!")

class TestEdgeCases(unittest.TestCase):
    def test_hanging_task_timeout(self):
        """Ensure that hanging tasks are terminated after a timeout."""
        with self.assertRaises(TimeoutError):
            run(hanging_task)

    def test_crashing_task(self):
        """Ensure that a task raising an exception is handled correctly."""
        with self.assertRaises(RuntimeError):
            run(crashing_task)

