import argparse
"""
parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()

print(args.square**2)
"""

"""
# 可选参数
parser = argparse.ArgumentParser()
# 现在多加一个标志来替代必须给出一些值，并修改了名称来表达我们的意思。注意现在指定了一个新的关键词action，并且赋值为store_ture。如果指定了这个可选参数，args.verbose就赋值为True,否则就为False。
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on {}".format(args.verbosity))
"""

"""
# 简写
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on {}".format(args.verbose))
"""

"""
# 混合使用定位参数和可选参数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print("the square of {} equals {}".format(args.square, answer))
    print(answer)
else:
    print(answer) 
"""

"""
# 来看看为程序加上处理重复参数的能力会怎么样：
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2],
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
"""

# 引入参数count与default
# count用于统计指定参数在传入时出现次数
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
# 加入了一个关键词default。设置它的默认值为0，这样可以让它兼容其他整型。注意，如果一个可选参数没有指定，它就会被设置成None，None是不能和整型比较的(触发[TypeError][5]异常)。
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity >= 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity >= 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
