# Speaker Identification - Friends TV Series

## With Qdrant + TitaNet + Streamlit
-----
This repository contains code for Character Identification in TV series Friends Using Voice.
The demo is based on the vector search engine [Qdrant](https://github.com/qdrant/qdrant), [TitaNet Model](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/titanet_large) from Nvidia and [Streamlit](https://streamlit.io/).

## Requirements
-----
You need [Docker](https://docs.docker.com/get-docker/) and [docker-compose](https://docs.docker.com/compose/install/)
<br></br>
## Deployment and Usage
-----
Clone the repository

```
git clone https://github.com/AndresRestrepoRodriguez/speaker_recognition_friends_qdrant.git
```

Go to the project folder
```
cd speaker_recognition_friends_qdrant/
```

Deploy Services
```
sudo docker-compose -f docker-compose.yml up -d
```

After services is started you can upload initial data to the search engine

First, go to the running container
```
docker exec -it qdrant_demo_friends bash
```

Then, run the following script.
```
python3 upload_embeddings.py
```

After a successful upload, Speaker Identification in Friends TV Series App will be available at port 8050 in the localhost if you deploy locally or in the public IP of your server.

