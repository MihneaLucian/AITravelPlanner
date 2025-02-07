from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# 🔹 Replace with your actual OpenAI API Key
openai.api_key = "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"

@app.route('/')
def home():
    return render_template("index.html")  # Loads the HTML page

@app.route('/generate-itinerary', methods=['POST'])
def generate_itinerary():
    destination = request.form.get('destination')
    duration = request.form.get('duration')
    budget = request.form.get('budget')
    interests = request.form.getlist('interests')


    # Convert interests list to a comma-separated string
    interests_text = ", ".join(interests) if interests else "General travel"

    # Generate a prompt for OpenAI
    prompt = f"Create a {duration}-day travel itinerary for {destination} with a {budget} budget. Focus on {interests_text}. Include hotel recommendations, must-visit places, and dining options.In the end Analyze the best time to visit {destination}: Weather conditions by month, Cheapest months for flights,Busiest vs. quietest tourist seasons,Recommended travel months"

    # Request AI to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[{"role": "user", "content": prompt}]
    )

    itinerary = response["choices"][0]["message"]["content"]

    return jsonify({"itinerary": itinerary})

if __name__ == '__main__':
    app.run(debug=True)
