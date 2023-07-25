# Resume-Compatibility-Analyzer

This Flask web application is designed to predict the compatibility between a user's resume and a specific job profile. It utilizes the Universal Sentence Encoder, OpenAI API, and pdfplumber library to achieve this functionality.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- pdfplumber
- TensorFlow
- TensorFlow Hub
- OpenAI API Key (Replace 'YOUR API KEY HERE' in the code with your actual API key)

Install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

1. Obtain an API Key from OpenAI: To use the application, you need an API key from OpenAI. Sign up for an account and get your API key.

2. Insert the API Key: Replace `'YOUR API KEY HERE'` in the code with your actual OpenAI API key.

3. Start the Web Application: Run the Flask application by executing the `main.py` file. The application will be accessible on `http://127.0.0.1:5000/` in your web browser.

4. Upload a Resume: Navigate to the home page of the application and upload a resume in PDF format. The application will parse the resume and extract the text content.

5. Enter a Job Profile: Input the desired job profile for which you want to predict compatibility. The application will generate a concise job description using the OpenAI API.

6. Get Compatibility Score: The application will calculate the compatibility score between the user's resume and the job description based on semantic similarity. The compatibility score will be displayed to the user.

## How It Works

The application uses the Universal Sentence Encoder model to vectorize text data, enabling semantic similarity calculation. It leverages the OpenAI API to generate a concise job description based on the input job profile. The text content from the user's uploaded resume and generated job description are vectorized using the Universal Sentence Encoder. The compatibility score is computed based on the semantic similarity of the two vectors.

## Notes

- This application is for demonstration purposes and should not be used as the sole decision-making factor for job applications.
- The application is currently set to run in debug mode for development purposes. Ensure to disable debug mode when deploying it in production.

Feel free to customize the UI, improve the model, or add additional features to suit your specific needs. Happy predicting!
