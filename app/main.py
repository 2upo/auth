from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_config 
from app.users import auth_controller
from app.users import user_controller
from fastapi_jwt_auth import AuthJWT

class App(FastAPI):

    config = get_config()

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
            return {'message': 'healthy'}
        
        self.get('/api/healthcheck')(root)


    def init_auth_config(self):
        AuthJWT.load_config(lambda : self.config.AuthSettings())
    

def create_app():
    app = App()
    app.init_auth_config()
    app.init_middleware()
    app.init_healthcheck()
    app.init_router()
    return app

