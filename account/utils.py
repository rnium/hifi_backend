import base64
from django.core.files.base import ContentFile
import time

def get_base64_image_file(avatar_base64: str) -> ContentFile:
    format, imgstr = avatar_base64.split(";base64,")
    ext = format.split("/")[-1]
    img_data = base64.b64decode(imgstr)
    file_name = f"avatar_{int(time.time())}.{ext}"
    img_file = ContentFile(img_data, name=file_name)
    return img_file