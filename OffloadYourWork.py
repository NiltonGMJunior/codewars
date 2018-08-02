#   Nilton Gomes Martins Junior
#   31/07/2018
#   CodeWars - Offload Your Work! - http://www.codewars.com/kata/offload-your-work/train/python

def work_needed(projectMinutes, freeLancers):
    freelancers_worktime = sum([60*hours + minutes for (hours, minutes) in freeLancers])
    if freelancers_worktime >= projectMinutes:
        output = 'Easy Money!'
    else:
        work_minutes = projectMinutes - freelancers_worktime
        hours = work_minutes // 60
        minutes = work_minutes - hours * 60
        output = 'I need to work ' + str(hours) + ' hour(s) and ' + str(minutes) + ' minute(s)'
    
    return output

def main():
    print(work_needed(60, [(0, 50)]))
    return

if __name__ == "__main__":
    main()