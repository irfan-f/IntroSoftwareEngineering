from itsdangerous import (TimedJSONWebSignatureSerializer \
                                  as Serializer, BadSignature, \
                                  SignatureExpired)
import time
import json

# initialization
def generate_auth_token(val, expiration=600):
   # s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
   s = Serializer(val, expires_in=expiration)
   # pass index of user
   ob = s.dumps({'id': 1})
   return ob
def verify_auth_token(val, token):
    s = Serializer(val)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None    # valid token, but expired
    except BadSignature:
        return None    # invalid token
    return 1
