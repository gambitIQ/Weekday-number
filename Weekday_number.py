#CS110A Zamambo Mkhize Assignment: Weekday number

#Step 1: Get input of the days of the year we are looking at 
wk_day_yr_start = int(input('Enter the weekday number of the first day of year: ')) 
yr_day_find= int(input('Enter the day number of the year, for which you want to find out the weekday: '))

#Step 2: Calculate the weekday which the day falls into 
# step2a add the start day and target day to get the total days under consideration
# step2b adjust the total days to align to days of the week by subtracting 1, then calculate the weekday number with %7 
yr_days_total = int(wk_day_yr_start + yr_day_find) #step2a
wk_day_num = (yr_days_total -1)%7 #step2b

#Step 3: Output the weekday number 
print(f'That will be weekday number: {wk_day_num}')

'''Sample Output1:
Enter the weekday number of the first day of year: 3
Enter the day number of the year, for which you want to find out the weekday: 10
That will be weekday number: 5 

Sample Output2:
Enter the weekday number of the first day of year: 3
Enter the day number of the year, for which you want to find out the weekday: 17
That will be weekday number: 5
'''