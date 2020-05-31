from flask import Flask, request
import boto3
from .nasa_proj2.visual_computing_map.population_industry_detect.dlights import VisionManager
import time

app = Flask(__name__)
s3 = boto3.resource("s3", aws_access_key_id="AKIAWKFFMIP2PRIVCDEV", aws_secret_access_key="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")
bucket = s3.Bucket("nasa-space-app")


@app.route('/vision', methods=["GET"])
def vision():
    # pegar argumentos query
    image = request.args.get("image_name_on_s3")
    bucket.download_file(image, image) # nome no bucket, path/nome que sera salvo
    analytics = VisionManager(image)
    analytics.execute_detect()
    image_name = f"output_image{time.time()}.jpg"
    analytics.save_image(f'data/{image_name}')
    bucket.upload_file(image_name, image_name)
    return image_name



