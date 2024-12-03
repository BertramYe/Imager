
from fastapi import APIRouter
from fastapi import File, UploadFile,Form
from ImageHelper import Imager

BlogImageRouter = APIRouter()
ImagerHandler = Imager('blog_detail')
# 对于图片的获取不需要 get 参数
# 而是直接在挂载完获取即可
# image: UploadFile = File(...)：这是 FastAPI 提供的方式，告诉它从请求中获取文件并将其赋值给 image 变量。
@BlogImageRouter.post('/blog_content/upload/')
# async def upload_Image(image: UploadFile = File(...)): # 注意前端表单要设置 enctype="multipart/form-data"
async def upload_Image(image: UploadFile = Form(...)): # 注意前端表单要设置 enctype="multipart/form-data"
    saved_image_result = {
        'path':None,
        'saved':False,
        'message':'failed to saved image !!!'
    }
    try:
        ImagerHandler.image_type = 'blog_detail'
        print('image uploaded size',image.size)
        print('image uploaded details',image.size)
        if image.size == 0:
            saved_image_result['message'] = 'failed to save image, error: size is 0 !!!'
            return saved_image_result
        saved_result = ImagerHandler.save_image(image)
        saved_image_result = {**saved_result}
    except Exception as err:
        #  这里最好做对应的日志打印
        saved_image_result['message'] = f'failed to saved image , error: {err}'
    return saved_image_result