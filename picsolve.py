from PIL import Image as img
import requests as req
from io import BytesIO


def png2jpg(pic):
    return pic.convert('RGB').save('u.jpg','jpeg')
    
    
def url2img(url):
    return Image.open(BytesIO(response.content))

def read_md(file_dir):
    f=open(file_dir)
    text=""
    for i in f:
        test=text+i
    f.close()
    
def excert_url(txt):
    