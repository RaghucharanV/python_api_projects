## This is a Restful api using python

>A REST API (also called a RESTful API or RESTful web API) is an application programming interface (API) that conforms to the design principles of the representational state transfer (REST) architectural style. REST APIs provide a flexible, lightweight way to integrate applications and to connect components in microservices architectures.(source IBM)

### How REST APIs work

>REST APIs communicate through HTTP requests to perform standard database functions like creating, reading, updating and deleting records (also known as CRUD) within 
 a resource.

>For example, a REST API would use a GET request to retrieve a record. A POST request creates a new record. A PUT request updates a record, and a DELETE request 
 deletes one. All HTTP methods can be used in API calls. A well-designed REST API is similar to a website running in a web browser with built-in HTTP functionality.

>The state of a resource at any particular instant, or timestamp, is known as the resource representation. This information can be delivered to a client in virtually 
 any format including JavaScript Object Notation (JSON), HTML, XLT, Python, PHP or plain text. JSON is popular because it’s readable by both humans and machines—and 
 it is programming language-agnostic.(source IBM)

## About FastAPI app:
This an API build using FASTAPI Library, copy the file or clone the file

Run this in terminal:

```bash
  uvicorn fastapi:app --reload

```

## How api works:
> After api reloaded then use ["https:localhost/docs"] to open docs, You can check each employee's details by ["https:localhost/employee/2"] (to get details of second employee)



![Screenshot (1022)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/0219d149-dc7a-45d0-aa36-297d31782727)






![Screenshot (1025)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/46e80847-c645-4800-a4e4-a87d6c943c55)




> To search or filter employee based on salary, name you can do by [https:localhost/search?salary=75000&name=A]


![Screenshot (1023)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/e7d779c6-d7f4-4554-8f0f-c9ac3d13aeff)




![Screenshot (1026)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/46eadad6-dcf7-4298-bdce-25124d0aa990)




![Screenshot (1027)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/ddb100b0-6879-45c5-9073-c7f1b4cc414b)






>To add an employee you can do by using ["https:localhost/addEmployee"] and also by Docs ["https:localhost/docs"]


![Screenshot (1024)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/c22ac28a-99e2-4d6c-bce5-20c928710b16)






>To Change an employee you can do by using ["https:localhost/addChange"] and also by Docs ["https:localhost/docs"]




![Screenshot (1028)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/1c8e44f8-a439-45f9-ac6d-e918d47a08ec)







> To delete an employee you can do by using ["https:localhost/deleteEmployee"] and also by Docs ["https:localhost/docs"]




![Screenshot (1029)](https://github.com/RaghucharanV/python_api_projects/assets/81848656/ac4e05ec-5363-4209-bf7d-eec219b20123)








## FastApi Advantages

> Easy to build any API and it provide full documentation automatically

>Reduced number of bugs: It reduces the possibility for human-induced errors.

>Standards-based: It’s based on the open standards for APIs, OpenAPI and JSON Schema.

>Fast to run: It offers very high performance, on par with NodeJS and Go.


