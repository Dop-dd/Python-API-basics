#Import the necessary classes 
from flask import Flask
from flask_restful import Api
from resources.recipe import RecipeListResource, RecipeResource, RecipePublishResource

# Set up Flask and initialize flask_restful.API with the Flask app
app = Flask(__name__)
api = Api(app)

# Add resource routing by passing in the URL so that it will route to our 
# resources. Each resource will have its own HTTP method defined
api.add_resource(RecipeListResource, '/recipes')
api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')


if __name__ == '__main__':
    app.run(port=5000, debug=True)