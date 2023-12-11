import pandas as pd

data=[

    {"name":"sunny","age":27,"city":"bhopal"}
    {"name":"krish","age":37,"city":"bangluru"}
    {"name":"Aadil","age":23,"city":"Anantnag"}

]

df=pd.DataFrame(data)

df.to_csv("data/data.csv",index=False)