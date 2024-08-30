from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

SPOONACULAR_API_KEY = 'your_spoonacular_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_recipes', methods=['POST'])
def get_recipes():
    ingredients = request.form['ingredients']
    api_url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={SPOONACULAR_API_KEY}"
    
    response = requests.get(api_url)
    recipes = response.json()

    detailed_recipes = []
    for recipe in recipes:
        recipe_id = recipe['id']
        detail_url = f"https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={SPOONACULAR_API_KEY}"
        detail_response = requests.get(detail_url)
        detailed_recipes.append(detail_response.json())

    return jsonify(detailed_recipes)

if __name__ == '__main__':
    app.run(debug=True)
