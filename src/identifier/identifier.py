from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import Dict, List

class QdrantService():
    def __init__(self, host: str, port: int) -> None:
        self.qdrant_client = QdrantClient(
            host=host,
            port=port
        )

    
    def upsert_embeddings(self, collection: str, payload: List[Dict], embeddings: List[List]):
        self.qdrant_client.upload_collection(
            collection_name=collection,
            vectors=embeddings,
            payload=payload,
            ids=None
        )
    

    def identify_character(self, collection: str, embedding: List):
        result = self.qdrant_client.search(
                    collection_name=collection,
                    query_vector=embedding,
                    limit=1,
                )
        character =  result[0]
        character_score = character.score
        character_name = character.payload['name']
        return character_name, character_score
    

    def recreate_collection(self, collection: str, vector_size: int):
        self.qdrant_client.recreate_collection(
        collection_name=collection,
        vectors_config=models.VectorParams(size=vector_size,
                                           distance=models.Distance.COSINE),
    )
    

        