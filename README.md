# Full Stack Nano Degree Capstone

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/starter` directory and running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

From within the `./starter` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application.

Endpoints
GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
PATCH '/actors/<int:actor_id>'
PATCH '/movies/<int:movie_id>'
DELETE '/actors/<int:actor_id>'
DELETE '/movies/<int:movie_id>'

GET '/actors'

- Fetches all actors from our database.
- Request Arguments: None
- Returns: An array of actor dictionairies with keys: id, name, age, and gender.
  {'id' : "1",
  'name' : "Bob",
  'age' : 47,
  'Gender' : "Male"
  }

GET '/movies'

- Fetches all movies from our database.
- Request Arguments: None
- Returns: An array of movie dictionairies with keys: id, title, and release.
  {'id' : "1",
  'title' : "The Thing",
  'release' : "September 8, 1989"
  }

POST '/actors'

- Adds a new actor to our database.
- Request Arguments: A json dictionary with keys: name, age, and gender, and values of a string, an integer, and a string respectively.
- Returns: An array of actor dictionairies for the added actor and a success value.
  {'success' : True,
  'actors' : [{'id' : "1",
  'name' : "Bob",
  'age' : 47,
  'Gender' : "Male"
  }]

POST '/movies'

- Adds a new movie to our database.
- Request Arguments: A json dictionary with keys: title, and release, and values of a string, and another string respectively.
- Returns: An array of movie dictionairies for the added movie and a success value.
  {'success' : True,
  'movies' : [{'id' : "1",
  'title' : "The Thing",
  'release' : "September 8, 1989"
  }]

PATCH '/actors/<int:actor_id>'

- Updates the given actor in our database.
- Request Arguments: A json dictionary with keys that can include: name, age, and gender, and values of a string, an integer, and a string respectively for whichever key:values are added. Also the id of the actor to update needs to be in the endpoint.
- Returns: An array of actor dictionairies for the updated actor and a success value.
  {'success' : True,
  'actors' : [{'id' : "1",
  'name' : "Bob",
  'age' : 47,
  'Gender' : "Male"
  }]

PATCH '/movies/<int:movie_id>'

- Updates the given movie in our database.
- Request Arguments: A json dictionary with keys that can include: title, and release, and values of a string, and another string respectively for whichever key:values are added. Also the id of the movie to update needs to be in the endpoint.
- Returns: An array of movie dictionairies for the updated movie and a success value.
  {'success' : True,
  'movies' : [{'id' : "1",
  'title' : "The Thing",
  'release' : "September 8, 1989"
  }]

DELETE '/actors/<int:actor_id>'

- Deletes the given actor from our database.
- Request Arguments: The id of the actor to delete needs to be in the endpoint.
- Returns: The id of the actor deleted and a success value.
  {'success' : True,
  'actors' : 1
  }

DELETE '/movies/<int:movie_id>'

- Deletes the given movie from our database.
- Request Arguments: The id of the movie to delete needs to be in the endpoint.
- Returns: The id of the movie deleted and a success value.
  {'success' : True,
  'movies' : 1
  }

```

## Testing

To run the tests, run

```

dropdb agency_test
createdb agency_test
python3 test_app.py

Also included is a postman testing collection.
To run, start the server, import the collection, and run the tests. The included tokens are good for 24 hours.

```
https://git.heroku.com/c-k-capstone.git
```
