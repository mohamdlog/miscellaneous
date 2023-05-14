import timeit

mycode = '''

'''

exec_time = timeit.timeit(stmt=mycode, number=1000000) * 10**3
print(f"The time of execution of above program is : {exec_time:.03f}ms")
