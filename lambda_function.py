import json
import logging

import redis

logger = logging.getLogger()
logger.setLevel(logging.INFO)

host = ""
port = 6379

r = redis.StrictRedis(host=host, port=port, password=None)


def lambda_handler(event, context):
    try:
        records = event.get('Records', [])
        added = []
        for record in records:
            data = json.loads(record.get('body'))

            key = data.get('key')
            url = data.get('url')
            logger.info("Received message with Key: {} | URL: {}".format(key, url))

            if isinstance(key, str) and isinstance(url, str):
                redis_key = 'sl:{}'.format(key)
                r.set(redis_key, url)
                added.append([key, url])
                logger.info("Added to Redis: {} | URL: {}".format(key, url))

        logger.info("Completed event function. Added {} shortlinks.".format(len(added)))
        return {
            "statusCode": 200,
            "body": json.dumps(added)
        }
    except Exception as e:
        logger.error("Exception hit: {}".format(e))
        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }
