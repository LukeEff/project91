import json
import threading


def main():
    # get ranges from sum_range.json
    ranges = read_ranges_from_json()

    n = len(ranges)
    result = [0] * n
    threads = []
    for i in range(n):
        # Create threads
        thread = threading.Thread(target=add_range_of_numbers, args=(ranges[i][0], ranges[i][1], result, i))
        threads.append(thread)
        thread.start()
    # Wait for all sub-threads to finish
    for thread in threads:
        thread.join()

    print(result)
    print(sum(result))


def add_range_of_numbers(begin, end, result_array, index):
    # use closed form to calculate sum of numbers from begin to end
    result_array[index] = closed_form_sum(begin, end)
    # slower complexity
    # result_array[index] = sum(range(begin, end + 1))


def closed_form_sum(begin, end):
    return (end * (end + 1)) // 2 - (begin * (begin - 1)) // 2


def read_ranges_from_json():
    with open("sum_range.json", "r") as f:
        ranges = json.load(f)
        return ranges


if __name__ == "__main__":
    main()
