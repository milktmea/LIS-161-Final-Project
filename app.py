from flask import Flask
from data import swimsuit

app = Flask(__name__)

@app.route('/') 
def index():
    return """<h1>Welcome UPVST!</h1>
                <p>Browse through the links below and pick your brand of swimsuit:</p>
                <ul>
                    <li><a href='/brand/Neptune Actives'>Neptune Actives</a></li>
                    <li><a href='/brand/Amanzi'>Amanzi</a></li>
                    <li><a href='/brand/Speedo'>Speedo</a></li>
                </ul>
    """

@app.route('/brand/<swimsuit_type>')
def brand(swimsuit_type):
    html = "<h1>List of {}</h1>".format(swimsuit_type)
    html += "<ul>"
    my_swimsuit = swimsuit[swimsuit_type]

    for item in my_swimsuit:
        html += "<li>{}</li>".format(item["suit"])

    html += "</ul>"
    return html


if __name__ == '__main__':
    app.run(debug=True)