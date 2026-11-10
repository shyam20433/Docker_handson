from flask import Flask
import os
app=Flask(__name__)

# increment the count when someone hits the /health page
def increment():
    os.makedirs("/data", exist_ok=True)

    if not os.path.exists("/data/counter.txt"):
        with open("/data/counter.txt", "w") as file:
            file.write("0")
    with open("/data/counter.txt","r") as file:
        count=int(file.read())
    count+=1
    with open("/data/counter.txt","w") as file:
        file.write(str(count))
    return count

@app.route("/")
def homePage():
    # HOME PAGE
    return {"Message":"You are in the Home Page"}

@app.route("/health")
def healthPage():
    increment()
    # HEALTH CHECK
    return {"Status":"Up"}

@app.route("/counter")
def counter():
    os.makedirs("/data", exist_ok=True)
    if not os.path.exists("/data/counter.txt"):
        with open("/data/counter.txt", "w") as file:
            file.write("0")
            return 0
    else:
        with open("/data/counter.txt","r") as file:
            return file.read()



if __name__=="__main__":
    app.run(port=5000,debug=True,host="0.0.0.0")
