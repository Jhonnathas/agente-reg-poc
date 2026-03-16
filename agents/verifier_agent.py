def verify_evidence(docs):

    if not docs:
        return False

    for doc in docs:
        if len(doc.page_content) > 20:
            return True

    return False