from flask import Flask, request, jsonify
import sqlite3
app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("books.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn


@app.route("/books", methods=["GET","POST"])
# view function
def books():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        conn = db_connection()
        cursor = conn.cursor("SELECT * FROM book")
    
        books = [
            dict(id=row[0],author=row[1],language=row[2],title=row[3])
            for row in cursor.fetchall()
        ]
    
        if books is not None:
            return jsonify(books)
        
    if request.method=="POST":
        new_author = request.form['author']
        new_lang   = request.form['language']
        new_title  = request.form['title']
        sql = """INSERT INTO book(author, language, title) VALUES (?, ?, ?)"""

        cursor = cursor.execute(sql,(new_author,new_lang,new_title))
        conn.commit()

        return f"Book with the id: {cursor.lastrowid} added successfully."    


# # GET | PUT | DELETE
# # Note: Previous route is books
# @app.route("/book/<int:id>",methods=["GET","PUT","DELETE"])
# def single_book(id):
#     if request.method=="GET":
#         for book in books_list:
#             if book['id']==id:
#                 return jsonify(book)
            

#     if request.method=='PUT':
#         for book in books_list:
#             if book['id']==id:
#                 book['author']=request.form['author']
#                 book['language']=request.form['language']
#                 book['title']=request.form['title']
#                 updated_book = {
#                     'id':id,
#                     'author':book['author'],
#                     'language':book['language'],
#                     'title':book['title'],
#                 }        
#                 return jsonify(updated_book)
            
#     if request.method == "DELETE":
#          for index, book in enumerate(books_list):
#              if book['id']==id:
#                  books_list.pop(index)
#                  return jsonify(books_list)
    
if __name__=="__main__":
    app.run(debug=True)

# Step1: After writing the code to handle post request and the code for creating table in db.py
# Execute the app.py (if required db.py) you will get a file named 'books.sqlite'
# Step2: Data Grip > New|Exisiting Project > Data Source > paste the path of books.sqlite > done



# copy the link and move towards postman
# POST > Body > form-data> Key values> send> Yep! All done!


