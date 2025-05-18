from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# Replace with your MongoDB Atlas URI
MONGO_URI = "mongodb+srv://flask_user:flask_pass123@cluster0.5tuuyga.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["flask_user"]
collection = db["cluster0"]

@app.route('/', methods=['GET', 'POST'])
def form():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except PyMongoError as e:
            error = f"An error occurred: {str(e)}"

    return render_template('form.html', error=error)

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
