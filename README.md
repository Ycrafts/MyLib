# MyLib

MyLib is a modern Django-based web application for managing your personal digital library. Discover new books, keep track of your favorites, and enjoy a world of reading at your fingertips.

## Features
- User authentication (sign up, login, logout)
- Search for books
- View book details
- Download book PDFs
- Add/remove books from your favorites
- Responsive, modern UI

## Screenshots

<img src="screenshots/Screenshot%202025-06-22%20155212.png" width="900"/>
<img src="screenshots/Screenshot%202025-06-22%20140408.png" width="900"/>
<img src="screenshots/Screenshot%202025-06-22%20141003.png" width="900"/>
<img src="screenshots/Screenshot%202025-06-22%20141023.png" width="900"/>
<img src="screenshots/Screenshot%202025-06-22%20140336.png" width="900"/>
<img src="screenshots/Screenshot%202025-06-22%20155229.png" width="900"/>

## Getting Started

### Prerequisites
- Python 3.8+
- pip
- (Recommended) virtualenv or pipenv

### Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd MyLib
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or, if using pipenv:
   ```bash
   pipenv install
   pipenv shell
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. (Optional) Load sample data:
   ```bash
   python manage.py loaddata data.json
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage
- Register for a new account or log in.
- Browse the collection, search for books, and view details.
- Download books as PDFs.
- Add books to your favorites for quick access later.

## Project Structure
- `books/` - Book models, views, and templates
- `users/` - User authentication and profile management
- `templates/` - HTML templates
- `static/` - CSS and static assets
- `media/` - Uploaded files (e.g., book covers)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to contribute or open issues for suggestions and bug reports!
