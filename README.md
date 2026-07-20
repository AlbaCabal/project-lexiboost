# LexiBoost

## Video Demo: https://youtu.be/8ymwa4XrSKU

## Versions

| Date       | Version | Description          |
|------------| ------- |----------------------|
| 12/12/2025 | 1.0.0   | Initial CS50 version |
| 19/06/2026 | 2.0.0   | Application refactored using Flask Blueprints, SQLAlchemy and Service Layer          |


## Description
LexiBoost is a web application that helps English learners improve their vocabulary by encouraging them to use words they have already learned.
Unlike grammar correction tools or AI writing assistants, LexiBoost focuses on vocabulary practice. Its purpose is simple: detect common words in a text and replace them with synonyms that already exist in the user's personal vocabulary list.
As an English learner myself, I noticed that I often used the same basic words even after learning more advanced vocabulary. This project was created to solve that problem by making vocabulary practice part of the writing process.

When a user submits a text, LexiBoost:
1. Splits the text into individual words.
2. Retrieves possible synonyms using the Datamuse API.
3. Compares those synonyms with the user's saved vocabulary.
4. Replaces words whenever a learned synonym is found.
5. Stores both the original and modified text in the user's history.
The application is intentionally simple. It is designed as a vocabulary learning tool rather than an AI-powered writing assistant..

## Features
- User authentication
- Personal vocabulary list
- Vocabulary replacement while writing
- Writing history
- User-specific data
- Responsive interface
- Password hashing
- Session management
- Database persistence

## Technologies
LexiBoost was built using:
- **Python**: Backend programming language.
- **Flask**: Web framework.
- **Flask Blueprints**: Modular route organization.
- **MySQL**: Relational database.
- **SQLAlchemy**: ORM used to map Python classes to database tables and simplify database operations.
- **Flask-Session**: Server-side session management.
- **HTML and CSS**
- **Jinja2**
- **JavaScript**
- **Datamuse API**: Used to find words that are similar in meaning.
- **Pytest**: Unit testing framework.

## Project Structure
- `app/`
  - `__init__.py`
  - `extensions.py`
  - `models.py`
  - `routes/`
    - `auth_routes.py`
    - `content_routes.py`
  - `services/`
    - `history_service.py`
    - `user_service.py`
    - `vocabulary_service.py`
  - `static/`
    - `css/`
      - `layout.css`
      - `styles.css`
    - `js/`
      - `main.js`
  - `templates/`
    - `users/`
      - `index.html`
      - `vocabulary.html`
      - `write.html`
    - `layout.html`
    - `login.html`
    - `register.html`
- `tests/`
  - `conftest.py`
  - `test_models.py`
  - `test_user_service.py`
  - `test_vocabulary.py`
- `requirements.txt`
- `pytest.ini`
---
## Project Architecture
The project follows a modular architecture inspired by the MVC pattern.

### Application Factory
The application is created using Flask's Application Factory pattern inside __init__.py.
This approach makes the project easier to configure, test and extend.

### Models
The models.py file defines the database structure using SQLAlchemy.
The main models are:
- User
- Vocabulary
- History
- SearchedWord

Relationships between models are managed through SQLAlchemy.

### Routes
Routes are divided into Blueprints.

auth_routes.py → Handles authentication:
- Register
- Login
- Logout

content_routes.py → Handles the application features:
- Writing
- Vocabulary
- History

Separating routes improves readability and scalability.

### Services
Business logic is separated from HTTP routes.

user_service.py → contains operations related to users.

vocabulary_service.py → Handles adding vocabulary, retrieving vocabulary, deleting vocabulary, checking duplicates

history_service.py → Stores and retrieves user writing history.

Keeping business logic inside services keeps the routes small and easier to maintain.

---
## Design Decisions
Several architectural decisions were made while developing version 2.0.

### Service Layer
Business logic was moved from routes into dedicated service classes. This makes the code more reusable and easier to test.
### Flask Blueprints
Routes were separated by functionality instead of keeping everything in a single file.
### SQLAlchemy
Using an ORM simplified database operations and reduced the amount of SQL code required.
### User-specific vocabulary
Each user maintains an independent vocabulary list, allowing personalized learning.
### Writing history
Saving every submitted text allows learners to review previous writing and monitor their vocabulary progress over time.

## Future Improvements
The following features could be added in future versions of LexiBoost:
- **Predefined vocabulary by level**: Add built-in vocabulary lists for common English levels such as B1, B2, C1, and C2, so users can start practicing without manually adding every word.
- **Grammar and spelling correction**: Extend the application to detect and correct basic grammar and spelling mistakes, making it a more complete writing support tool.
- **Visual highlight for changed words**: Show replaced words with a green underline, so users can easily see what was modified in their text.
- **Word meaning on hover**: Display the meaning of a replaced word when the user moves the mouse over it, helping learners understand and remember new vocabulary.
