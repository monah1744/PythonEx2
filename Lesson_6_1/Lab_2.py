dict_of_sizes = {"1": "talia", "2": "bedra", "3": "INT",
                 "4": "RU", "5": "GER", "6": "USA", "7": "FR", "8": "GB"}
pre_tables_of_size = {}
pre_tables_of_size["Pre"] = {"1": None, "2": None, "3": None,
                             "4": None, "5": None, "6": None, "7": None, "8": None}
pre_tables_of_size["Pre"]["1"] = {"talia": "63-65", "bedra": "89-92", "INT": "XXS",
                                  "RU": "42", "GER": "36", "USA": "8", "FR": "38", "GB": "24"}
pre_tables_of_size["Pre"]["2"] = {"talia": "66-69", "bedra": "93-96", "INT": "XS",
                                  "RU": "44", "GER": "38", "USA": "10", "FR": "40", "GB": "26"}
pre_tables_of_size["Pre"]["3"] = {"talia": "70-74", "bedra": "97-101", "INT": "S",
                                  "RU": "46", "GER": "40", "USA": "12", "FR": "42", "GB": "28"}
pre_tables_of_size["Pre"]["4"] = {"talia": "75-78", "bedra": "102-104", "INT": "M",
                                  "RU": "48", "GER": "42", "USA": "14", "FR": "44", "GB": "30"}
pre_tables_of_size["Pre"]["5"] = {"talia": "79-83", "bedra": "105-108", "INT": "L",
                                  "RU": "50", "GER": "44", "USA": "16", "FR": "46", "GB": "32"}
pre_tables_of_size["Pre"]["6"] = {"talia": "84-89", "bedra": "109-112", "INT": "XL",
                                  "RU": "52", "GER": "46", "USA": "18", "FR": "48", "GB": "34"}
pre_tables_of_size["Pre"]["7"] = {"talia": "90-94", "bedra": "113-117", "INT": "XXL",
                                  "RU": "54", "GER": "48", "USA": "20", "FR": "50", "GB": "36"}
pre_tables_of_size["Pre"]["8"] = {"talia": "95-97", "bedra": "118-122", "INT": "XXXL",
                                  "RU": "56", "GER": "50", "USA": "22", "FR": "52", "GB": "38"}


def prepare_dict(k_size):
    return {kvalue[dict_of_sizes[k_size]]: kvalue for new_value in pre_tables_of_size.values() for kvalue in new_value.values(
    )}


known_size = input("Which kind of size do you know? : \n 1 - Talia. \n 2 - Bedra. \n 3 - International \n 4 - Russia. \n 5 - Germany \n 6 - USA \n 7 - France \n 8 - Great Britain \n Make a choice : ")

current_dict = prepare_dict(known_size)
dict_your_choise = dict(
    zip(range(1, len(current_dict)+1), current_dict.keys()))
[print(kkey, kvalue) for kkey, kvalue in dict_your_choise.items()]
your_size = input("\nPlease, choose your size : ")
which_size = input("Which kind of size do you want look at? : \n 1 - Talia. \n 2 - Bedra. \n 3 - International \n 4 - Russia. \n 5 - Germany \n 6 - USA \n 7 - France \n 8 - Great Britain \n Make a choice : ")
print("\nYour size - ", dict_your_choise[int(your_size)], ";\nYou want to look at - ", dict_of_sizes[which_size],
      "\nConverted size - ", current_dict[dict_your_choise[int(your_size)]][dict_of_sizes[which_size]], "...")
