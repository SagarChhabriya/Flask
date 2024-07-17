# Flask

## Working of a Web App
  ![image](https://github.com/user-attachments/assets/0a8b7396-ad32-43a7-ac69-17e94656963d)


- How to make a web app?<br>
  - Frameworks<br><br>
- Why to make a web app?<br>
  Exchange of information<br><br>
- __"Exchange of information"__ with what?<br>
  Server<br><br>
- What's server?<br>
  Computer system.<br><br>
- __"Exchange of information"__ how?<br>
  Client -Server Architecture<br>
  HTTP Protocol<br><br>

  

## Flask -Introduction
  - Flask is a web framework mainly used for creating and working with web applications using Python.<br><br>
  - Flask is based on WSGI architecture and supports Jinja.<br><br>

  ![image](https://github.com/user-attachments/assets/bf0df4b0-4bcb-46db-a297-64dfa00d63ef)<br><br>

- What is WSGI? <br>
    - Web Sever Gateway Interface<br>
    - An architecture to follow, for handling requests and responses between client & server.<br><br>
- What is Jinja?<br>
  - Web Template Engine
  - Allows to develop dynamic web pages
  - Support "Template Inheritance"
  - Helps reduce repetitiveness and complexity in web page development.
    


## Prerequisties
1. **Endpoint**: Addresses of webpages <br> 
	Ex:<br>
	https://abc.com/office<br>
	https://abc.com/employee<br>
	https://abc.com/contact<br>
<br><br>

2. **Path Parameters**: Used for accessing a particular resource at an endpoint.<br>
	Ex: Data of an specific employee<br>
	https://abc.com/employee/53464<br>
	Where 53464 is an employee id<br>

<br><br>
   **Query Parameters**: Query parameters are used for filtering the data received from an endpoint.<br>
	Ex: An employee whose department is sales<br>
	https://abc.com/employee?dep=sales<br>
	https://abc.com/employee?dep=sales&loc=chennai<br>
<br><br>

3. **HTTP Methods**: Over the server to perform CRUD Operation<br>
| Methods | Operation|
|---------|----------|
|Post|		C|
|Get |	  R|
|Put |		U|
|Delete|	D|

<br><br>
4. **HTTP Response Codes**: How do we know whether the response was successful or failed.
	
 |Code| Meaning|
 |-----|-------|
|1xx | Informative|
|2xx | Success |
|3xx | Redirection |
|4xx | Client-side error|
|5xx |Server side error|

<br><br>
5. **Basic Understanding of HTML Tags**<br>
  Ex: `HTML` `Head` `Body` 


## Demo

File/Module name: app.py
```python
app = Flask(__name__)
# __name__ is the name of module (File name) python assigned
#Create an endpoint: We will create a decorator: starts with @ and 	write a function for the home page:

@app.route("/") # "/" means our home page
	def home():
		return "Welcome to the home page!"


if __name__ == "__main__":
  app.run(debug=True)

# the debug true will return the logs that what is happening or what are the responses
# The home page refers to the "/" endpoint but what if the user enters something like "/home"?
# do we need to create another page named "/home"? No. We just write another decorator like:

@app.route("/") # "/" means our home page
@app.route("/home")
def home():
  return "Welcome to the home page!"
# For the same function we can have multiple routes
```
