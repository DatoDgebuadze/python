#  Exercise: Accepts Users input date of goal and deadline
# Print's back:
# How much time remains until that deadline

import datetime
print(datetime.datetime.strptime(deadline, "%d/%m/%Y"))

U = input("Sheiyvane mizani da deadline am miznis shesasruleblad\n Aucileblad Gamoyavi : amit\n")
i_list = U.split(":")

mizani = i_list[0]
deadline = i_list[1]

print(i_list)
