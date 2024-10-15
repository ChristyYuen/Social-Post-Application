# Social Post Application

## Overview
This project is a social post application built using **Py4web**, a web framework designed for rapid development of web applications in Python. Py4web emphasizes simplicity and speed, enabling developers to create applications with minimal boilerplate code while providing essential features like routing, templating, and database management.

## Features
- **User Authentication**: The application uses a simple authentication system without strict password complexity, making it easier for users to sign up and log in.
- **Create Posts**: Users can add new posts through a dedicated text area that appears when the "+" button is clicked. The posts are initially empty and can be submitted or canceled.
- **Display Posts**: All users can view each other's posts, which are displayed in reverse chronological order (newest at the top). Each post includes a delete button visible only to the author.
- **Delete Functionality**: Users can delete their own posts, which removes them immediately from the display and the database upon confirmation.
- **Thumbs Up/Down**: Users can react to posts with a thumbs up or down. The state of the thumbs changes as specified in the assignment, and each user's reaction is saved individually.
- **Likers/Dislikers List**: A list of users who liked or disliked a post is displayed when hovering over the thumbs, with caching implemented to avoid unnecessary reloads.

## Project Structure
- **app.py**: Main application file that handles routing and logic.
- **models.py**: Database models and schema definitions.
- **templates/**: Contains HTML templates for rendering views.
- **static/**: Static files like CSS and JavaScript.

## Installation
To run this application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/social-post-app.git
   cd social-post-app

2. Install the required dependencies:
   ```bash
   pip install py4web

3. Start the application:
   ```bash
   python app.py

4. Open your web browser and go to `http://localhost:8000`.

## Lessons Learned
Through the development of this project, I learned the importance of user-centered design in web applications. Ensuring that users can easily navigate and interact with the application was crucial for its success. Additionally, I gained valuable experience in using Py4web for rapid development, particularly its ORM and built-in features for managing user sessions and database interactions.

Implementing the caching mechanism for the likers and dislikers list was also a significant learning point, as it enhanced performance and provided a smoother user experience.