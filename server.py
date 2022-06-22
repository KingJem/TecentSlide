# -*- coding: UTF-8 -*-

from io import BytesIO
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from PIL import Image
from centernet_server import CenterNet
import base64

app = FastAPI()
centernet = CenterNet()


class Item(BaseModel):
    image_base64: str = None


@app.post("/post")
async def api(postData: Item):
    image_buffer = base64.b64decode(postData.image_base64)
    image_data = BytesIO(image_buffer)
    img = Image.open(image_data)
    image, left = centernet.detect_image(img)
    image.show()

    return {"item_retval": str(left)}


if __name__ == '__main__':
    uvicorn.run(app, port=8080)
