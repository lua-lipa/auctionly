""" class to initialize the web application """
from auctionly import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
