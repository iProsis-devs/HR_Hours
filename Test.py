
# pylint: disable=no-name-in-module

# pylint: disable=no-self-argument

## Namer's encryption/decription program is called ZKN_CALL_DECRYPTION_API

from fastapi import FastAPI,Cookie

from pydantic import BaseModel
import pandas as pd

import os
import base64

from base64 import b64decode, b64encode

# from Crypto.Cipher import AES, PKCS1_OAEP

# from Cryptodome.Util.Padding import pad, unpad

 

app = FastAPI()

# key = os.environ.get('KEY')
key = "12345678901234567890123456789012" # for testing
 

class Item(BaseModel):

    ProjID        :str
    ProjName      :str
    ProjectType   :str
    isFixed       :int
    includeLunch  :int
    parentProj    :str
    color         :str
    isBillable    :int
    isDefault     :int
    isActive      :int

# {
#  "ProjID"      :"214",
#  "ProjName"    :"Machine Learning",
#  "ProjectType" :"null",
#  "isFixed"     :0,
#  "includeLunch":1,
#  "parentProj"  :"181",
#  "color"       :"gray",
#  "isBillable"  :0,
#  "isDefault"   :1,
#  "isActive"    :1
# }


# def decryptInput(data):

#     # with open(encryptionParameters["keyFile"]) as jsonFile:  keyFile = json.load(jsonFile)
#     # session_key = bytes(keyFile["key"], 'utf-8')      #32Byte

#     session_key = key

#     decipher = AES.new(session_key, AES.MODE_ECB)
#     return unpad(decipher.decrypt(b64decode(data)), 32).decode("iso-8859-8")
    

# def encryptInput(data):
#     # with open(encryptionParameters["keyFile"]) as jsonFile:  keyFile = json.load(jsonFile)
# 	# session_key = bytes(keyFile["key"], 'utf-8')      #32Byte

#     session_key = key
#     cipher_ecb = AES.new(session_key, AES.MODE_ECB)
    
# 	# msg = cipher_ecb.encrypt(pad(str(input).encode('ascii'), 32))
# 	# msg = cipher_ecb.encrypt(pad(str(input).encode('ISO-8859-8'), 32))

#     msg = cipher_ecb.encrypt(pad(str(data).encode('iso-8859-8'), 32))
#     return base64.b64encode(msg).decode('iso-8859-8')


# @app.post("/decrypt")


# async def create_decryption(item: Item):

#     return "decryptInput(item.data)"


# @app.post("/encrypt")

# async def create_encryption(item: Item):

#     return {"data": "encryptInput(item.data)"}


@app.post("/holidays")

async def holidays(item: Item):

    print(item.data)
    df1 = pd.read_csv ('Holidays.csv')
    df2 = pd.read_csv ('Holidays.csv')

    df1 = df1.merge(df2,on='Date')
    # print(df2)
    jsonStr = df2.head(1).to_json()
    print(type(jsonStr))
    return jsonStr

@app.post("/Projects")
async def Projects(item: Item):

    # print(item)

    df = pd.read_csv('Projects_test.csv')   #.head(3)
    print(df)
    print('='*100)
    
    # Check fey found:
    print('Find: ', df.loc[df['ProjID'] == item.ProjID].size)

    if df.loc[df['ProjID'] == item.ProjID].size > 0:
        return { "msg": "Key found can't insert row"}
    else:

        print('='*100)
        # a_row = pd.Series()

        row_df = pd.DataFrame([[
            item.ProjID,      
            item.ProjName,
            item.ProjectType, 
            item.isFixed,     
            item.includeLunch,
            item.parentProj,  
            item.color,       
            item.isBillable,  
            item.isDefault,   
            item.isActive]]
            , columns=['ProjID','ProjName','ProjectType','isFixed','includeLunch','parentProj','color','isBillable','isDefault','isActive'])

        print(row_df)
        print('='*100)

        df = pd.concat( [df, row_df])
        
        print(df)
        df.to_csv('Projects_test.csv', index=False)
        return item

@app.put("/Projects")
async def Projects(item: Item):

    # print(item)

    df = pd.read_csv('Projects_test.csv')   #.head(3)
    print(df)
    print('='*100)
    
    # Check fey found:
    print('Find: ', df.loc[df['ProjID'] == item.ProjID].size)

    if df.loc[df['ProjID'] == item.ProjID].size == 0:
        return { "msg": "Key Not found can't update row"}
    else:
        print('='*100)
        # a_row = pd.Series()

        df.drop(df.loc[df['ProjID'] == item.ProjID].index, inplace=True)

        row_df = pd.DataFrame([[
            item.ProjID,
            item.ProjName,
            item.ProjectType,
            item.isFixed,
            item.includeLunch,
            item.parentProj,
            item.color,
            item.isBillable,
            item.isDefault,
            item.isActive]]
            , columns=['ProjID','ProjName','ProjectType','isFixed','includeLunch','parentProj','color','isBillable','isDefault','isActive'])

        print(row_df)
        print('='*100)

        df = pd.concat( [df, row_df])
        
        print(df)
        df.to_csv('Projects_test.csv', index=False)
        return { "msg": "row updated"}

@app.delete("/Projects")
async def Projects(item: Item):

    # print(item)

    df = pd.read_csv('Projects_test.csv')   #.head(3)
    print(df)
    print('='*100)
    
    # Check fey found:
    print('Find: ', df.loc[df['ProjID'] == item.ProjID].size)

    if df.loc[df['ProjID'] == item.ProjID].size == 0:
        return { "msg": "Key Not found can't update row"}
    else:
        print('='*100)
        # a_row = pd.Series()

        df.drop(df.loc[df['ProjID'] == item.ProjID].index, inplace=True)
        df.to_csv('Projects_test.csv', index=False)

        return { "msg": "row deleted"}




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
    
    employeeInProject = pd.read_csv('EmployeeInProject.csv')
    employee = pd.read_csv('Employee.csv')
    
    print(employeeInProject)
    print('='*100)
    print(employee)

    # df1 = df1.merge(df2,on='Date')

    return { "msg": "row"}