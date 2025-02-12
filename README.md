# SmartExecutor

SmartExecutor is a Python library that automatically determines whether a given task is CPU-bound or I/O-bound and dispatches it to the appropriate executor. This solves a common problem in Python where developers must manually decide between using threading (for I/O-bound tasks) or multiprocessing (for CPU-bound tasks), especially in light of the Global Interpreter Lock (GIL).

## Problem Statement

In Python, concurrency is often handled using either:

- **Threading:**  
  Suitable for I/O-bound tasks (e.g., network operations, file I/O) because threads can handle waiting without blocking the main thread. However, due to the GIL, threads do not run CPU-bound code in parallel.

- **Multiprocessing:**  
  Ideal for CPU-bound tasks (e.g., heavy computations) since each process runs independently and bypasses the GIL. However, processes have higher overhead, and managing inter-process communication and resource sharing can be complex.

Developers must manually choose the best method for each task. This not only complicates the code but can also lead to suboptimal performance if the wrong method is used.

## How SmartExecutor Solves This

SmartExecutor automates the decision-making process by:
- **Analyzing the Task:**  
  It performs both static analysis (e.g., scanning the source code for keywords like `sleep` or network calls) and micro-profiling (comparing CPU time with wall time) to determine if a function is CPU-bound or I/O-bound.
- **Dynamic Task Dispatch:**  
  - CPU-bound tasks are submitted to a **ProcessPoolExecutor**.
  - I/O-bound tasks are submitted to a **ThreadPoolExecutor**.
- **Unified API:**  
  Developers simply use the `run()` function, and the library handles the rest.

## Example Usage

Below are two examples that demonstrate how to use SmartExecutor.

### Example 1: CPU-bound Task

```python
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

```


# TO BE CONTINUED . . .