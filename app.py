from flask import Flask, render_template, redirect, request, url_for
import os
from flask_pymongo import PyMongo
from bson.objectid import ObjectId





app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'my_cookbook'
app.config["MONGO_URI"] = 'mongodb+srv://root:R00t75@cluster0-efmd8.mongodb.net/my_cookbook?retryWrites=true'

mongo = PyMongo(app)

#home page
@app.route('/')
@app.route('/home_page')
def home_page():
    
    return render_template('home.html', categories = mongo.db.categories.find())
    
#show full list of recipes
@app.route('/list_recipes')
def list_recipes():
    
    return render_template('list_recipes.html', recipes = mongo.db.recipes.find(), categories = mongo.db.categories.find())
    
    
#show choosen  category
@app.route('/list_categories/<category_id>')
def list_categories(category_id):
    
    the_category = mongo.db.recipes.find({"category_name": ObjectId(category_id)})
    return render_template('categories.html', category = the_category, recipes = mongo.db.recipes.find(), categories = mongo.db.categories.find())


#show an individual recipe
@app.route('/show_recipe/<recipe_id>')
def show_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return render_template('recipes.html', recipe = the_recipe, categories = all_categories)
    


# show favourites
@app.route('/show_favourites')
def show_favourites():
    return render_template('favourites.html', recipe = mongo.db.recipes.find(), categories = mongo.db.categories.find(), favourites = mongo.db.recipes.find( {"add_favourite": "on" } ))
                                                                                                                                                                
                                                                                                                                    
    
#add a recipe 
@app.route('/add_recipe')
def add_recipe():
    _categories = mongo.db.categories.find()
    category_list = [category for category in _categories]
    
    return render_template('add_recipe.html', categories = category_list)

#insert recipe into mongoDB that you added with #add a recipe
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('list_recipes'))

#edit a recipe    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    category_list = [category for category in all_categories]
    return render_template('editrecipe.html', recipe = the_recipe, categories = category_list)
    
# delete an individual recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    remove_recipe = mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    all_categories = mongo.db.categories.find()
    return redirect(url_for('list_recipes', recipe = remove_recipe, categories = all_categories))
    
#update database
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe_updated = mongo.db.recipes
    recipe_updated.update({"_id": ObjectId(recipe_id)},
    {
    
    'category_name':request.form.get('category_name'),
    'title':request.form.get('title'),
    'description':request.form.get('description'),
    'ingredients':request.form.get('ingredients'),
    'preparation_time':request.form.get('preparation_time'),
    'cooking_time':request.form.get('cooking_time'),
    'cooking_instructions':request.form.get('cooking_instructions'),
    'vegan_friendly':request.form.get('vegan_friendly'),
    'gluten_free':request.form.get('gluten_free'),
    'add_favourite':request.form.get('add_favourite'),
    'difficulty':request.form.get('difficulty')
    
    
    })
    return redirect(url_for('list_recipes'))
    
    

if __name__ == '__main__':
    
    app.run(host=os.environ.get('IP'),port=int(os.environ.get('PORT')),
    debug=True)

