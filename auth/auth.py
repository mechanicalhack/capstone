import json
from flask import request, _request_ctx_stack
from functools import wraps
from jose import jwt
from urllib.request import urlopen


AUTH0_DOMAIN = 'dev-r3if9a-n.us.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'castingService'

## AuthError Exception

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

## Auth Header
def get_token_auth_header():
    auth = request.headers.get('Authorization', None)

    if not auth:
        raise AuthError({
            'code': 'authorization_header_mission',
            'description': 'Authorization header is missing.'
        }, 401)
    
    split_auth = auth.split(' ')

    if split_auth[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_bearer',
            'description': 'Authorization header must start with "Bearer".'
        }, 401)
    elif len(split_auth) == 1:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'No Token".'
        }, 401)
    elif len(split_auth) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header is not a bearer token".'
        }, 401)
    
    auth_token = split_auth[1]
    return auth_token

def check_permissions(permission, payload):
    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_permissions',
            'description': 'Permissions not included'
        }, 400)
    
    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'invalid_permissions',
            'description': 'Correct permissions not included'
        }, 401)

def verify_decode_jwt(token):
    jsonurl = urlopen(f'https://{AUTH0_DOMAIN}/.well-known/jwks.json')
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_headers(token)
    rsa_key = {}

    if 'kid' not in unverified_header:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization malformed'
        }, 401)
    
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer='https://' + AUTH0_DOMAIN + '/'
            )

            return payload
        
        except jwt.ExpiredSignatureError:
            raise AuthError({
                'code': 'token_expired',
                'description': 'Token expired.'
            }, 401)
        
        except jwt.JWTClaimsError:
            raise AuthError({
                'code': 'invalid_claims',
                'description': 'Incorrect claims. Please, check the audience and issuer.'
            }, 401)
        except Exception:
            raise AuthError({
                'code': 'invalid_header',
                'description': 'Unable to parse authentication token.'
            }, 400)
        
    raise AuthError({
        'code': 'invalid_header',
        'description': 'Unable to find the appropriate key.'
    }, 400)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = get_token_auth_header()
            payload = verify_decode_jwt(token)
            check_permissions(permission, payload)
            return f(payload, *args, **kwargs)
        return wrapper
    return requires_auth_decorator