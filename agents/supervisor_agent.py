from agents.retriever_agent import retrieve
from agents.verifier_agent import verify_evidence
from agents.writer_agent import generate_answer

def ask(question):

    docs = retrieve(question)

    if not verify_evidence(docs):

        return "Não encontrei evidência suficiente nos documentos."

    answer = generate_answer(question, docs)

    return answer