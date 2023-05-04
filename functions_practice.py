def hello():
    print("Hello user!")

hello()


  
def pack(shirt, belt, watch):
    return [shirt, belt, watch]

pack_list = pack("nike", "reebok", "gucci")

print(pack_list)




# def eat_lunch():
#     prints(["First I eat   ", "Next I eat   ","Make lunchbox is empty!"])


def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_items)):
            if i == 0:
             print(f"First I eat {lunch_items[0]}")
            else:  
              print(f"Next I eat {lunch_items[1]}") 

eat_lunch([" a burger", "fries", "nuggets"])
