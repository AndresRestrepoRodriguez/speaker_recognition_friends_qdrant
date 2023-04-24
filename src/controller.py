from identifier.identifier import QdrantService
from vectorizer.titanet_model import Vectorizer
from config import COLLECTION_NAME, QDRANT_HOST, QDRANT_PORT


class Controller():
    def __init__(self) -> None:
        self.vectorizer = Vectorizer()
        self.qdrant_client = QdrantService(
                host=QDRANT_HOST, 
                port=QDRANT_PORT,
            )
        
    
    def get_character_info(self, audio_url: str):
        embedding = self.vectorizer.get_embedding(audio_url)
        character_name, character_score = self.qdrant_client.identify_character(
            collection=COLLECTION_NAME,
            embedding=embedding
        )
        return character_name, character_score