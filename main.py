from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles    # 静态文件夹的挂在和访问
from BlogRouter.BlogImager import BlogImageRouter
from middleware import MiddleWare     # 导入自定义的中间件类
from settings import DeBug
import uvicorn

app = FastAPI(
        docs_url=None,  # 禁用 Swagger UI
        redoc_url=None, # 禁用 ReDoc
        debug=DeBug
    )

if __name__ == "__main__":
    # 添加中间件，检查域名访问，后续还可以用于鉴权什么的
    app.add_middleware(MiddleWare)
    # 将静态文件夹挂载到应用的 `/static` 路径下，这样我们就可以直接
    app.mount("/static", StaticFiles(directory="static"), name="static")
    # blog 的图片路由
    # tags 参数主要用于组织和分组 API 文档中的路由。
    # 当你在路由中使用 tags 时，FastAPI 会将该路由标记为特定的标签，在自动生成的 Swagger UI 或 ReDoc 文档中，这些标签会帮助你更好地组织和分类 API 路由。
    app.include_router(BlogImageRouter, prefix="/blog", tags=["blog"])
    uvicorn.run(app, host="0.0.0.0", port=8000)
    # uvicorn.run("main:app", host="127.0.0.1", port=8000,reload=True)