import logging
import requests

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    enpoint = 'https://milestone-app.documents.azure.com:443/'
    key = 'navoSx6VpzoXZ4WkTwkvbu8d0djlPsc5vXoHr14ubrec5ha40U0A8bU9If4lh6shh3nZ0SAWTdMI2uHUHO4sQA=='

    # <create_cosmos_client>
    client = CosmosClient(endpoint, key)
    
    # <create_database_if_not_exists>
    database_name = 'usernames'
    database = client.create_database_if_not_exists(id=database_name)

    # <create_container_if_not_exists>
    container_name = 'usernamesContainer'
    container = database.create_container_if_not_exists(
        id=container_name, 
        partition_key=PartitionKey(path="/username"),
        offer_throughput=400
    )

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

    # <create_item>
    item_to_add={
        "id"=str(random.randint(0,1000))
        "username"=finalString
    }
    container.create_item(body=item_to_add)

    return func.HttpResponse(f"Welcome to the party {finalString}")