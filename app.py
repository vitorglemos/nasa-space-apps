from flask import Flask, request
import boto3
from nasa_proj2.visual_computing_map.population_industry_detect.dlights import VisionManager
import time
import base64

app = Flask(__name__)


@app.route('/vision', methods=["POST"])
def vision():
    # pegar argumentos query
    image = request.args.get("image_base64")
    image_name = request.args.get("image_name") # nome para salvar
    with open(image_name, "wb") as fh:
        fh.write(base64.decodebytes(image))
    analytics = VisionManager(image_name)
    analytics.execute_detect()
    image_name = f"output_image{time.time()}.jpg"
    analytics.save_image(f'data/{image_name}')
    with open(f'data/{image_name}', "rb") as image_file:
        response = base64.b64encode(image_file.read())
    return response


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
