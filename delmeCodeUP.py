import json

# Name the data
d = json.load(open('profiles.json')) 

# 3a. Total number of users = 19
count_users = len(set([user["_id"] for user in d]))

# 3b. Number of active users = 9
active_users = len([user["isActive"] for user in d if user["isActive"] == True])

# 3c. Number of inactive users = 10
inactive_users = len([user["isActive"] for user in d if user["isActive"] == False])

# 3d. Grand total of balances for all users = $52667.02
Grand_total_balance = sum([int(round(float(user["balance"].replace("$","").replace(",",""))*100)) for user in d ]) / 100

# 3e. Average balance per user
Average_balance_per_user = round((Grand_total_balance / count_users), 2)

# 3f. User with the lowest balance
lowest_balance = min([user["balance"] for user in d ])
lowest_balance_user = [x["name"] for x in d if x["balance"] == lowest_balance]

# 3g. User with the highest balance
highest_balance = max([user["balance"] for user in d ])
highest_balance_user = [x["name"] for x in d if x["balance"] == highest_balance]

# 3h. Most common favorite fruit = strawberry = 9
# def Most_common_favorite_fruit():
#     fruits = list(set([x["favoriteFruit"] for x in d]))
#     fav_fruits = [x["favoriteFruit"] for x in d]
#     i=-1
#     for fruit in fruits:
#         i += 1
#         print(f" {fruit} = {(fav_fruits.count(fruits[i]))}")
# print(Most_common_favorite_fruit())        
#print(Most_common_favorite_fruit())

def Most_common_favorite_fruit():
    fruits = list(set([x["favoriteFruit"] for x in d]))
    fav_fruits = [x["favoriteFruit"] for x in d]
    i=-1
    f = []
    for fruit in fruits:
        i += 1
        f.append((fav_fruits.count(fruits[i]), fruit))
    return max(f)
 
# 3i. Least most common favorite fruit
def Least_common_favorite_fruit():
    fruits = list(set([x["favoriteFruit"] for x in d]))
    fav_fruits = [x["favoriteFruit"] for x in d]
    i=-1
    f = []
    for fruit in fruits:
        i += 1
        f.append((fav_fruits.count(fruits[i]), fruit))
    return min(f)

print(Least_common_favorite_fruit())
# 3j. Total number of unread messages for all users = 210
# greetings = [user["greeting"] for user in d]
# numbers = sum([int(word) for str_ in greetings for word in str_.split() if word.isdigit()])

# for str_ in greetings:
#     for word in str_.split():
#         if word.isdigit():
#             numbers.append(int(word))
        
