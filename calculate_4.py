def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    return x / y
def mod(x, y):
    return x % y


if __name__ == "__main__":    # 프로그램의 시작점일 때만 아래 코드 실행
    x= input("x: ")
    x= int(x)
    y= input("y: ")
    y= int(y)
    print(f"{x} + {y} is {x + y}")
    print(f"{x} - {y} is {x - y}")
    print(f"{x} * {y} is {x * y}")
    print(f"{x} / {y} is {x / y}")
    print(f"{x} // {y} is {x // y}")
