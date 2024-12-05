
# from pydantic import BaseModel
from fastapi import UploadFile
from typing import Literal,Optional
from datetime import datetime
from uuid import uuid4
from shutil import copyfileobj
from settings import Image_Type
from FileHelper import Filer
# class ImagerFormModule(BaseModel):
#     #  定义一个Image 的模型，用于图片的验证
#     type:str


class SaveImageReturnType():
    saved: bool
    message: str
    path: Optional[str]  # 表示类型可以是 str 或者 None



class Imager():
    def __init__(self,type:Literal['blog_detail','blog_user']) -> None:
        self.filer = Filer
        self.image_type:Literal['blog_detail','blog_user'] = type
        self.avalable_image_type = {
            'image/png':'png',         # png 图片
            'image/svg+xml':'svg',     # svg 图片
            'image/gif':'gif',         # gif 图片
            'image/jpeg':'jpeg',        # jpeg 图片
            'image/bmp':'bmp',    # bmp 图片
        }
        self.allow_image_type = Image_Type
        
    
    def create_image_name(self,image:UploadFile):
        if image.content_type in self.avalable_image_type:
            image_save_type = self.avalable_image_type[image.content_type]
            if image_save_type in self.allow_image_type:
                to_save_image_name = uuid4()
                return f"{to_save_image_name}.{image_save_type}"
            else:
                return None
        else:
            return None
    
    def create_image_full_path(self) -> Optional[str]:
        base_path  = None
        static_path = self.filer.static_path
        if static_path:
            match self.image_type:
                case 'blog_detail':
                    base_path = f'{static_path}blog/blog_detail'   # 使用相对路径表示
                case 'blog_user':
                    base_path = f'{static_path}blog/user_avater'
                case _:
                    base_path = None
            if base_path:
                current_date = datetime.now()
                formatted_date = current_date.strftime("%Y/%m/%d")
                to_save_image_path = f"{base_path}/{formatted_date}"
                return self.filer.check_and_create_path(to_save_image_path,True)
            else:
                return None
        else:
            return None


    def save_image(self,image:UploadFile) -> SaveImageReturnType:
        saved_result = {
            'saved':False,
            'message':'failed to saved',
            'path':None
        }
        try:
            image_name = self.create_image_name(image)
            print('image size',image.size)
            if image_name:
                to_save_image_path = self.create_image_full_path()
                if to_save_image_path:   # 小型图片 比如只有 kb或者 MB 大小可以使用下面的方式存储，如果是大文件，建议利用 aiofiles 去做文件切块处理
                     # 使用 shutil.copyfileobj() 保存文件
                    final_saved_path = f"{to_save_image_path}/{image_name}"
                    with open(final_saved_path, "wb") as buffer:
                        #  以下方式，直接保存图片，并不会修改和直接读取，这种方式会很方便
                        copyfileobj(image.file, buffer)
                    saved_result['saved'] = True
                    saved_result['path'] = final_saved_path
                    saved_result['message'] = "success to save current image !!!"
                    return saved_result
                else:
                    return saved_result
            else:
                saved_result['message'] = f'failed to saved current image, error: target image type [{image.content_type}] is not supported !'
                return saved_result
        except Exception  as err:
            print('there were an error when saving image ',err)
            #  这里会添加对应的日志 打印 功能
            saved_result['message'] = f'failed to saved current image, error: {err}'
            return saved_result