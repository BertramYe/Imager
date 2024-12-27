
# 项目安装启动

简单说明一下，这是一个以 `fastAPI` 为主的 `图片` 项目存储的简单快速的接口


## 1. dev 环境

```bash

# 创建虚拟开发环境
$ pipenv --python 3.12.6

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


```bash
# 对于ubuntu 24.04 以后，由于对于当前不支持直接使用 pip3 安装 ，乃至 pip3 没有自带在默认的系统里面，同时在 pip3 安装时可能遇到 报错 `error: externally-managed-environment`
# 所以为了便捷目前推荐使用 pipx 安装和部署以上的python 安装包

# 以下以 ubuntu 24，04 为例，安装 pipx,
$ sudo apt-get update
$ sudo apt-get install python-pipx
# pipx ensurepath 是一个命令，用于确保 pipx 安装的可执行文件路径已经添加到系统的环境变量中。pipx 是一个用于隔离 Python 应用程序的工具，通过它可以方便地安装和运行 Python 脚本或应用。如果 pipx 的路径没有自动添加到 PATH 中，运行这个命令会帮你添加进去。
$ pipx ensurepath

#  继续安装以上的部署依赖
$ pipx install fastapi "uvicorn[standard]" python-multipart

```

>> 拓展：
`pipx` 不是传统意义上的虚拟环境管理工具（像 venv 或 virtualenv），但它确实使用虚拟环境来隔离每个 Python 应用。pipx 主要用于安装和运行 Python 应用，并且会自动为每个安装的应用创建一个独立的虚拟环境。这样做的目的是避免不同应用之间的依赖冲突。

具体来说，pipx 的工作流程是：

当你用 pipx 安装一个应用时，它会在后台为这个应用创建一个隔离的虚拟环境。
安装的应用会被放置在该虚拟环境中，这样就能确保它的依赖与其他 Python 应用不会冲突。
安装后，pipx 会把这个应用的可执行文件路径添加到系统 PATH 环境变量中，使得你可以直接从命令行运行它，而不需要手动激活虚拟环境。
因此，虽然 pipx 使用虚拟环境的概念，它更像是一个专注于隔离和管理 Python 命令行工具的工具。


> 或者直接抛弃 `pipenv` 或者 `pipx` , 直接使用原始自带的 `venv` 创建虚拟环境`(推荐)`

```bash
# 切换到home的指定项目目录下
$ cd ~/Imager
#  利用 venv 创建一个虚拟环境，并且虚拟环境的文件夹名为 imager_env
$ python3 -m venv imager_env

# 激活虚拟环境 
$ source imager_env/bin/activate

# 安装所需安装包
$ pip3 install fastapi "uvicorn[standard]" python-multipart -i https://pypi.tuna.tsinghua.edu.cn/simple

#  退出虚拟环境
$ deactivate

```

# 配置参数

最好创建对应的服务启动的配置文件,对于当前项目，配置文件，我都放在了 `settings.py` 这个文件夹里面，这里直接省略


# 启动项目

## 1. 在开发和测试中启动

以下命令终端关闭后，当前服务会停止

```bash
#  reload 表示项目热更新
#  默认端口 http://127.0.0.1:8000
$ uvicorn main:app --reload
#  或者手动
$ uvicorn main:app --host 0.0.0.0 --port 8000


# 当前项目测试时，只需要下面方式启动即可，另外需要注意，当前项目没有开启热更新，所以更新完代码需要手动重启
$ python ./main.py   

```

## 2. 在 项目中实际的部署

以下命令即使关闭终端也不会停止

```bash
#  对于生产环境而言，如果项目不是特别复杂，可以使用以下命令让其在后台运行
# nohup：nohup 是一个 Linux/Unix 命令，它的作用是忽略挂起信号（SIGHUP），从而使得命令在终端关闭后依然能够继续运行。通常用于在后台启动长期运行的进程。

# 注意以下命令在运行时，会接受所有 代码中的 print 的打印结果，并放到 uvicorn.log 里面，而如果不想要这种结果，可以使用 logging 模块，自定义日志输出（比较推荐 logging，这也是我这么做的）

# 如果以上设置了 logging 模块 进行当前项目的管理，此时下面的 uvicorn.log 就只会记录项目的启动和重启的记录，由于项目不会经常重启，所以不用关心以下项目文件的大小
$ nohup uvicorn main:app --host 0.0.0.0 --port 8000 > ./Log/uvicorn.log &

```

# 在前端调用当前接口

以下是一个前端的form表单的post提交实例如下,最主要的核心在于，表单在提交时，需要加上 `enctype="multipart/form-data"` 属性 :

```html
    <!-- 以下是 POST 的使用 -->
    <form action="http://localhost:8000/blog/blog_detail/upload/" method="post"  enctype="multipart/form-data">
        <input type="file" name="image">
        <button type="submit"> submit </button>
    </form>

    <!--  以下是GET 在 <img> 标签中的显示使用 -->
    <img src="http://localhost:8000/static/blog/blog_detail/2024/11/28/4caf9be0-2098-4684-adec-17196b022991.png" alt="">
```

如果是异步也可以使用 fetch 去做

```ts
  // 以下是 POST 方法，而对于 GET 方法，基本一样，这里暂时就省略了 
  const form = new FormData();  
  form.append('image',Image)  // 这里的Image是一个图片对象
  const response = await fetch(`http://localhost:8000/blog/blog_detail/upload/`, {  // 对于hander 默认情况下，fetch 会自动添加
                method: 'POST',
                // headers: header, // 自动设置 multipart/form-data 头部
                // headers:{
                //     'Content-Type': contentType as string,
                //     'User-Agent': userAgent as string,
                // },
                mode: 'cors',  // 执行跨域请求
                body: form, // FormData 作为请求体
                // headers:{
                //     ...reqHeaders
        // }
});


```

