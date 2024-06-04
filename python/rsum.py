from dataclasses import dataclass
import sys

@dataclass
class DataError(Exception):
    data: str

def robust_sum(xs):
    total = 0
    for x in xs:
        try:
            total += int(x)
        except ValueError:
            raise DataError(x)
    return total

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            break
        items = line.split()
        try:
            sum_result = robust_sum(items)
            print(sum_result)
        except DataError as e:
            computable = []
            for item in items:
                try:
                    computable.append(int(item))
                except ValueError:
                    break
            sum_result = sum(computable)
            print(f"({sum_result})")
            