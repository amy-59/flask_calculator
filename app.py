from flask import Flask, render_template, redirect,url_for, request
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome"

@app.route("/cal",methods=["GET"])
def math_operator():
    operation=request.jeson["operation"]
    num1=request.json['num1']
    num2=request.json['num2']

    # Operation 
    if operation=="add":
        result=num1+num2
    elif operation=='substract':
        result=num1-num2
    elif operation=="multiply"
        result=num1*num2
    else:
        result=num1/num2
    return result

if __name__=="__main__":
    app.run(debug=True)