import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executando função de teste.')
    return func.HttpResponse("Função rodou com sucesso!", status_code=200)

print('Hello Azure')
