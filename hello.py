from flask import Flask,redirect, url_for

app = Flask(__name__)

#开启调试模式，代码修改后可自动重载
app.debug = True

@app.route("/")
def hello_world(username):

    return  redirect(url_for("login"))

@app.route("/haha")
def login():
    return "登陆页面"




if __name__ == "__main__":
    app.run(host="127.0.0.1",port=5000)