import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from smartexecutor.core import run

def heavy_computation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total

if __name__ == "__main__":
    n = 1000000
    result = run(heavy_computation, n)
    print("CPU-bound task result:", result)
