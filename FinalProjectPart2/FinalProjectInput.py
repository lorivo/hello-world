# Lori Vo 1852113
# Final Project for CIS 2348

from datetime import date
import datetime
# print(date.today())
today = date.today()
# print(today)
year = today.year
# print(year)
month = today.month
# print(month)
day = today.day
# print(day)


# reads given lists and adds to dictionary
man_name = "ManufacturerList.csv"
price_name = "PriceList.csv"
SD_name = "ServiceDatesList.csv"

data_dictionary = {}
try:
    man_file = open(man_name)
    for line in man_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        data_dictionary[temp[0]] = temp[1:]
    man_file.close()
#    print(data_dictionary)

    price_file = open(price_name)
    for line in price_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        string1 = temp[1]  # makes text on file a string instead of list
        data_dictionary[temp[0]].append(string1)
    price_file.close()
#    print(data_dictionary)

    SD_file = open(SD_name)
    for line in SD_file.readlines():
        line = line.strip()
        temp = line.split(',')
#        print(temp)
        string2 = temp[1]  # information that will be appended into a string and not a list
        data_dictionary[temp[0]].append(string2)
    SD_file.close()
#    print(data_dictionary)

except:
    print("Error reading file or gathering data")

# writes Full Inventory!!!
of = open('FullInventory.csv', 'w')

# creates sorted dictionary for output part a
sorted_man = {}
sorted_names = sorted(data_dictionary.values())
# sorts the dictionary into new dictionary
for i in sorted_names:
    for k in data_dictionary.keys():
        if data_dictionary[k] == i:
            sorted_man[k] = (data_dictionary[k])
# print(sorted_man)

manufacturer_names = []
item_types = []

for n in sorted_man:
    value1 = n  # ID
    value2 = data_dictionary[n][0]  # Manufacturer
    value3 = data_dictionary[n][1]  # Item type
    value4 = data_dictionary[n][3]  # Price
    value5 = data_dictionary[n][4]  # Service date
    value6 = data_dictionary[n][2]  # if damaged

    # adding into manufacturer list and item types list
    if data_dictionary[n][0] not in manufacturer_names:
        manufacturer_names.append(data_dictionary[n][0])
    if data_dictionary[n][1] not in item_types:
        item_types.append(data_dictionary[n][1])

    of.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
    of.write('\n')
#    print(n)
of.close()

# print(manufacturer_names)
# print(item_types)


# inventory type list!!! part b of output

# sorts by item ID
sort_ID = dict(sorted(data_dictionary.items()))
# print(sort_ID)
# print()

# item_type = ""  # empty string for item type to change later in the code
# this for loop method is only perfect when the file item inventories don't already exist


for f in sort_ID:
    item_type = sort_ID[f][1]
    op = open(item_type + "Inventory.csv", 'w')
    for u in sort_ID:
        temp_item = sort_ID[u][1]
        if item_type == temp_item:  # is item file exists or not
            op = open(item_type + "Inventory.csv", 'a')   # appends to previous file instead of creating a new one
            value1 = u  # ID
            value2 = sort_ID[u][0]  # Manufacturer
            value3 = sort_ID[u][1]  # Item type
            value4 = sort_ID[u][3]  # Price
            value5 = sort_ID[u][4]  # Service date
            value6 = sort_ID[u][2]  # if damaged
            op.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
            op.write('\n')
            op.close()
        else:   # if item doesn't exist
            continue
    op.close()

# writes damage inventory file!!
# converts price information to int so I could sort from greatest to least
for n in data_dictionary:
    data_dictionary[n][3] = int(data_dictionary[n][3])
# print(data_dictionary)

# new dictionary that sorts from greatest to least
# reverse is used bc the function without it makes it least to greatest
price_sort = dict(sorted(data_dictionary.items(), key=lambda data_dictionary: data_dictionary[1][3], reverse=True))
# print(price_sort)

os = open('DamagedInventory.csv', 'w')

