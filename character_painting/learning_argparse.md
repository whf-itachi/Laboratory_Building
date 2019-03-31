import argparse

parser = argparse.ArgumentParser()
# 方法add_argument() 用来指定程序需要接受的命令参数 本例中的 echo
parser.add_argument("echo")
# 方法parse_args()通过分析参数返回一些数据
args = parser.parse_args()
# 像魔法方法一样,argparse自动生成变量 echo 与我们指定的参数echo相同
print(args.echo)import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number")
args = parser.parse_args()

# 运行有点问题，因为如果不指定参数类型，argparse默认它是字符串。因此我们需要告诉argparse该参数是整型。
print(args.square**2)

# 运行结果
Traceback (most recent call last):
  File "learning_argparse.py", line 6, in <module>
    print(args.square**2)
TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="display a square of a given number", type=int)
args = parser.parse_args()

print(args.square**2)

# 执行:
python3 learning_argparse.py 4
# 运行结果
16
# 可选参数
import argparse

# 可选参数
parser = argparse.ArgumentParser()
# 当指定--verbosity时程序就显示一些东西，没指定的时候就不显示。这个参数事实上是可选的，不指定它也不会出错。如果不指定可选的参数，对应的变量就被设置为None
parser.add_argument("--verbosity", help="increase output verbosity")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on {}".format(args.verbosity))
 
# 执行:
python3 learning_argparse.py --verbosity 1
# 运行结果
verbosity turned on 1
## 接受布尔值参数
parser = argparse.ArgumentParser()
# 现在多加一个标志来替代必须给出一些值，并修改了名称来表达我们的意思。注意现在指定了一个新的关键词action，并且赋值为store_ture。如果指定了这个可选参数，args.verbose就赋值为True,否则就为False。
parser.add_argument("--verbosity", help="increase output verbosity", action="store_true")
args = parser.parse_args()
if args.verbosity:
    print("verbosity turned on {}".format(args.verbosity))

# 注:即 传入参数即值为真,不传就为假
# 简写
# 简写
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on {}".format(args.verbose))

# 执行
python3 learning_argparse.py -v 500
# 运行结果
verbosity turned on 500
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
else:
    print(answer)
    
# 执行:
python3 learning_argparse.py 4 -v # 无所谓顺序
# 运行结果
the square of 4 equals 16
16# 加入运算复杂度
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbosity", type=int,
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbosity == 2:
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbosity == 1:
    print("{}^2 == {}".format(args.square, answer))
else:
    print(answer)
    
# 执行:
python3 learning_argparse.py -v 2 3
# 运行结果
the square of 3 equals 9# 解决上面代码 -v传参无限制的bug
import argparse
parser = argparse.ArgumentParser()
# 使用choices=[],限定传参范围
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
    print(answer)# 引入参数count与default
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

# 执行:
python3 learning_argparse.py -vvv 2
# 运行结果
the square of 2 equals 4

```python

```
