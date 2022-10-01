from flask import Flask,redirect ,url_for
app = Flask (__name__)
@app.route('/admin')
def hellow_admin():
    return 'hellow admin'

@app.route('/guest/<guest>')
def hellow_guest(guest):
    return "heellow %s as guest"%guest

@app.route ("/user/<name>")
def hellow_user(name):
    if name=="admin":
        return redirect (url_for("hellow_admin"))
    else :
        return redirect (url_for("hellow_guest",guest=name))

if __name__=="__main__":
    app.run(debug=True)        
            