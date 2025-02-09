import unittest
from SmartExecutor.performance_analyzer import analyze_task

def cpu_task(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

def io_task(delay):
    import time
    time.sleep(delay)
    return "done"

class TestPerformanceAnalyzer(unittest.TestCase):
    def test_cpu_task_analysis(self):
        analysis = analyze_task(cpu_task, 1000)
        self.assertEqual(analysis, "cpu")

    def test_io_task_analysis(self):
        analysis = analyze_task(io_task, 0.1)
        self.assertEqual(analysis, "io")

if __name__ == '__main__':
    unittest.main()
