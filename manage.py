from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    """TODO: Docstring for index.
    :returns: TODO

    """
    return 'index'


if __name__ == "__main__":
    app.run()
