from data.mongodb import MongoDB_Session
from data.snippet_schema import SnippetInDB, snippet_helper

DATABASE="progmod" 
COLLECTION="snippets"

class SnippetRepository:

    @staticmethod
    def fetch_all_snippets():
        session = MongoDB_Session(DATABASE, COLLECTION)
        return list(map(lambda sn: snippet_helper(sn), session.fetch_all()))
    
    @staticmethod
    def create_snippet(title, description="", code="", tags=[], links=[]):
        session = MongoDB_Session(DATABASE, COLLECTION)
        snippet = SnippetInDB(title=title, description=description, code=code,tags=tags,links=links)
        session.create(item=snippet)

    @staticmethod
    def fetch_one_by_id(id: str):
        session = MongoDB_Session(DATABASE, COLLECTION)
        res = session.fetch_one_by_id(id)
        if not res:
            return None
        return snippet_helper(item=res)