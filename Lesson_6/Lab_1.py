import sys


num_flat = int(input("Enter number of apartment - "))
num_floors = int(input("Enter number of floors - "))
num_flats_per_floor = int(input("Enter number of apartments per floor - "))
current_floor = 1
current_porch = 1
# while num_flat > num_floors*num_flats_per_floor*current_porch:
#     current_porch += 1
# num_flat -= num_floors*num_flats_per_floor*(current_porch-1)
# while current_floor <= num_floors:
#     if num_flat <= current_floor * num_flats_per_floor:
#         print("Porch - ", current_porch, "Floor - ",
#               current_floor, " appartment found !!")
#         break
#     current_floor += 1

while num_flat > current_floor * num_flats_per_floor:
    current_floor += 1
print("porch - ", current_floor//(num_floors) if not current_floor %
      (num_floors) else current_floor//(num_floors)+1)
print("floor - ", current_floor % num_floors if current_floor %
      num_floors else num_floors)