for e in price_sort:
    if price_sort[e][2] == 'damaged':
        value1 = e  # ID
        value2 = data_dictionary[e][0]  # Manufacturer
        value3 = data_dictionary[e][1]  # Item type
        value4 = data_dictionary[e][3]  # Price
        value5 = data_dictionary[e][4]  # Service date
        os.write("{}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5))
        os.write('\n')
os.close()

# part c of output!!! past service date inventory file!!

for r in sorted_man:  # using sorted_man so it's easier to see if dates are right using full inventory csv
    string_date = sorted_man[r][4]
    example = datetime.datetime.strptime(string_date, '%m/%d/%Y')
#    print(example.date())
    sorted_man[r][4] = example.date()
# print(sorted_man)

sorted_date = dict(sorted(sorted_man.items(), key=lambda sorted_man: sorted_man[1][4]))
# print(sorted_date)
# for k in sorted_date:
#    print(sorted_date[k][4])

od = open('PastServiceDateInventory.csv', 'w')
for item in sorted_date:
    item_year = sorted_date[item][4].year
    item_month = sorted_date[item][4].month
    item_day = sorted_date[item][4].day

    value1 = item  # ID
    value2 = sorted_date[item][0]  # Manufacturer
    value3 = sorted_date[item][1]  # Item type
    value4 = sorted_date[item][3]  # Price
    value5 = (str(item_month)+'/'+str(item_day)+'/'+str(item_year))  # Service date
    value6 = sorted_date[item][2]  # if damaged
    if item_year < year:
        od.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
        od.write('\n')
    elif item_year == year:
        if item_month < month:
            od.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
            od.write('\n')
        elif item_month == month:
            if item_day < day:
                od.write("{}, {}, {}, {}, {}, {}".format(value1, value2, value3, value4, value5, value6))
                od.write('\n')
    else:
        continue
od.close()

if __name__ == "__main__":
    print("Please enter the manufacturer and item type of the item you want or 'q' to exit: ")
    user_input = input().split(' ')
    while user_input[0] != 'q':
        item_name_match = 0
        item_type_match = 0
        manufacturer_name = ''
        item_type = ''
        highest_price = 0
        item_ID = ''
        item_price = 0
        item_ID2 = ''
        manufacturer_name2 = ''
        item_price2 = 0
        price_difference = 0
        smallest_price_difference = 10000000000000000

        for word in user_input:
            # print(word)
            for name in manufacturer_names:
                # print(name)
                if word == name:
                    print("Item manufacturer found")
                    temp_name = name
                    item_name_match = 1
                    manufacturer_name = name
            for type_1 in item_types:
                if word == type_1:
                    print("Item type found")
                    temp_type = type_1
                    item_type_match = 1
                    item_type = type_1
        if item_name_match == 0 or item_type_match == 0:
            print('No such item in inventory')

    # priority order: manufacturer/item type, damaged/service date, highest price
        for items in sorted_man:
            item_year = sorted_date[items][4].year
            item_month = sorted_date[items][4].month
            item_day = sorted_date[items][4].day
            if manufacturer_name == data_dictionary[items][0] and item_type == data_dictionary[items][1]:
                # makes sure manufacturer name and item types are matching
                if data_dictionary[items][2] == '':
                    # make sure item isn't damaged
                    if item_year > year:
                        # similar code to past service date but changing it so dates are after given date
                        if data_dictionary[items][3] > highest_price:
                            # getting highest priced item
                            highest_price = data_dictionary[items][3]
                            item_ID = items  # ID
                            item_price = data_dictionary[items][3]  # Price
                    elif item_year == year:
                        if item_month > month:
                            if data_dictionary[items][3] > highest_price:
                                # getting highest priced item
                                highest_price = data_dictionary[items][3]
                                item_ID = items  # ID
                                item_price = data_dictionary[items][3]  # Price
                        elif item_month == month:
                            if item_day > day:
                                if data_dictionary[items][3] > highest_price:
                                    # getting highest priced item
                                    highest_price = data_dictionary[items][3]
                                    item_ID = items  # ID
                                    item_price = data_dictionary[items][3]  # Price

        if item_name_match == 1 and item_type_match == 1:
            if highest_price == 0:
                print()
                print("The item you're looking for is damaged or past its service date")
            else:
                print()
                print('Your item is:')
                print("{}: {} {}, ${}".format(item_ID, manufacturer_name, item_type, item_price))

    # for alternative item option
        for items in sorted_man:
            item_year = sorted_date[items][4].year
            item_month = sorted_date[items][4].month
            item_day = sorted_date[items][4].day
            price_difference = item_price - int(data_dictionary[items][3])
            if manufacturer_name != data_dictionary[items][0] and item_type == data_dictionary[items][1]:
                # makes sure manufacturer name is different and item types are matching
                if data_dictionary[items][2] == '':
                    # make sure item isn't damaged
                    if item_year > year:
                        # similar code to past service date but changing it so dates are after given date
                        if smallest_price_difference > price_difference:
                            smallest_price_difference = price_difference
                            item_ID2 = items  # ID
                            item_price2 = data_dictionary[items][3]  # Price
                            manufacturer_name2 = data_dictionary[items][0]  # manufacturer name
                    elif item_year == year:
                        if item_month > month:
                            if smallest_price_difference > price_difference:
                                smallest_price_difference = price_difference
                                item_ID2 = items  # ID
                                item_price2 = data_dictionary[items][3]  # Price
                                manufacturer_name2 = data_dictionary[items][0]  # manufacturer name
                        elif item_month == month:
                            if item_day > day:
                                if smallest_price_difference > price_difference:
                                    smallest_price_difference = price_difference
                                    item_ID2 = items  # ID
                                    item_price2 = data_dictionary[items][3]  # Price
                                    manufacturer_name2 = data_dictionary[items][0]  # manufacturer name

        if item_type_match == 1:
            if item_ID2 == '':
                print()
                print("There are no alternative options.")
                print()
            else:
                print()
                print('You may also consider:')
                print("{}: {} {}, ${}".format(item_ID2, manufacturer_name2, item_type, item_price2))
                print()

        print("Please enter the manufacturer and item type of the item you want or 'q' to exit: ")
        user_input = input().split(' ')
        if user_input[0] == 'q':
            break
