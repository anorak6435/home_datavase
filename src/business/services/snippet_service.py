from data.snippet_repository import SnippetRepository
from business.models.snippet import Snippet

class SnippetService:
    @staticmethod
    def read_all_snippets():
        return SnippetRepository.fetch_all_snippets()
    
    @staticmethod
    def create_snippet(title, description="", code="", tags=[], links=[]):
        # data validation for now done by default values parameters
        SnippetRepository.create_snippet(title, description, code, tags, links)

    @staticmethod
    def read_one(query : dict):
        return SnippetRepository.fetch_one(query)