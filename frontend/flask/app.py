from flask import Flask, request
from flask_cors import CORS, cross_origin
from PIL import Image
from io import BytesIO
from base64 import b64decode
from map_review import MapReview
import time
import base64

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/vision', methods=["POST"])
@cross_origin()
def vision():
    image = request.json["image_base64"]
    image_name = f"input_image{int(time.time())}.jpg"
    im = Image.open(BytesIO(b64decode(image.split(',')[1])))
    im = im.convert('RGB')
    im.save(image_name)
    analytics = MapReview(image_name)
    analytics.execute()
    analytics.save_image(f'data/{image_name}')
    with open(f'data/{image_name}', "rb") as image_file:
        response = base64.b64encode(image_file.read())
    return b'data:image/png;base64,' + response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
