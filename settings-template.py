from Types.SettingType import AvaliableImageType,AllowHostType


# 是否开启 debug，默认我这是设置 false ，
# 这与接口运行的错误信息的打印以及 log 保存有关，以及启动等等
DeBug:bool = True

# 允许上传的图片的类型,目前参数只有如下几个
# 'png','svg','gif','jpeg','bmp'
Image_Type:AvaliableImageType = [
    'png','svg','gif','jpeg','bmp'
]

# 允许访问当前网站接口的目标前端项目，涉及到 CORS 的配置问题
# 同时我们会在 middleware 里面做限制 
Allow_Host:AllowHostType = [
   'localhost',
]

Running_Port:int = 8000

#  静态文件存储的路径 默认就是当前路径下的 static
Static_Path:str = 'static'


#  访问的加密
crypt_key:str = ""
crypt_salt = ""


#  日志管理
Logger_Dir = "./Log"


