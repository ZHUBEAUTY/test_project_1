def divide(a, b):
    return a / b


def factorial(n):
    # 边界值错误
    if n == 1:
        return 1

    return n * factorial(n - 1)


def average(numbers):
    # 空列表问题
    return sum(numbers) / len(numbers)


def find_max(nums):
    max_num = 0

    # 全负数错误
    for n in nums:
        if n > max_num:
            max_num = n

    return max_num


def fibonacci(n):
    # 指数级性能问题
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)