# **Sentiment Analysis and Topic Modelling with Phone Reviews Dataset**
## Information Retrieval Subject

---
### About this project :
- Find the dataset here : [![Linkedin Badge](https://img.shields.io/badge/Kaggle-blue?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/PromptCloudHQ/amazon-reviews-unlocked-mobile-phones)
- Find the development process here : [![GitHub Badge](https://img.shields.io/badge/GitHub-grey?style=flat&logo=github&logoColor=white)](https://github.com/EDafee1/ir-learn.git)
- The goal is to make a dashboard from the phone review dataset to find the good things and the bad things about this specific phone brand.
- Preprocessing :
  - Drop empty rows
  - The brand column for the grouping and the Reviews column is where the process begins.
  - Filter the review value, only reviews in English.
- Method :
  - NLTK is used for the sentiment analysis process.
  - BERTopic is used for the topic modeling process.
  - The output is positive topics and negative topics from the dataset reviews.
- Mean accuracy is 78.65%
- You can find the department here : [![Streamlit Badge](https://img.shields.io/badge/Streamlit-red?style=flat&logo=streamlit&logoColor=white)](https://edafee1-uas-phone-review-sentiment-topics-app-0fllrg.streamlit.app/)
