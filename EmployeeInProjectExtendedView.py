from fastapi import FastAPI,Cookie
from pydantic import BaseModel
import pandas as pd
import json

app = FastAPI()

class Item(BaseModel):

    employeeID        :int


# CREATE COLUMN TABLE "SHARON"."SHARON.Data::Projects.EmployeeInProject" (
#     "ProjectID" NVARCHAR(10) NOT NULL , 
#     "EmpID" NVARCHAR(10) NOT NULL , 
#     "isProjAdmin" TINYINT CS_INT, 
#     "isProjManager" TINYINT CS_INT

# ProjectID,EmpID,isProjAdmin,isProjManager

# CREATE COLUMN TABLE "SHARON"."SHARON.Data::Employee.Employee" (
#     "FirstName" VARCHAR(40), 
#     "LastName" VARCHAR(40), 
#     "Email" NVARCHAR(255), 
#     "EmployeeID" NVARCHAR(10) NOT NULL , 
#     "ManagerID" NVARCHAR(10), 
#     "DateOfBirth" DATE CS_DAYDATE, 
#     "StartWorkAt" DATE CS_DAYDATE, 
#     "LastUpdate" SECONDDATE CS_SECONDDATE, 
#     "CreatedAt" SECONDDATE CS_SECONDDATE, 
#     "EndWorkAt" SECONDDATE CS_SECONDDATE, 
#     "isActive" TINYINT CS_INT, 
#     "IDnumber" NVARCHAR(15), 
#     "defaultProjId" NVARCHAR(10), 
#     "defaultSubProjId" NVARCHAR(10),

# "FirstName", "LastName", "Email", "EmployeeID", "ManagerID", "DateOfBirth", "StartWorkAt", "LastUpdate", "CreatedAt", "EndWorkAt", "isActive", "IDnumber", "defaultProjId", "defaultSubProjId"


@app.get("/EmployeeInProjectExtendedView")
async def EmployeeInProjectExtendedView(item: Item):
    
    # Read files:
    employeeInProject = pd.read_csv('EmployeeInProject.csv')
    employee = pd.read_csv('Employee.csv')
    
    # Filter none active employee:
    employee = employee.loc[employee['isActive'] == 1]
    employeeInProject = employeeInProject.rename(columns={"EmpID": "EmployeeID"})
    
    print(employee)
    print('='*100)
    print(employeeInProject)
    print('='*100)

    employeeJoin = employee.merge(employeeInProject,on='EmployeeID', how='inner')

    print(employeeJoin)
    print(item.employeeID)
    # Filter by api parameters:
    employeeJoin = employeeJoin.loc[employeeJoin['EmployeeID'] == item.employeeID]
    
    jsonStr = employeeJoin.to_json(orient="records")
    print(jsonStr)
    jsonResult = json.loads(jsonStr)

    return jsonResult