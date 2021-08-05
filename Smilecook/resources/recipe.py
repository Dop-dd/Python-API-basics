# To build an API endpoint, we need to define a class 
# that inherits from flask_restful.Resource

from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipe import Recipe, recipe_list

# We need to create three resources: RecipeListResource,
# RecipeResource, and RecipePublishResource

class RecipeListResource(Resource):
    # Add the get metho
    def get(self):
            data = []
            for recipe in recipe_list:
                if recipe.is_publish is True:
                    data.append(recipe.data)
            return {'data': data}, HTTPStatus.OK

# Add the post method
    def post(self):
        data = request.get_json()
        recipe = Recipe(name=data['name'],
                        description=data['description'],
                        num_of_servings=data['num_of_servings'],
                        cook_time=data['cook_time'],
                        directions=data['directions'])
        recipe_list.append(recipe)
        return recipe.data, HTTPStatus.CREATED

# define the recipe resource
class RecipeResource(Resource):
    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe.id and 
        recipe.is_publish == True), None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
        return recipe.data, HTTPStatus.OK

        # Implement the put method
    def put(self, recipe_id):
        data = request.get_json()
        recipe = recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']
        return recipe.data, HTTPStatus.OK

    # delete recipe
    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
            #recipe.is_publish = False
        recipe_list.remove(recipe)
        return {}, HTTPStatus.NO_CONTENT
        

# Define the RecipePublic resource and implement the put method 
# RecipePublishResource inherits from flask_restful.Resource
class RecipePublishResource(Resource):
# finds the recipe with the passed-in recipe_id and update the is_publish status to true.
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
            # shows that the recipe has been published successfully.
        recipe.is_publish = True
        return{}, HTTPStatus.NO_CONTENT

    # Implement the delete method
    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)
        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND
            recipe.is_publish = False
            return {}, HTTPStatus.NO_CONTENT



