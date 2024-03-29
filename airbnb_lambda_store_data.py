import os
import sys

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
sys.path.append(lib_path)
print(lib_path)

import pandas as pd
import json
from datetime import datetime
import traceback


TARGET_BUCKET_NAME = "airbnb-processed-data"



def store_file_to_s3(data):
    try:
        file_name = "airbnb_" + datetime.now().strftime("%Y%m%d%H%M%S")+".json"
        file_path = "s3://{}/{}".format(TARGET_BUCKET_NAME, file_name)
        df = pd.DataFrame(data)
        df.to_json(file_path, orient="records", lines=True)
        print("Stored file successfully at: ", file_path)
    except Exception as e:
        raise e

def lambda_handler(event, context):
    # TODO implement
    try:
        if event[0]['body']:
            data = eval(event[0]['body'])
            store_file_to_s3(data)
            return {
                'statusCode': 200,
                'body': json.dumps('Stored file to s3 successfully')
            }
        else :
            print("Event received: ", event)
            print("Received no records")
    except Exception as e:
        print("Error occurred while trying to store Airbnb data to s3")
        print("Event received:  ")
        print(event)
        print(traceback.format_exc())



