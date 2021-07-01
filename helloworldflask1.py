#dynamic route

from flask import Flask

app = Flask(__name__)


app.config["DEBUG"] = True

@app.route("/")
@app.route("/hello")


def hello_world():
	return ("hello_world?")


@app.route("/test/<search_query>")
def search(search_query):
	return (search_query)

app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return ("hello, {}".format(name))
	else:
		return ("not found", 404)




if __name__ == '__main__':
    app.run(host='0.0.0.0')