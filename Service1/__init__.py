import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    randNumsResponce = requests.get('https://serverlessmilestone.azurewebsites.net/api/Service2')
    randCharsResponce = requests.get('https://serverlessmilestone.azurewebsites.net/api/Service3')

    randNums = str(randNumsResponce.content)
    randChars = str(randCharsResponce.content)

    count = 0
    finalString = ""

    while count < 5:
        finalString += str(randNums[count+2])
        finalString += str(randChars[count+2])
        count += 1

    return func.HttpResponse(f"Welcome to the party {finalString}")