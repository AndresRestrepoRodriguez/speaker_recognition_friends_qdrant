import os

CODE_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CODE_DIR)
DATA_DIR = os.path.join(ROOT_DIR, 'data')

COLLECTION_NAME = "friends_characters"
COLUMNS = 4

QDRANT_HOST = os.environ.get("QDRANT_HOST", "localhost")
QDRANT_PORT = os.environ.get("QDRANT_PORT", 6333)


