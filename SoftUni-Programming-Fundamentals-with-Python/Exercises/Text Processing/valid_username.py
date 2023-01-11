username = input().split(', ')
for users in username:
    if 3 <= len(users) < 16 :
        # if users.__contains__("-") or users.__contains__("_"):
        if users.isalnum() or users.__contains__("-") or users.__contains__("_"):
            print(users)