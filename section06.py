# Section06

# 예제1
def hello(world):
    print("Hello", world)

hello("Python!")
hello(7777)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

print(hello_return("PYthon!!!!"))

# 예제3 - 다중 리턴
def func_mul(x):
    return x*100, x*200, x*300
val1, val2, val3 = func_mul(100)
print(val1, val2, val3)

# 예제4
def func_mul2(x):
    return (x*100, x*200, x*300)

lt = func_mul2(100)
print(lt, type(lt))

# 예제5
def args_func(*args):
    print(args)

args_func('kim')
args_func('kim', 'Park')
args_func('kim', 'Park', 'Lee')

# 예제6
def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(name1 = 'kim', name2 = 'park') # dictionary로 출력됨.

# 전체 혼합
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)

# 중첩함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 10000)

nested_func(10000)



# 예제7
def func_mul3(x : int) -> list:
    return [x*100, x*200, x*300]

print(func_mul3(5))
print(func_mul3(5.)) # 타입이 틀렸다고 해서 오류가 발생하지는 않는다.

print()


# 일반적 함수
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func, type(var_func)) # 함수는 객체를 생성 == 메모리 할당
print(var_func(10))

# lambda
lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10, type(lambda_mul_10)) # 람다식은 즉시 실행 -> 메모리 초기화
print(lambda_mul_10(100))
'''
<function mul_10 at 0x000002757B8C42F0> <class 'function'>
100
<function <lambda> at 0x000002757B8C4378> <class 'function'>
1000
'''

print()

