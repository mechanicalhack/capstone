
#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=app.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing
To run the tests, run
```
dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test < casting_agency.psql
python test_flaskr.py
```

## Resources used to make this site
I found how to import environment variables at the following site https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5

I found out how to make a global test variable here:
https://stackoverflow.com/questions/21447740/persist-variable-changes-between-tests-in-unittest

## Bearer Tokens For Authentication

executive_producer_auth_header:

Roles: 

delete:actors	Can delete actors	castingService	

delete:movies	Can delete movies	castingService	

get:actors	Can view actors	castingService	

get:movies	Can view movies	castingService	

patch:actors	Can edit actors	castingService	

patch:movies	Can edit movies	castingService	

post:actors	Can add actors	castingService	

post:movies	Can add movies	castingService

Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE1MDY2OTQsImV4cCI6MTYwMTU5MzA5MywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.NcSb-M-6vKTt8NG7jDB50Gi-rhRsyP7Bipfa74mLp8DnWkeNnNtcpmYFNbKvWEh4tpns5YT_Q30_W3z5k_NVssWJspIUVA1REhKJmi0aqgpusBtp_9WAOjx3Jsa1R7YEoWLhheZqR8GhYjDSSOvjj0MdJDWXwYB0CykYmxRLuJzhMSXxrcDoF0Lwpz1wqHMq8N2IAScKWMrer58iHpOVG0PMy5IoMz3C_Kg2wrRF7RGGVEwk-ebfIdZbVQmXQUQ3rr3J1VKDhlMspvRIRl1q--dNk2bcEGXdfPboc2GL3ZssxpMvZxN04foz7STf7a8I-xzI1cLnIQkW1bo_ZdgrTQ
    
casting_director_auth_header:

Roles: 

delete:actors	Can delete actors	castingService	

get:actors	Can view actors	castingService	

get:movies	Can view movies	castingService	

patch:actors	Can edit actors	castingService	

patch:movies	Can edit movies	castingService	

post:actors	Can add actors	castingService

Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE1MDY2OTQsImV4cCI6MTYwMTU5MzA5MywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.NcSb-M-6vKTt8NG7jDB50Gi-rhRsyP7Bipfa74mLp8DnWkeNnNtcpmYFNbKvWEh4tpns5YT_Q30_W3z5k_NVssWJspIUVA1REhKJmi0aqgpusBtp_9WAOjx3Jsa1R7YEoWLhheZqR8GhYjDSSOvjj0MdJDWXwYB0CykYmxRLuJzhMSXxrcDoF0Lwpz1wqHMq8N2IAScKWMrer58iHpOVG0PMy5IoMz3C_Kg2wrRF7RGGVEwk-ebfIdZbVQmXQUQ3rr3J1VKDhlMspvRIRl1q--dNk2bcEGXdfPboc2GL3ZssxpMvZxN04foz7STf7a8I-xzI1cLnIQkW1bo_ZdgrTQ'

casting_assistant_auth_header:

Roles:

get:actors	Can view actors	castingService	

get:movies	Can view movies	castingService

Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE1MDY2OTQsImV4cCI6MTYwMTU5MzA5MywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.NcSb-M-6vKTt8NG7jDB50Gi-rhRsyP7Bipfa74mLp8DnWkeNnNtcpmYFNbKvWEh4tpns5YT_Q30_W3z5k_NVssWJspIUVA1REhKJmi0aqgpusBtp_9WAOjx3Jsa1R7YEoWLhheZqR8GhYjDSSOvjj0MdJDWXwYB0CykYmxRLuJzhMSXxrcDoF0Lwpz1wqHMq8N2IAScKWMrer58iHpOVG0PMy5IoMz3C_Kg2wrRF7RGGVEwk-ebfIdZbVQmXQUQ3rr3J1VKDhlMspvRIRl1q--dNk2bcEGXdfPboc2GL3ZssxpMvZxN04foz7STf7a8I-xzI1cLnIQkW1bo_ZdgrTQ

## API Documentation

Endpoints
GET '/actors'
GET '/movies'
POST '/actors'
POST '/movies'
PATCH '/actors/<int:id>'
PATCH '/movies/<int:id>'
DELETE '/actors/<int:id>'
DELETE '/movies/<int:id>'


GET '/actors'
- Fetches an array of actor lists
- Request Arguments: None
- Returns:
{
    'success': True,
    'actors': [{
                    'id': actor.id,
                    'name': actor.name,
                    'age': actor.age,
                    'gender': actor.gender
                }]
}

GET '/movies'
- Fetches an array of movie lists
- Request Arguments: None
- Returns: 
{
    'success': True,
    'movies': [{
                    'id': movie.id,
                    'title': movie.title,
                    'releaseDate': movie.releaseDate
                }]
}

POST '/actors'
- Request Argument: <int:id> id of the specific actor that is requested to be added
- Returns:
{
    'success': True,
    'actor': {
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender
             }
}

POST '/movies'
- Request Argument: <int:id> id of the specific movie that is requested to be added
- Returns:
{
    'success': True,
    'movie': {
                'id': actor.id,
                'title': movie.title,
                'releaseDate': movie.releaseDate
             }
}

PATCH '/actors/<int:id>'
- Request Argument: <int:id> id of the specific actor that is requested to be edited
- Returns:
{
    'success': True,
    'actor': {
                'id': actor.id,
                'name': actor.name,
                'age': actor.age,
                'gender': actor.gender
             }
}

PATCH '/movies/<int:id>'
- Request Argument: <int:id> id of the specific movie that is requested to be edited
- Returns:
{
    'success': True,
    'movie': {
                'id': actor.id,
                'title': movie.title,
                'releaseDate': movie.releaseDate
             }
}

DELETE '/actors/<int:id>'
- Request Argument: Argument: <int:id> id of the specific actor that is requested to be deleted
- Returns:
{
    "success": True,
    "delete": actor_to_delete.id
}

DELETE '/movies/<int:id>'
- Request Argument: Argument: <int:id> id of the specific actor that is requested to be deleted
- Returns:
{
    "success": True,
    "delete": movie_to_delete.id
}