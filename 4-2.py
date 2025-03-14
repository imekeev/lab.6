import time

number = int(input())
milliseconds = int(input())
time.sleep(milliseconds/1000)

ans = number ** (1/2)

print(f"Square root of {number} after {milliseconds} miliseconds is {ans}")

