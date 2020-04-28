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

Also included is a postman testing collection. (cant get it to work on heroku because it is sending to endpoints with 2 '//' instead of 1 '/'? ie:'/actors' is '//actors')
To run, start the server, import the collection, and run the tests. The included tokens are good for 24 hours. Normal postman routes seem to be working fine though.

```
URL where the application is hosted:
https://c-k-capstone.herokuapp.com/
```

casting_assistant_auth_header =
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWU3ZDZiNjliYzBjMTJkYzhiZjciLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYyMzUsImV4cCI6MTU4ODE0MjYzNSwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.a95TT00C2lqpbSyOSXCJpercfEHQov4-mSGcjkRjSIUNLDurjmIA2C8TEHWIVaLuk8fl5Q-DB4rjnogSsQUyAGxdLyTNAv6XDgyTk9KUWz0fWmey3iX9Pkghky_9cbk7-O-wCXJEWrNQEJ0xGJ0PuMDKSXbhIUZ-hnBX_ujfDohr2S-pJQqnEIvzOVriIEy_zyKjip3IRjyYyR7REUwNtQaEV7ZYoY0MCy52xqZzwGJM911MKoXq_aYegQldUSZ-oeO0zg1vjCv-BcAuHJXvFH-APzf5GfdJhtnifAotXcEIW5jwbND3IsaXB05DlpUmKRNe-q6MinsrXcKgg-dHdA

casting_director_auth_header =
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWVhNzZiNjliYzBjMTJkYzhjNTgiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYyODIsImV4cCI6MTU4ODE0MjY4MiwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.F8QhFldNHU3xUVcleOb77EywK1alxsEDemT6OpfGO9otVVglogWYL3fqy8yJwyHNo-n44gzTmFErmLGgyGeRWp7KDEFDvmojD78RLOcYCZqcIfgVh9D3VtV1kvkV2c56jLbneCMI1lM523UhtlgugYsSSAuNa0QqoRj5PFZhp2YPBAitceVvVJ_j3fYBOifG1hSDF8yINt-UvuP09WcrfyYRVN2SYW7jpygg6-qd8sPl36hsdgvxAOJcD-\_ZyuPN4MoNoki5mgcVQey2dShDazK9PU_c-T4bFoTCg5yxNIl0H0UIaa7FoWTLRdk4CKDV6sAv9n-GlKq8Hp94rOpqiA

executive_producer_auth_header =
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImtRbnNxTm4ybGFIeHJuWVV6a0pKdSJ9.eyJpc3MiOiJodHRwczovL2xheGdvZDc3LmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWE3YWY5MzZiNjliYzBjMTJkYzhlOTQiLCJhdWQiOiJhZ2VuY3kiLCJpYXQiOjE1ODgwNTYzMzEsImV4cCI6MTU4ODE0MjczMSwiYXpwIjoiaVR1cnRvS3hQbGhMOW5uUTNwN1Q2YXdxTjBCbGJ0N2siLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.k2Pu57G_8AaqFdudnePttx3FAqr16jTWV1pwgk_4sxVFuMmP7argCwqFHCkP6PdzGZgIrgUrm975_OhtXQIMWS5LvX8SOxSajfME0zlX8Rauec7p2VZ4mtvAX7vEIvfGJermu_wAA_CEsYYvRJXTVFDAjXkFddPz-Fmqj_5VBFo9kJaxwKsO7B1Q8nszv8M0FLQO7Aw5LV9SvFrjETfc7gCV_AkkAIM0V8u9XNsbKmnenowv231K0buOdi-G77d0WxGy8TSPnNu_o-F2Mo1DVjDV6MjZAKnRvZ3GMTHLAKslphmNM9i64onZAwPq-A7D4hzIdtHrinBDlw4A18Lerg
