# LexiBoost

## Video Demo: (url)

## Versions

| Date     | Version | Description                                                 |
| ---------- | ------- | ------------------------------------------------------------ |
| 12/12/2025 | 1.0.0   | Initial version                                             |

## Description
LexiBoost is a web application created to help English learners improve their writing by practicing vocabulary usage. The main goal of this project is not to check grammar, rephrase sentences, or correct writing mistakes. Instead, LexiBoost focuses on a single and clear task: finding simple words in a text and replacing them with similar words that the user is learning.

As an English learner myself, I noticed that many students often use very basic words even when they already know better ones. This usually happens because using new vocabulary feels risky, and learners prefer words they feel safe with. LexiBoost was designed to reduce that fear by helping users practice replacing simple words with familiar alternatives in a controlled way.

The application allows users to create an account, save vocabulary words they are learning, and write short texts. When a user submits a text, LexiBoost checks each word and looks for similar words using the Datamuse API. If a similar word matches one of the words saved in the user’s vocabulary list, the application replaces the original word with that vocabulary word. The result is a new version of the text with slightly improved vocabulary.

LexiBoost does not claim to produce perfect results. The word replacement is simple and sometimes limited, but this is intentional. The project is meant as a learning tool, not a full writing assistant. Keeping the logic simple also made the project easier to understand and build as a first web application.

This makes it particularly useful for learners who:
- want to practice using newly studied words in sentences,
- tend to overuse common verbs, adjectives, or connectors,
- need a simple tool to generate small variations to their writing,
- prefer a controlled learning environment rather than an AI-generated rewrite.

## Technologies
LexiBoost was built using the following technologies:
- **Python**: Used for all backend logic and text processing.
- **Flask**: A lightweight web framework used to manage routes, templates, and user sessions.
- **SQLite**: A simple database used to store users, vocabulary words, and writing history.
- **HTML and CSS**: Used to build and style the user interface.
- **Jinja2**: Flask’s templating engine, used to render dynamic content.
- **JavaScript**: Used to manage tabs in the writing history view.
- **Datamuse API**: Used to find words that are similar in meaning.

## File Structure and Explanation
- `app.py`
- `lexiboost.db` →  SQLite database with vocabulary mappings
- `schema.sql`
- `requirements.text`→ Required Python packages
- `static/`
   - `javascript.js`
   - `styles.css`
- `templates/`
   - `layout.html` 
   - `index.html`
   - `login.html`
   - `register.html`
   - `vocabulary.html`
   - `write.html`

### app.py
This is the main file of the application. It initializes Flask, configures sessions, and connects to the SQLite database. All routes are defined here.
- `/register`: Allows new users to create an account. Passwords are securely hashed before being stored.
- `/login`: Allows existing users to log in. Sessions are used to remember the logged-in user.
- `/logout`: Clears the session and logs the user out.
- `/`: Displays the user’s writing history.
- `/vocabulary`: Lets users add and view vocabulary words they want to practice.
- `/write`: Allows users to write text and submit it for vocabulary replacement.

The word replacement logic also lives in this file. For each word in the submitted text, the app requests similar words from Datamuse and checks if any of them exist in the user’s saved vocabulary.

### schema.sql
This file defines the structure of the database. It contains three tables:
- `users`: Stores user accounts, hashed passwords, and language level.
- `vocabulary`: Stores words added by users, their type (noun, verb, etc.), and level.
- `writing_history`: Stores original texts, modified texts, dates, and the level used.

Using SQLite was a design choice because it is simple, lightweight, and perfect for a small project.

### Templates Folder
The templates folder contains all HTML files rendered by Flask:
- `layout.html`: The base template used by all pages. It includes the navigation bar and basic structure.
- `register.html`: A form that allows users to create an account.
- `login.html`: A login form for existing users.
- `index.html`: Displays the writing history using tabs to switch between texts.
- `vocabulary.html`: Allows users to add vocabulary words and see a list of saved words.
- `write.html`: The main writing page, showing the original text and the modified text side by side.

Using a base layout helped reduce repeated code and made the project easier to maintain.

### Static Folder
The static folder contains CSS and JavaScript files:
- `styles.css`: Controls the design and layout of the website, including responsiveness.
- `javascript.js`: Manages the tab behavior in the writing history page.

Separating static files from Python code follows good web development practices.

## Design Decisions
One design decision was to store vocabulary per user. This allows each learner to practice words that match their personal level and learning goals. Saving writing history was also important, because it lets users see their progress over time.

The Datamuse API was chosen because it is easy to use and works well for finding similar words without being too complex.

## Future Improvements
The following features could be added in future versions of LexiBoost:

- **Edit and delete vocabulary words**: Allow users to modify or remove words from their vocabulary list, giving them more control as their learning goals change.
- **Predefined vocabulary by level**: Add built-in vocabulary lists for common English levels such as B1, B2, C1, and C2, so users can start practicing without manually adding every word.
- **Grammar and spelling correction**: Extend the application to detect and correct basic grammar and spelling mistakes, making it a more complete writing support tool.
- **Visual highlight for changed words**: Show replaced words with a green underline, so users can easily see what was modified in their text.
- **Word meaning on hover**: Display the meaning of a replaced word when the user moves the mouse over it, helping learners understand and remember new vocabulary.

These improvements show how LexiBoost can grow as I continue learning programming. This project represents a starting point in my journey, and future versions will reflect my progress, new ideas, and a deeper understanding of how language learners practice vocabulary.

## Acknowledgments
This project was developed as part of CS50’s Introduction to Computer Science, offered by Harvard University. The course provided the foundational tools and skills that made LexiBoost possible.
