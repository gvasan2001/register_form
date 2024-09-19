from flask import *
import data_base

aa=data_base.data_base()

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("register")


# @app.route("/")
# def start():
#     return redirect('index')



# @app.route("/index")
# def index():
#     data=aa.show("select * from chat")
#     if data:
#         return render_template("chat_bot.html",msg=data)
#     else:
#         return render_template("chat_bot.html")
    

# @app.route("/add_text", methods=['get','post'])
# def add_text():
#     msg=request.form['box1']
#     aa.register("insert into chat value('"+msg+"')")

#     return redirect('index')

if __name__ == '__main__':
    app.run(debug=True)