# Flask API - Technical Challenge Python

Minimal REST API in Python, using Flask. The API has a single GET endpoint that randomly suggest an app name from a hard-coded list of possible app names.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/hugo27rocha/challengeapi.git
```
2. Navigate to the project directory:

```bash
cd challengeapi
```
3. Create and activate the virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
3. To install the required dependencies:
```bash
python -m pip install Flask==2.2.2
python -m pip install "connexion[swagger-ui]==2.14.1"
```

## Usage

1. Start the Flask API:
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
2. Open another terminal or a web browser and run the following command to make a GET request:
```bash
curl http://localhost:5000/suggest_app
```

