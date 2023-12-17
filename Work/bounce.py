# bounce.py
#
# Exercise 1.5

height = 100

bounce = 10

while bounce > 0:
    height = height * 0.6
    print(round(height, 4))
    bounce -= 1