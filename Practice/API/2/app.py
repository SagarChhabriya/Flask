from flask import Flask, request, jsonify

app = Flask(__name__)

# List of books
books_list = [
    {
        "id":0,
        "author":"Chinua Acehebe",
        "language":"English",
        "title": "Things Fall Apart",
    },
    {
        "id":1,
        "author":"Hans Christian Andersen",
        "language":"Danish",
        "title": "Fairy tales",
    },
    {
        "id":2,
        "author":"Samuel Beckett",
        "language":"French, English",
        "title": "Molloy, Malone Dies, The Unnamble, the trilogy",
    },
    {
        "id":3,
        "author":"Giovanni Boccaccio",
        "language":"Italian",
        "title": "The Decameron",
    },
    {
        "id":6,
        "author":"Jorge Luis Borges",
        "language":"Spanish",
        "title": "Ficciones",
    },
    {
        "id":5,
        "author":"Emily Bront",
        "language":"English",
        "title": "Wuthering Heights",
    },

]


@app.route("/books", methods=["GET","POST"])
# view function
def books():
    if request.method == "GET":
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            return "Nothing Found",404
        
    if request.method=="POST":
        new_author = request.form['author']
        new_lang   = request.form['language']
        new_title  = request.form['title']
        # get the last dictionary/record, fetch the id, add 1 and assign to new id (iD)
        iD = books_list[-1]['id']+1

        # create a new object (i.e., record)
        new_obj = {
            'id':iD,
            'author':new_author,
            'language':new_lang,
            'title':new_title,
        }
        # add to the existing in memory list (runtime database: in memory list)
        books_list.append(new_obj)

        # return the updated list/in memory db in the form of json
        return jsonify(books_list), 201
    

# GET | PUT | DELETE
# Note: Previous route is books
@app.route("/book/<int:id>",methods=["GET","PUT","DELETE"])
def single_book(id):
    if request.method=="GET":
        for book in books_list:
            if book['id']==id:
                return jsonify(book)
            

    if request.method=='PUT':
        for book in books_list:
            if book['id']==id:
                book['author']=request.form['author']
                book['language']=request.form['language']
                book['title']=request.form['title']
                updated_book = {
                    'id':id,
                    'author':book['author'],
                    'language':book['language'],
                    'title':book['title'],
                }        
                return jsonify(updated_book)
            
    if request.method == "DELETE":
         for index, book in enumerate(books_list):
             if book['id']==id:
                 books_list.pop(index)
                 return jsonify(books_list)
    
if __name__=="__main__":
    app.run(debug=True)

# copy the link and move towards postman
# POST > Body > form-data> Key values> send> Yep! All done!


