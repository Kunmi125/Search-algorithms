data = [10, 34, 73, 11, 63, 97, 23, 47, 85, 32]
key = int(input("What key do you want to find: "))

def linear_search(data, key):
    item_found = False
    for i in data:
        if i == key:
            item_found = True
            print("Item found at", data.index(i) + 1)
            break
    if item_found == False:
        print("Item not found")

linear_search(data, key)