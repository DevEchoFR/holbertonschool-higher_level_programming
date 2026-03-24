#!/usr/bin/python3
"""Task 2: Dynamic template with loops and conditions."""

import json
import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	"""Render home page."""
	return render_template('index.html')


@app.route('/about')
def about():
	"""Render about page."""
	return render_template('about.html')


@app.route('/contact')
def contact():
	"""Render contact page."""
	return render_template('contact.html')


@app.route('/items')
def items():
	"""Render items page from JSON file."""
	base_dir = os.path.dirname(os.path.abspath(__file__))
	json_path = os.path.join(base_dir, 'items.json')
	items_list = []

	try:
		with open(json_path, 'r', encoding='utf-8') as file:
			data = json.load(file)
			if isinstance(data, dict):
				items_list = data.get('items', [])
	except (OSError, json.JSONDecodeError):
		items_list = []

	return render_template('items.html', items=items_list)


if __name__ == '__main__':
	app.run(debug=True, port=5000)
