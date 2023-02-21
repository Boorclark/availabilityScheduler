import pandas as pd

# read the Excel file
df = pd.read_excel('availability.xlsx', header=None)

# define the start and end times for the day
start_time = pd.Timestamp('8:00')
end_time = pd.Timestamp('17:00')

# iterate over each row (student)
for i, row in df.iterrows():
    name = row[0]
    times = row[1:].dropna()  # extract the available times for this student

    # convert the times to datetime objects
    times = pd.to_datetime(times, format='%I:%M%p')

    # initialize a list of free time intervals
    free_times = [(start_time, times[0])]

    # iterate over each pair of adjacent available times
    for j in range(1, len(times)):
        free_times.append((times[j-1], times[j]))

    # add the last free time interval
    free_times.append((times[-1], end_time))

    # filter out any free time intervals outside the 8am-5pm range
    free_times = [(start, end) for start, end in free_times
                  if (start >= start_time) and (end <= end_time)]

    # print the free time intervals for this student
    print(f"Free times for {name}:")
    for start, end in free_times:
        print(f"\t{start.strftime('%I:%M%p')} - {end.strftime('%I:%M%p')}")