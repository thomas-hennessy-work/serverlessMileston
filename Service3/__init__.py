import logging
import random
import string
from flask import jsonify

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    chars = ""
    letter_list = string.ascii_lowercase
    count = 0

    while count < 5:
        chars += random.choice(letter_list)
        count += 1

    return func.HttpResponse(chars)