# Nurse Scheduling Task

The team needs to solve a scheduling problem for assigning shifts to a team of 8 nurses, which includes:

## Description

The team needs to solve a scheduling problem for assigning shifts to a team of 8 nurses, which includes:

1. 4 full-time nurses: An, Bình, Chiến, and Dương, who work 36 hours per week, divided into 18 shifts of 8 hours during the week.
2. 4 part-time nurses: Linh, Kiên, Giang, and Hòa, who work 20 hours per week, divided into 10 shifts during the week.

### Shift Requirements:

1. The work schedule for a week is divided into shifts assigned to days (from 1 to 5) and shift times (morning, afternoon, evening). The workday spans from 6:00 AM to 10:00 PM, with each shift lasting 4 hours.
2. Each shift must have at least 2 nurses (with at least 1 full-time nurse).
3. After completing a shift, ensure that the arrangement is suitable and optimal: each nurse works no more than 8 hours per day and has at least 2 days off per week (part-time nurses will have at least 1 day off per week).
4. The shifts are spread over 7 days a week, with 3 shifts per day (a total of 21 shifts per week), but the actual number of shifts may be fewer depending on the team's schedule.

## Requirements

Create the schedule for the team from Monday, August 5, 2024, to Sunday, September 1, 2024.

The schedule must ensure even distribution among team members and meet the following conditions:

1. Does the solution meet the minimum requirements or exceed the hard constraints? What conditions should not be violated?
2. Create a feasible (satisfactory) schedule while considering the optimal conditions. How can this be achieved?
3. In addition to the hard constraints, the nurses have the following preferences:
   - The full-time nurse An should have at least 2 days off each week.
   - Part-time nurses can adjust their shifts more flexibly based on their off days.

### Additional Considerations

If these preferences can be considered as possible (soft constraints), how would they be modeled? Find the closest solution to the new problem that includes both hard and soft constraints mentioned above. How can one solution be evaluated as better than another?

## References

1. De Bruecker, J., Van den Bergh, J., Belien, E., & Demeulemeester, E. (2015). Workforce planning incorporating job satisfaction. *European Journal of Operational Research*, 8-18.
2. Soto, R., Godseci, M., & Palma, F. (2015). Recursive and parametric scheduling: A case study. *Research Journal of Information Science and Technology*, 52-64.
