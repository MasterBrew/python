import random

feet_in_miles = 5280
meter_in_kilometer = 1000
beateles = ["John Lenon", "Paul McCardney", "George Harrison", "Ringo Star"]

def get_file_ext(filename):
    return filename[filename.index(".")+1]

def roll_dice(num):
    return random.randint(1, num)

