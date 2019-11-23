journal = dict([("Ivanov", [3, 2, 3, 5, 5]), ("Petrov", [1, 2, 3, 4, 5]), ("Sidorov", [1, 2, 3, 4, 5]),
                ("Shmatko", [1, 2, 3, 4, 5]), ("Novikov", [1, 2, 2, 2, 5]), ("Laktionov", [1, 2, 3, 4, 5])])
avg_min_1 = 5
avg_min_2 = ""
avg_max_1 = 0
avg_max_2 = ""
for i in journal.keys():
    if sum(journal[i])/len(journal[i]) >= avg_max_1:
        avg_max_1 = sum(journal[i])/len(journal[i])
        avg_max_2 = i
    if sum(journal[i])/len(journal[i]) <= avg_min_1:
        avg_min_1 = sum(journal[i])/len(journal[i])
        avg_min_2 = i
print("Bad - ", avg_min_2, " - ", avg_min_1)
print("Smart - ", avg_max_2, " - ", avg_max_1)
