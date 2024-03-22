'''
Author: Edward Drobnis
Date: March 19, 2024
Title: Object Height
Description: Calculates the user-inputted height of an object
'''

time = float(input("Enter a time less than 4.5 seconds: "))

height = 100 - (4.9 * (time ** 2))

print("The height of the object is", '{:.2f}'.format(height), "meters")