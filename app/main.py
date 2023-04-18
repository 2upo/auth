from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_config 
from app.users import auth_controller
from app.users import user_controller
from fastapi_jwt_auth import AuthJWT
from database import Database
from sqlalchemy import text


class App(FastAPI):

    config = get_config()

    def init_database(self):
        assert Database().session().execute( text('select 42'))


    def init_middleware(self):
        self.add_middleware(
            CORSMiddleware,
            allow_origins=[self.config.CLIENT_ORIGIN],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


    def init_router(self):
        self.include_router(auth_controller.router, tags=['Auth'], prefix='/api/auth')
        self.include_router(user_controller.router, tags=['Users'], prefix='/api/users')


    def init_healthcheck(self):
        def root():
            #TODO add exception
            try:
                Database().session().execute( text('select 42'))
            except:
                pass
            return {'message': 'healthy'}
        
        self.get('/api/healthcheck')(root)


    def init_auth_config(self):
        AuthJWT.load_config(self.config.auth_settings)
    

def create_app():
    app = App()
    app.init_database()
    app.init_auth_config()
    app.init_middleware()
    app.init_healthcheck()
    app.init_router()
    return app

