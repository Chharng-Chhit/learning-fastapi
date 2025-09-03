## Clone the project
git clone https://github.com/Chharng-Chhit/learning-fastapi.git

cd learning-fastapi

## Set up virtual environment
python -m venv .venv

## Activate the virtual environment
### On Linux/macOS:
source .venv/bin/activate

### On Windows:
.venv\Scripts\activate

## Install dependencies
pip install -r requirements.txt

## Run the project
uvicorn main:app --reload

## Project Structure
```
app/
  core/
  models/
  routers/
  schemas/
  utilities/
main.py
requirements.txt
README.md
```

## API Documentation
Once running, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for interactive Swagger UI.

## Troubleshooting
- If you get a `ModuleNotFoundError`, ensure you are in the correct directory and the virtual environment is activated.
- For database issues, check your configuration

