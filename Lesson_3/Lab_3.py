students = ['Vasya', 'Kolya', 'Petya', 'Masha', 'Platon']
flats_per_floor = 8
floors = 24

flat_needed = int(input("input number of flat : "))
current_floor = 1
currnet_flats = current_floor
while current_floor <= floors:
    if flat_needed <= current_floor * flats_per_floor:
        ##        print("Floor", current_floor, "appartment found !!")
        print("Floor {} appartment found !!".format(current_floor))
        break
    current_floor += 1
