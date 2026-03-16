import os

def check_new_documents():

    files = os.listdir("data")

    if files:
        print("Documentos disponíveis:", files)

    return files


def automation_workflow():

    docs = check_new_documents()

    if docs:
        print("Executando atualização da base vetorial")

        import ingestion.ingest as ingest

        ingest