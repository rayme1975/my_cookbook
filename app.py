from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'my_cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00t75@cluster0-efmd8.mongodb.net/my_cookbook?retryWrites=true'

mongo = PyMongo(app)

@app.route('/')
@app.route('/list_recipes')
def list_recipes():
    return render_template('recipes.html', recipes = mongo.db.recipes.find())
    
if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),
    debug=True)

