# from .exceptions import NotVerified, UserNotFound
# from fastapi import Depends, HTTPException, status
# from fastapi_jwt_auth import AuthJWT
# from repository import get_by_id

from database import get_db
from fastapi import Depends


class CustomBaseModel():

    _excluded_fields = []

    def to_dict(self):
        res = {k:v for k, v in self.__dict__.items() if k not in self._excluded_fields}
        res.pop("_sa_instance_state")
        return res


# # remove depends
# def require_user(authorize: AuthJWT = Depends()):
#     try:
#         authorize.jwt_required()
#         user_id = authorize.get_jwt_subject()
#         user = get_by_id(user_id)
#         if not user:
#             raise UserNotFound('User no longer exist')

#         if not user.verified:
#             raise NotVerified('You are not verified')

# po karasivee)
    # except Exception as e:
    #     error = e.__class__.__name__
    #     print(error)
    #     if error == 'MissingTokenError':
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED, detail='You are not logged in')
    #     if error == 'UserNotFound':
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED, detail='User no longer exist')
    #     if error == 'NotVerified':
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED, detail='Please verify your account')
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail='Token is invalid or has expired')
    # return user_id

def create_all():
