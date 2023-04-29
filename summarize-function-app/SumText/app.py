import json
import numpy as np
from transformers import pipeline
import torch



def lambda_handler(event, context):
    try:
        summarizer = pipeline("summarization", model="/opt/ml/model/facebook", tokenizer="/opt/ml/model/facebook")
        raw_string= r'{}'.format(event['body'])
        body=json.loads(raw_string)
        original_text=body['text']

        summary = summarizer(original_text,min_length=5, max_length=8)
        final={'output':summary}
        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps(final)
        }
    
    except Exception as e:
        return {
            'statusCode': 500,
             "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                "Access-Control-Allow-Credentials": True

            },
            'body': json.dumps(str(e))
        }