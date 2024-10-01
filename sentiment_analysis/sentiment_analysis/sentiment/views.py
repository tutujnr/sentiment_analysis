from django.http import JsonResponse
from django.shortcuts import render
import pandas as pd
import requests

def upload_form(request):
    return render(request, 'upload.html')

def sentiment_analysis(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        file_extension = file.name.split('.')[-1].lower()

        try:
            if file_extension == 'csv':
                data = pd.read_csv(file)
            elif file_extension in ['xls', 'xlsx']:
                data = pd.read_excel(file)
            else:
                return JsonResponse({"error": "Unsupported file format"}, status=400)

            if 'Review' not in data.columns:
                return JsonResponse({"error": "'Review' column not found in the file"}, status=400)

            reviews = data['Review'].tolist()
            sentiment_results = perform_sentiment_analysis(reviews)
            return JsonResponse(sentiment_results)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    
    return JsonResponse({"error": "No file uploaded or invalid request"}, status=400)

def perform_sentiment_analysis(reviews):
    api_url = "https://api.groq.com/sentiment"
    headers = {"Authorization": "Bearer Your_API_key"} #replace with your actual api key

    positive_score, negative_score, neutral_score = 0, 0, 0

    for review in reviews:
        try:
            response = requests.post(api_url, headers=headers, json={"text": review}, verify=False, timeout=10)
            response.raise_for_status()

            sentiment = response.json()
            positive_score += sentiment.get('positive', 0)
            negative_score += sentiment.get('negative', 0)
            neutral_score += sentiment.get('neutral', 0)

        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    return {
        "positive": positive_score,
        "negative": negative_score,
        "neutral": neutral_score
    }
