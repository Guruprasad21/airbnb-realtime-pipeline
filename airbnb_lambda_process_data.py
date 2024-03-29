import pandas as pd
import os
import sys

lib_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lib')
sys.path.append(lib_path)
print(lib_path)

def lambda_handler(event, context):
    try:
        records = [eval(rec['body']) for rec in event]
        data = pd.DataFrame(records)
        data['datediff'] = (pd.to_datetime(data['endDate']) - pd.to_datetime(data['startDate'])).dt.days
        filtered_data= (data[data.datediff>=1].drop(columns = 'datediff'))
        final_data = filtered_data.to_json(orient="records") if filtered_data.shape[0]>=1 else None
        print(final_data)
    except Exception as e:
        print("Error occured while trying to filter airbnb data")
        print(e)
    else:
        return {
            'statusCode': 200,
            'body': final_data
        }
