from flask import Flask, render_template, request
import openai
import pdfplumber
import tensorflow as tf
import tensorflow_hub as hub
from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()

# nlp = spacy.load("en_core_web_lg")
model_url = "https://tfhub.dev/google/universal-sentence-encoder-large/5"
embed = hub.load(model_url)

API_KEY = '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'

def parse_resume(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text

def get_tech_skills(job_profile):
    openai.api_key=API_KEY
    prompt=f"generate a job description for {job_profile}, out the minimum qualifications, tech skills and soft skills in different sections and be very concise in your response"
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        temperature=0.7,
        max_tokens=300
    )

    return response.choices[0].text.strip()

def calculate_compatibility(user_resume,job_description_skills):
    # Calculate the compatibility score based on the semantic similarity of skills
    compatibilty_score = tf.reduce_sum(tf.multiply(user_resume,job_description_skills))

    # Return the compatibility score rounded to two decimal places
    return round(compatibilty_score*100, 2)

app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')


@app.post('/upload')
def upload():
    # Handle uploaded files and extract data here
    resume_file = request.files['resume']
    job_profile = request.form['job_profile']

    # Parse the resume
    user_resume= parse_resume(resume_file)
    a=embed([parse_resume(resume_file)])[0]

    # Extract skills from the generated job description
    job_description = get_tech_skills(job_profile)
    b=embed([get_tech_skills(job_profile)])[0]

    # Calculate compatibility score based on skill matching
    compatibility_score = calculate_compatibility(a,b)

    # Return the results to the user in the template
    return render_template('ayamresult.html', job_profile=job_profile, job_description=job_description, compatibility_score=compatibility_score.numpy())


if __name__ == '__main__':
    app.run(debug=True)
