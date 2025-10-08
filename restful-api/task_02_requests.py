#!/usr/bin/python3
"""
Module: task_02_requests
Description:
    Demonstrates fetching data from a public API using the requests library,
    parsing JSON, printing information, and saving structured data to a CSV file.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches posts from JSONPlaceholder API and prints their titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the HTTP response status code
    print(f"Status Code: {response.status_code}")

    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()

        # Iterate and print post titles
        for post in posts:
            print(post.get("title"))
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetches posts from JSONPlaceholder API and saves them to a CSV file.
    The CSV file will contain columns: id, title, and body.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        posts = response.json()

        # Prepare list of dictionaries with selected fields
        formatted_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        # Write to CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(formatted_posts)

    else:
        print("Failed to fetch posts.")


# The functions are called from main_02_requests.py
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
