### Live preview:
http://decathlontaskbk.herokuapp.com/

Three endpoints are available:

- /api/movies
- /api/comments
- /api/top

### Setup:

Developed with python 3.6.5, Django 3.0.1 DRF 3.11.0

Assuming that python and virtualenv/virtualenvwrapper is installed and activated.

install all requirements:

```
pip install -r requirements.txt
```

Run migrations:
```python
python manage.py migrate
```

Start server:
```python
python manage.py runserver
```

Your website will be available under

```
http://localhost:8000/
```
