import logging
import datetime
import azure.functions as func


def main(myblob: func.InputStream):
    timestamp = datetime.datetime.utcnow()
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes\n"
                 f"Blob Content: {myblob.read()}"
                 )
    return '{}'.format(myblob.read())