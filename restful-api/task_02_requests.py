#!/usr/bin/python3
"""
Task 02 - Consuming and processing data from an API using Python
"""

import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder API and print their titles.
    """
    response = requests.get(API_URL)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If request is successful
    if response.status_code == 200:
        posts = response.json()  # Parse JSON response

        # Iterate and print titles
        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder API and save them to posts.csv
    """
    response = requests.get(API_URL)

    # If request is successful
    if response.status_code == 200:
        posts = response.json()

        # Structure data into list of dictionaries
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body"),
            }
            for post in posts
        ]

        # Write to CSV file
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
