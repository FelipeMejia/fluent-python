import time

def normalize_data(number):
    # Wait one second
    time.sleep(1)
    return number

sensor_data = [12, 45, 9, 88, 23]
normalized = [y for x in sensor_data if (y:= normalize_data(x)) > 20]

print(normalized)

if (y := (x := 2) + 3) > 4:
    print(f"x is {x} and y is {y}")

x = 2
if (y := x + 3) > 4:
    print(f"x is {x} and y is {y}")