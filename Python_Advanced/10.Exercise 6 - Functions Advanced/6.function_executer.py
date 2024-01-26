# def func_executor(*funcs_data):
#     result = []
#
#     for func, args in funcs_data:
#         result.append(f"{func.__name__} - {func(*args)}")       # тук разопаковаме args, което е value-to в съотвяетние key-value pair ,
#     return "\n".join(result)                                                          # за да може съответните аргументи num1, num2 да отидат към съответните параметри

### Second solution ###
#Това е функцията, която изпълнява тест кода.
# Чрез цикъл for loop минаваме през tuple от tuples,
# които представляват KVP и за всяка фунцкия принтраме името
# и чрез  {func.__name__}, а чрез {func(*args)}
# извикваме съответната функция и подаваме аргументи като ги разпакетираме чрез *.
# ако него направим ще изпратим един цял tuple от (num1, num2) в параметъра num1, а за
# num2 няма да им аргумент и ще ни хвърли error.
def func_executor(*funcs_data):
    result = []

    return "\n".join([f"{func.__name__} - {func(*args)}" for func, args in funcs_data])  # Идентичен запис, но чрез comprehension


# Това е зададение тест код.
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))