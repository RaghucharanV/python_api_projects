#imports
from fastapi import FastAPI,Query,HTTPException
from pydantic import BaseModel
from typing import Optional
import json
#fastapi constructor
app  = FastAPI()

#main page
@app.get('/')
def appopen():
    return "This is Restful api using Fastapi: Navigate to do restful tasks using /addperson, /deleteperson, /search, /changeperson"

#base class
class Person(BaseModel):
    id:Optional[int]= None
    name: str
    position:str
    department:str
    salary:str

#read json file
with open('people.json', 'r') as f:
    people = json.load(f)['people']


#get persons details using id
@app.get('/person/{p_id}',status_code=200)
def get_person(p_id:int):
    person = [p for p in people if p['id']==p_id]
    return person[0] if len(person) >0 else {}


#search and filter employes based on Salary and name
@app.get("/search", status_code=200)
def search_person(salary:Optional[int]=Query(None,title="Salary",description="salary filter"),
                  name:Optional[str]=Query(None,title="Name",description="Name filter")):
    people1 = [p for p in people if p['salary']==salary]

    if name is None:
        if salary is None:
            return people
        else:
            return people1
    else:
        people2 = [p for p in people if name.lower() in p['name'].lower()]
        if salary is None:
            return people2
        else:
            combined = [p for p in people1 if p in people2]
            return combined
        

#Add employee to json file 
@app.post('/addEmployee',status_code=201)
def add_person(person:Person):
    p_id = max([p['id'] for p in people])+1
    new_person = {
        'id':p_id,
        'name': person.name,
        'position': person.position,
        'department': person.department,
        'salary': person.salary

    }

    people.append(new_person)

    with open('people.json', 'w') as f:
        json.dump(people,f)


#Change employee details
@app.put('/changeEmployee', status_code=204)
def change_person(person:Person):
    new_person = {
        'id':person.id,
        'name': person.name,
        'position': person.position,
        'department': person.department,
        'salary': person.salary
    }

    person_list = [p for p in people if p['id'] == person.id]
    if len(person_list)>0:
        people.remove(person_list[0])
        people.append(new_person)
        with open('people.json','w') as f:
            json.dump(people,f)
    else:
        return HTTPException(status_code=404,detail=f"Person with id {person.id} does not exists.")
    

#delete empolyee details using id.
@app.delete('/deleteEmployee/{p_id}',status_code=204)
def delete_person(p_id:int):
    person = [p for p in people if p['id']==p_id]
    if len(person)>0:
        people.remove(person[0])
        with open('people.json','w') as f:
            json.dump(people, f)
    else:
        raise HTTPException(status_code=404, detail=f"There is no person id")
