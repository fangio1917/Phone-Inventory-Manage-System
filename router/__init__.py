from fastapi import FastAPI
from router.api_router import router_api
from controller.login import router_login
from router.middleware import AuthMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(router_login)

# 将子应用程序挂载到主应用程序
api_app = FastAPI()
api_app.include_router(router_api)
api_app.middleware("http")(AuthMiddleware)
app.mount("/api", api_app)

# 静态文件路由
app.mount("/", StaticFiles(directory="web/dist/spa", html=True), name="static")

