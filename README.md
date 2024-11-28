
# 项目安装启动

简单说明一下，这是一个以 `fastAPI` 为主的 `图片` 项目存储的简单快速的接口


## 1. dev 环境

```bash

# 创建虚拟开发环境
$ pipenv --python 3.12.2

# 启动开发环境
$ pipenv shell 

# 安装 fastAPI 和对应的 uwsgi 启动服务器进程 (国内为了快速安装，推荐使用清华源)
# python-multipart 是为了 image 文件上传做准备的
$ pip install fastapi "uvicorn[standard]" python-multipart -i https://pypi.tuna.tsinghua.edu.cn/simple

```

下面这个包可选，如果你想更精确的判断当前图片上传类型，可以使用以下`python-magic`包

```bash
# 另外需要注意一点，对于图片类型识别上，对于 python-magic 由于环境不同，安装方式也不同，详情参考： https://pypi.org/project/python-magic/
#  windows 环境下 安装
$ pip install python-magic-bin  python-magic -i https://pypi.tuna.tsinghua.edu.cn/simple

# unbantu/debian
$ sudo apt-get install libmagic1
$ pip install python-magic   -i https://pypi.tuna.tsinghua.edu.cn/simple

```


## 2. production 环境


# 创建第一个项目文件 `main.py`

```python

from typing import Union

from fastapi import FastAPI

app = FastAPI(
    # 注意在生产环境中部署时，最好使用以下参数
    docs_url=None,  # 禁用 Swagger UI
    redoc_url=None  # 禁用 ReDoc
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```


# 配置参数

最好创建对应的服务启动的配置文件,对于当前项目，配置文件，我都放在了 `settings.py` 这个文件夹里面






# 启动项目

## 1. 在开发和测试中启动
```bash
#  reload 表示项目热更新
#  默认端口 http://127.0.0.1:8000
$ uvicorn main:app --reload

# 当前项目测试时，只需要下面方式启动即可，另外需要注意，当前项目没有开启热更新，所以更新完代码需要手动重启
$ python ./main.py   

```

## 2. 在 项目中实际的部署



# 在前端调用当前接口

以下是一个前端的form表单的post提交实例如下,最主要的核心在于，表单在提交时，需要加上 `enctype="multipart/form-data"` 属性 :

```html
    <form action="http://localhost:8000/blog/blog_detail/upload/" method="post"  enctype="multipart/form-data">
        <input type="file" name="image">
        <button type="submit"> submit </button>
    </form>
```



