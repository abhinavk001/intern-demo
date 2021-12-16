# intern-demo
Demo of fastAPI

### How to setup
- Clone the repo.
- cd into the project folder. `cd intern-demo`
- Create a virtual environment. `python3 -m venv envname` (mac/linux) / `python -m venv envname` (windows)
- Activate virtual environemnt. `source ./envname/bin/activate` (mac/linux) / `.\Scripts\activate.bat` (windows)
- Install dependencies. `pip install -r requirements.txt`
- Run. `uvicorn main:app --reload`
- Visit http://127.0.0.1:8000/docs#/ for API documentation.

### Testing
- cd into the project folder.
- Run `pytest`
