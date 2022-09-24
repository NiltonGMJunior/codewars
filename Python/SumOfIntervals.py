#   Sum of Intervals - CodeWars
#   Nilton Gomes Martins Junior
#   26/09/2021
#   https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    new_intervals = sorted(intervals)
    changes = True
    while changes:
        changes, new_intervals = merge(new_intervals)
    return sum([interval[1] - interval[0] for interval in new_intervals])

def merge(intervals):
    new_intervals = [list(interval) for interval in intervals]
    if len(new_intervals) > 1:
        for i in range(len(new_intervals) - 1):
            current_interval_end = new_intervals[i][1]
            next_interval_start = new_intervals[i + 1][0]
            next_interval_end = new_intervals[i + 1][1]
            if current_interval_end >= next_interval_start:
                if current_interval_end <= next_interval_end:
                    new_intervals[i][1] = next_interval_end
                else:
                    new_intervals[i][1] = current_interval_end
                del new_intervals[i + 1]
                return True, new_intervals
    return False, new_intervals

def main():
    print(sum_of_intervals([[1, 5], [10, 20], [1, 6], [16, 19], [5, 11]]))
    print(sum_of_intervals([[1, 5], [1, 5]]))
    return

if __name__ == "__main__":
    main()
