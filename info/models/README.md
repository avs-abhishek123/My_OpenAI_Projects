# models

Entity extraction is one of the oldest NLP use cases, and maybe one of the most common NLP use cases deployed in production today. Traditionally, frameworks like spaCy and NLTK used to be the best choices.

## Old Models

- ### NLTK

  - NLTK is not suited for production but it is a great tool for research projects and ramp up on NLP.
  - NLTK proposes some pre-trained models too, but with less native entities than spaCy.
  - The major problem with these pre-trained models is that they only support the native entities they were trained for… and these entities are rarely useful in real life projects. Most companies want to use NER to extract custom entities like job titles, product names, movie titles, restaurants, etc. The only solution was to create a huge dataset for these new entities through a long and tedious annotation process, and then train a new model. Everytime one wanted to support a new entity, the only solution was to annotate and train again. Great annotation tools like [Prodigy](https://prodi.gy/) really help, but it still requires a lot of work involving one or several human resources on a potentially long period. Hopefully, GPT large language models now solve this problem.

- ### SpaCy

  - SpaCy is well suited for production because it is both easy to use and extremely fast when running in production.
  - SpaCy offers many pre-trained models that one can easily download and start using right away in production.
  - Several native entities are supported out of the box by the spaCy models like addresses, dates, currencies.

- ### GPT-3

  - GPT-3 is a large language model based on Transformers that started revolutionizing the NLP field. 
  - This model was trained on 175B parameters.
  - It is so big that it can understand many human queries without having to be explicitely trained for that.
  - It can pretty much do everything that traditional NLP models did: NER, summarization, translation, classification… and much more.

- #### GPT-3 has a couple of weaknesses though:

  - It is very expensive and can only be used through the OpenAI API.
  - It is quite slow (compared to frameworks like spaCy)
  - It is not necessarily easy to use

> Good news is that open-source alternatives were released in 2021 by EleutherAI (a collective of AI researchers): GPT-J and GPT-NeoX 20B. These NLP models can be deployed by anyone on any server, but in practice it takes some MLOps knowledge and it can be quite costly. We can use the NLP Cloud API that is both affordable and easy to use.
