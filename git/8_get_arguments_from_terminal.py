# using sys library you can give the .py file input arguments like a list
# example of command in terminal:
# python 8_get_arguments_from_terminal.py ali hasan reza hossein 12 15

# here sys just gets positional inout arguments
# you use argparse to give flags (--) and option (-) as the input to the file


import sys

print(sys.argv)
# sys.argv be shoma ye list bermigardune az argument haiy ke ma be onvan be input be python tuye terminal dadim
# hala avalish mishe esm e file badi hash ham mishe baghie ye argument ha

# print('the 2nd argument:')
# print(sys.argv[2])