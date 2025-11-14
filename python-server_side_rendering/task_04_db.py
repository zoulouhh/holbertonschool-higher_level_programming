#!/usr/bin/python3
"""Flask application for displaying products from different file sources."""

from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    """Read data from JSON file."""
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def read_csv_data():
    """Read data from CSV file."""
    products = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return []

def read_sql_data():
    """Read data from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
        return products
    except sqlite3.Error:
        return []
    finally:
        if conn:
            conn.close()

@app.route('/products')
def products():
    """Handle product display with source and optional id parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:  # Added 'sql' to valid sources
        return render_template('product_display.html', 
                             error="Wrong source")

    # Read data from appropriate source
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        products = read_sql_data()

    # Filter by id if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', 
                                     error="Product not found")
            products = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid product ID")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)