from flask import Flask
from views import views 

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/views")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)