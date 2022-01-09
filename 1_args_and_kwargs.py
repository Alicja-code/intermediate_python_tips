def check_var_args(f_arg, *args):
    print("first normal arg: ", f_arg)
    for arg in args:
        print("another arg from *args: ", arg)


check_var_args('1st', 'extra', 'additional', 'onemore')


# calling a function
def check_var_args_2(f_arg, arg1, arg2, arg3):
    print("first normal arg: ", f_arg)
    print("arg1: ", arg1)
    print("arg2: ", arg2)
    print("arg3: ", arg3)


args_2 = ('extra', 'additional', 'onemore')
check_var_args_2('1st', *args_2)


# **kwargs can be split into key and value
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print(f"My {key} is {value}")


greet_me(name="Alice")
