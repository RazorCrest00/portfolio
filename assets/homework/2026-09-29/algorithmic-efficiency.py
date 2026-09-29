# CODE_RUNNER: 3.17 Homework - Library workload calculator

def catalog_work(n):
    if type(n) is not int or n < 0:
        raise ValueError("Book count must be a nonnegative whole number")
    return {"books": n, "visits": n, "ordered_pairs": n * n}

for n in [12, 24, 0]:
    report = catalog_work(n)
    print("Books:", report["books"])
    print("Single-pass visits:", report["visits"])
    print("Ordered pairs (including self-pairs):", report["ordered_pairs"])
