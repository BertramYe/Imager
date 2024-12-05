from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction,RequestResponseEndpoint
from starlette.types import ASGIApp
from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware





class MiddleWare(CORSMiddleware):
    def __init__(self,app:ASGIApp) -> None:
        super().__init__(app,
                            allow_origins=["*"],  # 您可以指定允许的域名列表
                            allow_credentials=True,  # 是否允许跨域请求携带凭据（如 cookies、HTTP认证信息或客户端证书）。如果设置为 True，浏览器将会在跨域请求中携带凭据。如果设置为 False，则不会允许在跨域请求中携带凭据。
                            # allow_methods=["*"],  # 允许所有方法
                            allow_methods=["GET",'POST'],  # 允许所有方法
                            allow_headers=["*"],  # 允许所有请求头
                         )

    
    async def dispatch(self, request, call_next:RequestResponseEndpoint):
        try:
            print('request',request)
            print('headers',request.headers)
            origin = request.headers.get("origin") or request.headers.get("referer")
            # 获取 X-Forwarded-For 头部（可能包含多个 IP 地址）
            x_forwarded_for = request.headers.get("X-Forwarded-For")
            print('origin',origin)
            print('x_forwarded_for',x_forwarded_for)
            print('host',request.headers.get('host'))
            
            # 请求头验证通过，继续处理请求
            response = await call_next(request)
            print('response',response)
        except Exception as er:
            print('error',er)
        return response