from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float

app = FastAPI()


#Get request
#Logic can be anything, for application we fetch all the data from database and just return it
@app.get("/getdata")
async def read_root():
    return {"1" : "World"}

#Post Request
#for parameterize endpoint make sure to pass it as parameter in same function
#If we are pushing an item or object directly create class inherited by BaseModel, it's like pushing data in form of JSON object like NODEJS
#Here `item` represent that this is object which will be send from user side
#NODEJS SYNTAX:
# {name, price} = req.body
@app.post("/api/{item_id}")
async def push_data(item_id: int ,item: Item):
    return {"itemid": item_id, "item_detail": item}


#Get specific data from database
#Here _id is paramterize key, it is possible to define it's datatype
#If in function arg we write (_id: int) This makes that arg will be int only. Similarly for str
#If in function arg we write just (_id) then it can be anything, typically str or int or boolean value
@app.get("/api/getitem/{_id}")
async def get_item(_id):
    #Dummy data
    productList = {"PROA1":Item(name="Soap", price=102), "PROA2":Item(name="Sabun", price=120)}
    if(productList.__contains__(_id)):
        return productList[_id]
    else:
        return "No Such Item Exists"


#Patch/Put Request
@app.put("/api/patchitem/{_id}")
async def get_item(_id, newItem: Item):
    #Dummy data
    productList = {"PROA1":Item(name="Soap", price=102), "PROA2":Item(name="Sabun", price=120)}
    if(productList.__contains__(_id)):
        preItem = productList[_id]
        productList.update({_id:newItem})
        new_item = productList[_id]
        return {"oldvalue": preItem, "newvalue": new_item}
    else:
        return "No Such Item Exists"
    