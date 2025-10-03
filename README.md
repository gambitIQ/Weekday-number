The program takes the user's input to determine the weekday for any day in the year. 


1. Input two integers:
- The weekday number of the first day of the year (0–6).
- The day number in the year whose weekday you want.

2. Logic:
- The first day is known (e.g., Tuesday = 2).
- To reach any later day, you move (day_number – 1) steps forward.
- Example: Day 10 → 9 steps ahead of the first day.
- There are 7 days in a week, so the index must reset 

3. Calculation:
- New index = (start_index + (day_number – 1)) % 7.
- % 7 ensures the weekday index resets after 6 back to 0.

4. Output:
- The weekday index for the given day of the year.
