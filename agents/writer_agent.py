from langchain_community.chat_models import ChatOllama


llm = ChatOllama(model="phi3")

def generate_answer(question, docs):

    context = ""

    citations = []

    for d in docs:
        context += d.page_content + "\n"
        citations.append(
            f"(Fonte: página {d.metadata.get('page', '?')})"
        )

    prompt = f"""
Responda usando apenas o contexto abaixo.

Contexto:
{context}

Pergunta: {question}

Inclua citações de página.
"""

    response = llm.invoke(prompt)

    return response.content + "\n\n" + "\n".join(citations)