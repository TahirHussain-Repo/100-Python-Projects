from flask import Flask
import json

app = Flask(__name__)

recipes = {
    1: {'id': 1, 'title': 'Spaghetti Carbonara', 'ingredients': ['spaghetti', 'eggs', 'pecorino cheese', 'guanciale'], 'instructions': 'Cook pasta, fry guanciale, mix with eggs and cheese, and combine with pasta.'},
    2: {'id': 2, 'title': 'Tomato Soup', 'ingredients': ['tomato', 'water', 'salt'], 'instructions': 'Boil all together until mushy, blend, and serve.'},
    3: {'id': 3, 'title': 'Grilled Cheese Sandwich', 'ingredients': ['bread', 'cheese', 'butter'], 'instructions': 'Butter bread, place cheese between slices, grill until golden.'}
}

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = recipes.get(recipe_id)
    if recipe:
        return recipe
    else:
        return {'error': 'Recipe not found'}, 404

@app.route('/')
def index():
    return 'Homepage'

app.run(debug = True) 
