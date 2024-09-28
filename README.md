## Sentiment Analysis API
This project provides a Django-based API that processes customer reviews in CSV/XLSX formats and performs sentiment analysis using the Groq API Sentiment Analysis API. The API returns a structured JSON response with positive, negative, and neutral scores.

## Features
Accepts both CSV and XLSX files containing customer reviews.

Integrates with Groq API sentiment analysis model for text sentiment analysis.

Returns sentiment scores in a structured JSON format.

Basic error handling for unsupported file formats and missing columns.

Simple HTML upload form for testing file uploads via the browser.

## Technologies
Python

Django

Pandas

Groq API Sentiment Analysis API

Requests library

## Prerequisites
Make sure you have the following installed:

Python 3.x

pip (Python package manager)

A Groq API key

## Installation
Clone the repository:

git clone https://github.com/tutujnr/sentiment_analysis.git

cd sentiment_analysis

## Install the required packages:

pip install -r requirements.txt

Add your Groq API key to the project:

Open views.py and replace the placeholder YOUR_GROQ_API_KEY with your actual API key.

## Usage
Running the Development Server

Run the Django development server:

python manage.py runserver

Access the API via your browser or a tool like Postman:

Visit http://127.0.0.1:8000/upload/ in your browser to use the file upload form.

Alternatively, send a POST request to http://127.0.0.1:8000/sentiment/ with a file upload.

## API Endpoints
/upload/: Displays an HTML form for file upload.

/sentiment/: Accepts a CSV/XLSX file via POST and returns sentiment analysis results.
