import pandas as pd
import numpy as np
# students=["prasad","mani","sekhar"]
# courses=["python","java","php"]
# s=pd.Series(courses,index=students)
# print(s)
# print(s["prasad"])
# print(s["mani"])
# print(pd.DataFrame(students))



#data displaying in table format

university={
    "Courses":["pytthon","django","java","php"],
    "Students":["prasad","mani","sekhar","naidu"],
    "Status":["good","verygood","veryStrong","bad"]
}
s=pd.DataFrame(university)
jobs=["developer","tester","architech","designer"]
age=[23,22,21,20]
s["job"]=jobs
s["age"]=age


a=s.sort_values("Students",ascending=True)
b=s.sort_values("Students",ascending=False)
print(a)
print("-----------------------------------------------------")
print(b)
print("------------------------------------------------------------")
print(s.head())
print("-----------------------------------------------------------")
print(s.tail())


#Custom Indexing
# university={
#     "Courses":["pytthon","django","java","php"],
#     "Students":["prasad","mani","sekhar","naidu"],
#     "Status":["good","verygood","veryStrong","bad"]
# }
# # numbers=[1,2,3,4]
# # s=pd.DataFrame(university,index=numbers)
#
# p=pd.DataFrame(s,columns=["raju","ravi","rani","naidu"])



