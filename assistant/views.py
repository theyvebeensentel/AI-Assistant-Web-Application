import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import google.generativeai as genai

logger = logging.getLogger(__name__)

def index_view(request):
    return render(request, 'assistant/index.html')

@csrf_exempt
def generate_ai_response(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method. Only POST allowed.'}, status=405)

    api_key = getattr(settings, 'GEMINI_API_KEY', '') or ''
    if not api_key:
        return JsonResponse({
            'error': 'Gemini API key is missing. Please configure GEMINI_API_KEY in your .env file.'
        }, status=500)

    try:
        data = json.loads(request.body)
        user_prompt = data.get('prompt', '').strip()
        
        if not user_prompt:
            return JsonResponse({'error': 'Prompt cannot be empty.'}, status=400)

        genai.configure(api_key=api_key)
        
        model = genai.GenerativeModel('gemini-3.8-flash')
        response = model.generate_content(user_prompt)

        if hasattr(response, 'text') and response.text:
            return JsonResponse({'response': response.text})
        else:
            return JsonResponse({'error': 'No response generated from the model.'}, status=500)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format in request body.'}, status=400)
    except Exception as e:
        logger.error(f"Error calling Gemini API: {str(e)}")
        return JsonResponse({'error': f"Failed to generate response: {str(e)}"}, status=500)
