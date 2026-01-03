from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name:str='nitish' #default value for pydantic
    age:Optional[int]=None

good_student={"name":"dhruv"}
bad_student={"name":123}
default_student={}

s1=Student(**good_student)
# s2=Student(**bad_student) #this will generate error
s3=Student(**default_student)

print(s1)
