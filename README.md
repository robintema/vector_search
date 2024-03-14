# Simple vector database usage
To start the app:
```
docker-compose up
```

In this simple example the following wikipedia pages where used:
https://en.wikipedia.org/wiki/Reinforcement_learning
https://en.wikipedia.org/wiki/Supervised_learning
https://en.wikipedia.org/wiki/Rule-based_machine_learning
https://en.wikipedia.org/wiki/Statistical_classification
https://en.wikipedia.org/wiki/Regression_analysis


These documents are fed into the vector database (Chroma) using GPT4AllEmbeddings for generating the embeddings.

After this we are able to ask questions and we will get document parts that are about the answer. The relevant answers will appear on the command line (Page Content, Source, Score).



Tested using Docker Compose version v2.5.0, Docker version 24.0.5, build 24.0.5-0ubuntu1~22.04.1