import logging
import random
from flask import jsonify

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    nums = ""
    count = 0

    while count < 5:
        nums += str(random.randint(0,9))
        count += 1

    return func.HttpResponse(str(nums))
    