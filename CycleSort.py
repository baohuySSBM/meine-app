import random


def cycle_sort(arr):
    writes = 0

    for cycle_start in range(0, len(arr) - 1):
        item = arr[cycle_start]
    
        pos = cycle_start
        for i in range(cycle_start + 1, len(arr)):
            if arr[i] < item:
                pos += 1
        
        if pos == cycle_start:
            continue

        while item == arr[pos]:
            pos += 1
            arr[pos], item = item, arr[pos]

        writes += 1

        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(arr)):
                if arr[i] < item:
                    pos += 1

            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]
            writes += 1

    return arr


arr = [random.randint(5, 900) for _ in range(25)]

print(f"Unsorted: {arr}")
cycle_sort(arr)       
print(f"Sorted: {arr}")
