from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

recipes = [
    {
        'id': 1,
        'name': 'Egg Salad',
        'description': 'This is a lovely egg salad recipe.'
    },
    {
        'id': 2, 
        'name': 'Tomato Pasta',
        'description': 'This is a lovely tomato pasta recipe.'
    }
]
# get all recipes
@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})

# get a single recipe or th next recipe
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):   
    #recipe = recipe_id
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND

# create a recipe
@app.route('/recipes', methods=['POST'])
def create_recipe():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')
    recipe = {
        'id': len(recipes) + 1,
        'name': name,
        'description': description
    }
    recipes.append(recipe)
    return jsonify(recipe), HTTPStatus.CREATED

# update a recipe.
# start by getting the recipe with a specific ID:
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def update_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)
    # if recipe not found
    if not recipe:
        return jsonify({'message:' 'recipe not found'}), HTTPStatus.NOT_FOUND
   
    # if recipe found, then perform the recipe.update function
    data = request.get_json()
    recipe.update(
        {
            'name': data.get('name'),
            'description': data.get('description')
         }
    )


if __name__ == '__main__':
    app.run()