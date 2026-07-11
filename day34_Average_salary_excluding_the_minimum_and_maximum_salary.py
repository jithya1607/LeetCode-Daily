#34 Average salary excluding the minimum and maximum salary
#Remove the minimum and maximum salary from the list and calculate the average of the remaining salaries.
from ast import List


def average(self, salary: List[int]) -> float:
        import numpy as np
        salary.remove(max(salary))
        salary.remove(min(salary))
        return round(np.mean(salary),5)