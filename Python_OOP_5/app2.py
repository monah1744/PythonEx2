import csv


if __name__ == "__main__":
    with open("data/candidates.csv", 'r') as f_read:
        f_dict = csv.DictReader(f_read)
        for i in f_dict:
            print(i.get("Full Name"))
            print(i.get("Email"))
            print(i.get("Technologies").split("|"))
