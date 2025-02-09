import unittest
from SmartExecutor.task_manager import TaskManager

def sample_task(x, y):
    return x + y

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_submit_io_task(self):
        future = self.manager.submit_io_task(sample_task, 1, 2)
        self.assertEqual(future.result(), 3)

    def test_submit_cpu_task(self):
        future = self.manager.submit_cpu_task(sample_task, 10, 20)
        self.assertEqual(future.result(), 30)

    def tearDown(self):
        self.manager.shutdown()

if __name__ == '__main__':
    unittest.main()
