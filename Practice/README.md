# Exercises

## 1-2 Introduction and Redirection

1. Simple App

   - Add a home page
   - Add a welcome page
   - Add a path parameter to welcome page
   - Add a page 'add' with 2 numerical path parameters which returns the sum of parameters.

2. Dynamic URL

   - Add a page with path parameter 'name' and greets.

3. URL Redirection

   - Add a Home Page
   - Add a score page with two path parameters 'name' (str) and 'marks' (int). If marks < 30 redirect to 'fail' page otherwise 'pass' page.

4. URL Building
   - Add a home page
   - Add 'score' page with redirection to 'fail' and 'pass' pages. The parameters name and marks of score should be send/passed/shared to fail and pass pages.

## 3 Jinja-Inheritence

1. Add a "layout.html" containing the boiler-plot code for inheritence inside the folder "templates"
   - Add a jinja block "content"
   - Add a title variable
2. Create html pages inside the folder "templates"
   - home, about, emp
3. Create a file named emp.py which contains a 4 nested python dictionary. (outside the templates folder)
   Ex:
   ```python
   employees_data = {
    1: {
        "name": "Michael",
        "age": 42,
        "position": "Manager"
    },
   ```
   - import the emp.py data in app.py and pass it to emp.html as a paramter in render_templated() function.
