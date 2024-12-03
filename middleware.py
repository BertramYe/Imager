from starlette.middleware.base import BaseHTTPMiddleware, DispatchFunction,RequestResponseEndpoint
from starlette.types import ASGIApp
from starlette.responses import JSONResponse






class MiddleWare(BaseHTTPMiddleware):
    def __init__(self,app:ASGIApp) -> None:
        super().__init__(app)

    
    async def dispatch(self, request, call_next:RequestResponseEndpoint):
        print('request',request.headers)
        origin = request.headers.get("origin") or request.headers.get("referer")
        # 获取 X-Forwarded-For 头部（可能包含多个 IP 地址）
        x_forwarded_for = request.headers.get("X-Forwarded-For")
        print('origin',origin)
        print('x_forwarded_for',x_forwarded_for)
        print('host',request.headers.get('host'))
        
        # 请求头验证通过，继续处理请求
        response = await call_next(request)
        return response