from flask import Flask

app=Flask(__name__)

@app.route("/")
def homePage():
    return {"Message":"This is Home Page"}

@app.route("/health")
def health():
    return {"status":"Up"}

if __name__=="__main__":
    app.run(debug=True)