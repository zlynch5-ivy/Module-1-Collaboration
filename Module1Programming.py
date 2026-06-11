seconds_per_min = 60
minutes_per_hour = 60
hours_per_day = 24

seconds_per_hour = minutes_per_hour * seconds_per_min
seconds_per_day = seconds_per_hour * hours_per_day

task1 = seconds_per_day / seconds_per_hour
task2 = seconds_per_day // seconds_per_hour

print(task1)
print(task2)
