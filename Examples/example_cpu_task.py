from SmartExecutor.core import run

def heavy_computation(n):
    total = 0
    for i in range(n):
        total += i ** 2
    return total


# using the cpu for heavy computation for the test of the smartexecuter
if __name__ == "__main__":
    n = 1000000
    result = run(heavy_computation, n)
    print("Résultat du calcul intensif (CPU-bound):", result)
