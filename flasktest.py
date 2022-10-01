from flask import Flask
app=Flask(__name__)
@app.route("/home/<name>")
def home(name):
    return "hellow , Welcome to our website %s as guest "% name
if __name__ == "__main__":
    app.run()    