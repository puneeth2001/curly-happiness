from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import json
import requests
import random
from django.utils.decorators import method_decorator
from django.http.response import HttpResponse
from django.shortcuts import render


# from test import chatbot_tutorial


def chat(request):
    context = {}
    return render(request, 'chatbot_tutorial/chatbot.html', context)


def respond_to_websockets(message):
    Disease = {
        'Arthritis': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Arthritis" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""],
        'Asthma': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Asthma" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""],
        'cold': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Cold" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""],
        'Diabetes': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Diabetes" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""],
        'Headache': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Headache" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""],
        'Fever': ["""From the symptoms that you have mentioned I have come to the conclusion that you have "Fever" if you are not satisfied with
     this conclusion please kindly contact the suggested doctors"""]
    }

    result_message = {
        'type': 'text'
    }
    if 'Joint Pains,Inflamation' in message['text']:
        result_message['text'] = Disease['Arthritis']


    elif 'Throat Pain,Wheezing' in message['text']:
        result_message['text'] = Disease['Asthma']

    elif 'Cold,Cough,HighTemperature' in message['text']:
        result_message['text'] = Disease['Fever']
    elif 'Fatigue,Weight loss' in message['text']:
        result_message['text'] = Disease['Diabetes']
    elif 'Vomiting,Nausea' in message['text']:
        result_message['text'] = Disease['Headache']
    elif message['text'] in ['hi', 'hey', 'hello']:
        result_message['text'] = "Hello to you too! Please suggest your symptoms so that I can be of help"
    else:
        result_message['text'] = "I don't know any responses for that.Please suggest a valid symptom"

    return result_message