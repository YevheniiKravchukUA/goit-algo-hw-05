from task_1.main import caching_fibonacci as task_1
import task_2.main as task_2

# Task 1 
#
t_1 = task_1()
print(t_1(10))
print(t_1(9))  # Так как мы не видим print, это значит что мы получаем значения из cach. Блок else не выполняется. task_1 > main.py, line 13, print(cache)
print(t_1(14))
#
# Task 2
#
msg = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = task_2.sum_profit(msg, task_2.generator_numbers)
print(f"Загальний дохід: {total_income}")
#
# Task 3
#
