""""The main app of my flask proyect"""
import openai
import requests
from flask import Flask, render_template, request, send_file,redirect,jsonify
from pptx import Presentation

app = Flask('run',template_folder='app/views')

def chatGPTrequest(text):
    openai.api_key  = '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'
    prompt = 'Make me a JSON file of a PowerPoint presentation of the theme "'+text+'" in Spanish. This JSON file will contain multiple slides, each slide possibly containing the following: Title of the slide, descriptions of images it may have, and possible text.Here is an example about deer:{"slides": [{"title": "Definición de venado","image": "Una imagen de un majestuoso venado en su hábitat natural","text": "Los venados son animales majestuosos que habitan en diversas regiones del mundo."},{"title": "Características del venado","image": "Una imagen que muestra diferentes especies de venados con características únicas","text": "Existen diferentes especies de venados, cada una con características únicas."},{"title": "Cuernos ramificados del venado","image": "Una imagen que ilustra los cuernos ramificados de un venado, utilizados para la competencia y atracción de parejas","text": "Los venados poseen cuernos ramificados que son utilizados para la competencia y atracción de parejas."}, {"title": "Hábitats del venado","image": "Una imagen que muestra un venado en su hábitat natural, adaptándose a diferentes entornos como bosques, praderas y montañas","text": "Los venados se adaptan a diferentes hábitats, desde bosques hasta praderas y montañas."},{"title": "Importancia de la conservación del venado","image": "Una imagen que destaca la importancia de la conservación de los venados para preservar la biodiversidad y el equilibrio de los ecosistemas","text": "La conservación de los venados es crucial para preservar la biodiversidad y el equilibrio de los ecosistemas."}]}And so on, with multiple slides. Please note that:1. I want the image attribute to contain a description of the image, not a URL.2. The title attribute should contain the title of the slide, not the number of the slide3. I only want the JSON file in your response. Do not include any additional text, only JSON.'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=1000,
        n=1,
        stop=None,
        temperature=0.7
    )
    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text']
    return {}


@app.route('/',methods=['GET','POST'])
def index():
     if request.method == 'POST':
        txt = request.form.get('input_text')
        json = chatGPTrequest(txt)
        return json
 
     return render_template('index.html')

@app.route('/download')
def descargar():
    txt = request.args.get('input_text')
    json = chatGPTrequest(txt)
    return json
    
if __name__ == '__main__':
    app.run(debug=True)

