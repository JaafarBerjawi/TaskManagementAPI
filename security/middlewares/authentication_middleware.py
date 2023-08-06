from functools import wraps
from flask import g, request, jsonify, current_app
from injector import inject, Injector, Module, Binder
from security.data_access.user_data_manager_ABC import UserDataManagerABC
from security.data_access.user_token_data_manager_ABC import UserTokenDataManagerABC
from security.services.user_service import UserService
from security.services.user_token_service import UserTokenService


# class ServiceModule(Module):
#     def configure(self, binder: Binder):
#         from security.data_access_sqlalchemy.user_data_manager import UserDataManager as SQLUserDataManager
#         from security.data_access_sqlalchemy.user_token_data_manager import (UserTokenDataManager as
#                                                                              SQLUserTokenDataManager)
#         binder.bind(UserDataManagerABC, to=SQLUserDataManager)
#         binder.bind(UserService, to=UserService)
#         binder.bind(UserTokenDataManagerABC, to=SQLUserTokenDataManager)
#         binder.bind(UserTokenService, to=UserTokenService)
#

def needs_authentication(view_func):
    @wraps(view_func)
    @inject
    def decorated_view(*args, user_token_service: UserTokenService, **kwargs):
        token = request.headers.get('Authorization')
        if token:
            user_token = user_token_service.get_active_user_token_by_token(token)

            if user_token:
                # If the token is valid, store the user ID in the Flask request context.
                g.user_id = user_token.user_id
            else:
                # If the token is invalid, return a 401 Unauthorized response.
                return jsonify({"message": "Invalid token"}), 401
        else:
            # If no token is provided in the header, return a 401 Unauthorized response.
            return jsonify({"message": "Authorization required"}), 401
        return view_func(*args, **kwargs)
    return decorated_view
