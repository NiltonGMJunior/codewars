#   Finding An Appointment   -   CodeWars
#   Nilton Gomes Martins Junior
#   01/09/2018
#   https://www.codewars.com/kata/525f277c7103571f47000147/train/python

def clock_to_int(clock):
    return int(clock[:2])*60 + int(clock[3:])

def int_to_clock(integer):
    hours = integer // 60
    minutes = integer % 60
    return ('0' + str(hours))[-2:] + ':' + (str(minutes) + '0')[0:2]

def get_possible_start(slots, duration):
    return [slot[0] for slot in slots if (slot[1] - slot[0]) >= duration]

def get_free_gaps(schedule):
    free_gaps = []
    index = 0
    if schedule[0][0] != '09:00':
        free_gaps.append([clock_to_int('09:00'), clock_to_int(schedule[0][0])])
        index += 1
    while True:
        try:
            gap_start = schedule[index][1]
            gap_end = schedule[index + 1][0]
            free_gaps.append([clock_to_int(gap_start), clock_to_int(gap_end)])
            index += 1
        except IndexError:
            break
    if schedule[-1][-1] != '19:00':
        free_gaps.append([clock_to_int(schedule[-1][-1]), clock_to_int('19:00')])

    return free_gaps

def get_start_time(schedules, duration):

    return

def main():
    schedule = [['09:00', '11:30'], ['13:30', '16:00'], ['16:00', '17:30'], ['17:45', '19:00']]
    gaps = get_free_gaps(schedule)
    print(get_possible_start(gaps, 60))
    return

if __name__ == "__main__":
    main()
