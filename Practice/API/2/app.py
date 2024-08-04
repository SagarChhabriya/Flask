from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {
        "name":"sagar",
        "city":"kandhkot",
        "dept":"cs",
    },
    {
        "name":"kamlesh",
        "city":"kandhkot",
        "dept":"cs",
    },
    {
        "name":"qadeer",
        "city":"kandhkot",
        "dept":"cs",
    },
    
]


@app.route("/")
def index():
    return render_template("index.html",title="index")

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method == "POST":
        maths   = float(request.form['maths'])
        english = float(request.form['english'])
        ict     = float(request.form['ict'])

        score = (maths + english + ict) / 3
        return render_template("form.html",score=score,title="form")
    
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)