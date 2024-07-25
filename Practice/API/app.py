# Flask App Routing

from flask import Flask, request, render_template, jsonify

# Create a simple flask application
app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome!"

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to the Index Page"


# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    return "The Person has passed and the score is: "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is: "+str(score)

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("form.html")
    else:
        maths   = float(request.form["maths"])
        science = float(request.form["science"])
        history = float(request.form["history"])

        average_marks = (maths+science+history)/3
        return render_template("form.html",score=average_marks)
    
@app.route("/api",methods=["POST"])
def calculate_sum():
    data = request.get_json()
    a_val = float(dict(data)['a'])
    b_val = float(dict(data)['b'])
    return jsonify(a_val+b_val)

# Run Postman > paste url: 'http://127.0.0.1:5000/api' > select POST from drop down menu > body > raw > JSON> then paste
# {
#     "a":10,
#     "b":20
# }
# hit the send button


if __name__=="__main__":
    app.run(debug=True)