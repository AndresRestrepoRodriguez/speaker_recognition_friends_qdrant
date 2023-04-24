import nemo.collections.asr as nemo_asr
import utils as utils
import glob as glob


class Vectorizer:

    def __init__(self):
        self.model = self._load_model()

    def _load_model(self):
        return nemo_asr.models.EncDecSpeakerLabelModel.from_pretrained(model_name='titanet_large')

    def get_embedding(self, audio_path: str):
        embedding = self.model.get_embedding(audio_path)
        embedding_numpy = utils.tensor_to_numpy(embedding.squeeze())
        return embedding_numpy.tolist()
    
    def get_embeddings_folder(self, path_audios: str):
        embeddings_list = []
        for audio in path_audios:
            audio_embedding = self.get_embedding(audio)
            embeddings_list.append(audio_embedding)
        return embeddings_list