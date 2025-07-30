from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/',methods=["GET","POST"])
def calculate_bmi():
    bmi=None
    category=None
    if request.method=="POST":
        try:
            height=float(request.form["height"])
            weight=float(request.form["weight"])
            if height>0 and weight>0:
                bmi= weight/(height**2)
                #determine category

                if bmi<18.5:
                    category="underweight"
                elif 18.5<=bmi<=25:
                    category="Normal weight"
                else:
                    category="overweight"
            else:
                category="invalid input"
        except ValueError:
            category="invalid input: please enter the numeric value"
    return render_template("Index.html",bmi=bmi,category=category)


if __name__=="__main__":
    app.run(debug=True)
