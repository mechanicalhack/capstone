
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

The following bearer tolkens can be used for testing the live application on heroku. Also attached are the Roles that each bearer token has.

# executive_producer_auth_header:

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

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYzNTdhNTQzOGQxYTIwMDZkMjExNzdhIiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUzNjgsImV4cCI6MTYwMTkyMTc2NywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.Cij7tbfqc2SGCpIj24cbjJCwybqvosE8jUTG3Y2EYA2K08qQmp1G9v8WC9FUOEn0vaEPtTJcjpNXxbzx_QD5stln7UoCL5cfvTNKJBhijWW8TMEcOgqhp0jYxGrWW6FxF123Y9e30sRRRyDFtxKABsVOTiqGeuyWK1ytG01rEFSDgI-6nDDxeQd8W9RklKEWSLogbHsVOseaLoWuq8kmSl7zqgnv9kP_nRvBK03qbnxKo4Nfc5in9MXb6mhAHvtxSaQkr6y6JsIJpFA0zxB9PeSY6Vl6LVPr_fzMRutmEV2ku0f9ngIrvbQYpJxT8Brkl_ExcwVvP-cd7INavJV_cw
    
# casting_director_auth_header:

Roles: 

delete:actors	Can delete actors	castingService	

get:actors	Can view actors	castingService	

get:movies	Can view movies	castingService	

patch:actors	Can edit actors	castingService	

patch:movies	Can edit movies	castingService	

post:actors	Can add actors	castingService

Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyZmYxODc2OGRlOTkwMDM3NDZlYTA3IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUyNDcsImV4cCI6MTYwMTkyMTY0NiwiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.g-jXlKuLsNDKgm3iK-d_vYwkzvXgQYA4yrN_PzufnFmsHpjYs_WSZkGmzm5z7WoO0eOXGMbdb7J-DzUldq771cBWD6amvSJCrgzbJafoUjJoPcqt-wIK8CG9ds6xcXuREJGHftIX1ug1ovPHVxtzZyH2QuRluPxhbdqKe7von5d2FQLeE3dgXDIUHJ3gC9WZ0WGz8BuOFfNUTHoNYTYl6fmvQjEFkomxa6mSVhOs4C1ua32niblvIyP8W144zNjp98OJBvjJ3wVPkumwmhgraAfoSw0iKGVRxvcL1lfehBQfVKSvnaegA2vlmVdZWrTfccyojAgXdiy7ppAnvA_

# casting_assistant_auth_header:

Roles:

get:actors	Can view actors	castingService	

get:movies	Can view movies	castingService

Bearer Token:

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Il9YZGtlS1QxNFEtU1dZQUprOFlVQyJ9.eyJpc3MiOiJodHRwczovL2Rldi1yM2lmOWEtbi51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWY3YTAwMzNkYzViMjMwMDc4YWQ3NmY1IiwiYXVkIjoiY2FzdGluZ1NlcnZpY2UiLCJpYXQiOjE2MDE4MzUxMDQsImV4cCI6MTYwMTkyMTUwMywiYXpwIjoiQzJzR3BRaEh4WDhEQ3JvaE5nTTkzT3NRdWdweVlzNjMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.U4sUKNsYLJmg4tguefy8j3cboZyKBWbqKIlh4FG1SCWBHzPO0hkml1cp9MFgP_X215_IlCybiSybur1rLU2DAS95g1JmXR6kGHZxs_Ff4AflMHDJnLSR2yMFU3IweBbRu5VVTPmmiQOo1PuUy_NU1UIZybCRbwuggmcRcjm2VdjtgPr06baGh1qH7Lv6ijiydo5QHK7v9Jy3i9QT3-9ndcUFH6SJZQzjLTyj-gaJRNKK2LhW-Ky4KPCmk8yQHMfVI4EVF6VePOZZDDE97Diw3sae5Yp58cUzgzpMFWKsOy1DK_OAalu9fRx3JCLkXTCWLcbbR8nnVUUOmrxKVQIZaA

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