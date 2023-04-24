import utils as utils
from config import COLLECTION_NAME, DATA_DIR

from controller import Controller
import os


if __name__ == '__main__':

    controller = Controller()

    print("Obtaining audio to create voice prints")
    audio_files = utils.get_audios_folder(os.path.join(DATA_DIR, 'voice'))
    print("Generating the payload")
    payload_data = utils.generate_payload_list(audio_files)
    print("Generating the Voice prints (Embeddings)")
    embeddings = controller.vectorizer.get_embeddings_folder(audio_files)
    vector_size = len(embeddings[0])

    print("Creating Collection")
    controller.qdrant_client.recreate_collection(
        collection=COLLECTION_NAME,
        vector_size=vector_size

    )

    print("Uploading embeddings")
    controller.qdrant_client.upsert_embeddings(
        collection=COLLECTION_NAME,
        embeddings=embeddings,
        payload=payload_data
    )

    print("The embeddings have been uploaded successfully")
