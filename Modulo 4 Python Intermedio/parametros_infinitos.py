def my_function_with_infinite_params(*args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")


my_function_with_infinite_params(
    2, 5, 6, 3, 6, 5, 6
)

#combinacion con otros parametros
def my_function_with_infinite_params(my_other_param, *args):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"My other param: {my_other_param}")


my_function_with_infinite_params(10, 2, 5, 6, 3, 6, 5, 6)

#args primero, se define en el parametro el valor del parametro finito
def my_function_with_infinite_params(*args, my_other_param):
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"My other param: {my_other_param}")


my_function_with_infinite_params(2, 5, 6, 3, 6, 5, 6, my_other_param=10)


#Kwargs(keyword arguments **)
#siempre van de ultimo
def my_function_with_infinite_named_params(parameter_1, **kwargs):
    print(f"Parameter 1: {parameter_1}")
    print(f"Kwargs: {kwargs}")


my_function_with_infinite_named_params("Hello", my_other_parameter="World", whatever=6)

#args y kwargs en conjunto
def my_function(first_parameter, *args, **kwargs):
    print(f"First parameter: {first_parameter}")
    for index, arg in enumerate(args):
        print(f"Arg {index}: {arg}")

    print(f"Kwargs: {kwargs}")


my_function("First value", 1, 2, 3, 4, my_other_parameter="World", whatever=6)