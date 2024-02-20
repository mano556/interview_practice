# # 1
# import datetime
# currentTime=datetime.datetime.now()
# print(currentTime)
# # 2
# import datetime
# currentTime=datetime.datetime.now().strftime("%d/%m/%y")
# print(currentTime)

# 3
# import datetime
# date1 = datetime.datetime(2023, 12, 31)
# date2 = datetime.datetime(2023, 1, 1)
# difference = date1 - date2
# print("Difference in days:", difference.days)

#4 using time delta and strftime
# import datetime
# currentdate=datetime.datetime.now()
# newdate=currentdate+datetime.timedelta(days=10)
# print("10 days from now : ",newdate.strftime("%d/%m/%y"))

#5 using strptime

import datetime
string_date= "2023-05-15"
ans=datetime.datetime.strptime(string_date,"%Y-%m-%d")
print(ans)













