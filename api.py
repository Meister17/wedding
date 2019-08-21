# coding: utf-8
from __future__ import unicode_literals
import json
import logging
import os

from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

responses = {}

for filename in os.listdir('data'):
	with open(os.path.join('data', filename), 'rt') as file_input:
		responses[os.path.splitext(filename)[0]] = file_input.read().replace('\r', '').replace('\n', '')

@app.route("/", methods=["POST"])

def main():
	logging.info("Request: %r", request.json)

	response = {
		"version": request.json["version"],
		"session": request.json["session"],
		"response": {
			"end_session": False
		}
	}

	handle_dialog(request.json, response)

	logging.info("Response: %r", response)

	return json.dumps(
		response,
		ensure_ascii=False,
		indent=2
	)


def handle_dialog(req, res):
	if req['session']['new']:
		res['response']['text'] = responses['introduction']
		return

	utterance = req['request']['original_utterance'].lower()
	if utterance in ['давай познакомимся', 'знакомство', 'запускай знакомство']:
		res['response']['text'] = responses['acquaintance']
	elif utterance in ['клятва']:
		res['response']['text'] = responses['swear']
	elif utterance in ['разогрев', 'разогрей публику', 'давай разогрев']:
		res['response']['text'] = responses['warm_up']
	elif utterance in ['запусти свою игру', 'давай свою игру', 'своя игра']:
		res['response']['text'] = responses['own_game']
	elif utterance in ['конкурс песни', 'давай конкурс песни']:
		res['response']['text'] = responses['songs']
	elif utterance in ['шоу интуиция', 'конкурс интуиция']:
		res['response']['text'] = responses['intuition']
	elif utterance in ['давай к путешествиям', 'конкурс путешествия', 'путешествия']:
		res['response']['text'] = responses['travel']
	elif utterance in ['фотосессия в хорошую погоду']:
		res['response']['text'] = responses['photo_good_weather']
	elif utterance in ['фотосессия в плохую погоду']:
		res['response']['text'] = responses['photo_bad_weather']
	elif utterance in ['фокусник', 'встречай фокусника', 'представь фокусника']:
		res['response']['text'] = responses['magician']
	elif utterance in ['время дженги', 'дженга']:
		res['response']['text'] = responses['jenga']
	elif utterance in ['время аукционов', 'аукционы']:
		res['response']['text'] = responses['auction']
	elif utterance in ['заключительное слово', 'окончание мероприятия']:
		res['response']['text'] = response['final']
