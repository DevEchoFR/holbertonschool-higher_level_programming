#!/usr/bin/python3
"""Task 3: Display product data from JSON or CSV."""

import csv
import json
import os

from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_from_json(file_path):
	"""Read products from a JSON file."""
	try:
		with open(file_path, 'r', encoding='utf-8') as file:
			data = json.load(file)
			if isinstance(data, list):
				return data
			return []
	except (OSError, json.JSONDecodeError):
		return []


def read_products_from_csv(file_path):
	"""Read products from a CSV file."""
	products = []
	try:
		with open(file_path, 'r', encoding='utf-8', newline='') as file:
			reader = csv.DictReader(file)
			for row in reader:
				products.append(
					{
						'id': int(row.get('id', 0)),
						'name': row.get('name', ''),
						'category': row.get('category', ''),
						'price': float(row.get('price', 0)),
					}
				)
	except (OSError, ValueError, TypeError):
		return []
	return products


@app.route('/products')
def products():
	"""Render products from selected source and optional id filter."""
	source = request.args.get('source')
	product_id = request.args.get('id')
	base_dir = os.path.dirname(os.path.abspath(__file__))

	if source == 'json':
		data = read_products_from_json(os.path.join(base_dir, 'products.json'))
	elif source == 'csv':
		data = read_products_from_csv(os.path.join(base_dir, 'products.csv'))
	else:
		return render_template(
			'product_display.html', error='Wrong source', products=[]
		)

	if product_id is not None:
		try:
			target_id = int(product_id)
			data = [product for product in data if int(product.get('id')) == target_id]
		except (ValueError, TypeError):
			data = []

		if len(data) == 0:
			return render_template(
				'product_display.html',
				error='Product not found',
				products=[],
			)

	return render_template('product_display.html', products=data, error=None)


if __name__ == '__main__':
	app.run(debug=True, port=5000)
