from flask import Flask

app=Flask(__name__)

@app.route("/")
def homePage():
    # HOME PAGE
    return {"Message":"You are in the Home Page"}

@app.route("/health")
def healthPage():
    # HEALTH CHECK
    return {"Status":"Up"}

if __name__=="__main__":
    app.run(port=5000,debug=True,host="0.0.0.0")
