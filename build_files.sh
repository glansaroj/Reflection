
# python3.10 -m pip install -r requirements.txt 
# python3.10 manage.py collectstatic --noinput


# Create and activate a virtual environment
python3.10 -m venv env
source env/Scripts/activate

# Install Python dependencies
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput
