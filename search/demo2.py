# import pandas as pd
# sales=[{"account":"prasad","jan":150,"feb":200,"march":400},
#        {"account":"raju","jan":300,"feb":400,"march":500}]
# s=pd.DataFrame(sales)
# print(s)

# import pandas as pd
# sales=[("prasad",150,200,300),
#        ("ravi",150,200,300),
#        ("sudha",150,200,300),
#        ("raju",150,200,300)]
# labels=["accont","jan","feb","mar"]
# w=pd.DataFrame.from_records(sales,columns=labels)
# print(w)
#
# import pandas as pd
# sales={"account":["prasad","ramu","raju","rani"],
#        "jan":[150,200,300,800],
#        "feb":[500,800,900,140]}
# s=pd.DataFrame.from_dict(sales)
# s.to_csv("example.csv")
# print("Done.")


# import pandas as pd
#
# # making data frame from csv file
# data = pd.read_csv("example.csv", index_col="account")
#
# # retrieving rows by iloc method
# row2 = data.iloc[2]
#
# print(row2)



# import pandas as pd
# from datetime import date
#
# import xlrd
# create_date=date.today()
# created_by="prasad"
# footer = [('Created by', [created_by]), ('Created on', [create_date]), ('Version', [1.1])]
#
#
# students={"id":[1,2,3,4,5,6],
#           "name":["prasad","ravi","raju","rani","sudha","geetha"],
#           "age":[23,22,25,32,25,18],
#           "qualification":["MBA","MCA","MBA","MCA","MBA","MBA"]}
# de=pd.DataFrame.from_dict(students)
#
# de.to_excel("student.xls",footer)
# print("Done.")


# s=pd.read_excel("student.xls",index_col="id")
#
# s1=s.iloc[2]
#
# print(s1)
from datetime import date
import pandas as pd
import xlsxwriter
create_date = "{:%m-%d-%Y}".format(date.today())
print(create_date)
created_by="prasad"
footer = [('Created by', [created_by]), ('Created on', [create_date]), ('Version', [1.1])]
students={"id":[1,2,3,4,5,6],
          "name":["prasad","ravi","raju","rani","sudha","geetha"],
          "age":[23,22,25,32,25,18],
          "qualification":["MBA","MCA","MBA","MCA","MBA","MBA"]}
df=pd.DataFrame.from_dict(students)
df_footer=pd.DataFrame.from_items(footer)
writer = pd.ExcelWriter('simple-report2.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
df_footer.to_excel(writer, startrow=6, index=False)
writer.save()



