from flask import Flask, request
import boto3
from nasa_proj2.visual_computing_map.population_industry_detect.dlights import VisionManager
import time
import base64

app = Flask(__name__)
# s3 = boto3.resource("s3", aws_access_key_id="AKIAWKFFMIP2PRIVCDEV", aws_secret_access_key="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")
# bucket = s3.Bucket("nasa-space-app")


@app.route('/vision', methods=["POST"])
def vision():
    # pegar argumentos query
    image = request.args.get("image_base64")
    image_name = request.args.get("image_name") # nome para salvar
    # bucket.download_file(image, image) # nome no bucket, path/nome que sera salvo
    with open(image_name, "wb") as fh:
        fh.write(base64.decodebytes(image.encode()))
    analytics = VisionManager(image_name)
    analytics.execute_detect()
    image_name = f"output_image{time.time()}.jpg"
    analytics.save_image(f'data/{image_name}')
    # bucket.upload_file(image_name, image_name)
    return image_name


if __name__ == '__main__':
    app.run(host="localhost", port=5000)
