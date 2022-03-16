# Risk appetite Predictor - Stock Market 

## Introduction:

This project is a sister project of the chatbot created to assist the people in understanding the stock market and giving them the listing them with stocks that match their budget and other financial goals. The main hurdle in this was that the common people, who don't kknow about stock market have often no knowledge on what their risk appetite is. This sister project is an attempt to solve the issue.

## Motivation

People generaly have knowledge of their basic finances and how much risk they can take, but when asked to put this in words or select an option of their risk appetite, they don't appear to have confidence when choosing 'high', 'medium', 'low' in the dropdown provided to them. This project asks them simple question and predicts their risk appetite. It would make the people self aware of their risk appetite and would help them in making almost every financial decision of their life.

## Approach

The initial survey and research conducted by the team has found that the risk appetite is based on 5 factors mentioned
1. Age
2. Income
3. Gender
4. Marital status
5. Dependents in family 

We take advantage of this features in the data points to train the machine learning model.

## Solution

It is evident that their will be no public dataset available to cater ou data needs. So we will start with the data augmentation (creating dataset). Then we will understand the corelation between various features and finally we will be able to train the machine learning model. After that we will be writing the pipeline code

## Folder structure
    - readme.md
    - requirements.txt
    - gitignore
    - strategies
        - data_segmentation.md
    - data_synthesizer
        - data_creator.py
        - utils.py
        - data
            - dataset.csv
    - machine_learning
        - trainer.py
        - predictor.py
        - model
            - model.sav
            - model_scaler.pkl

## Steps to run
    - create virtualenv (optional)
    - pip install -r requirements.txt
    - cd machine_learning
    - python predictor.py

    Change values in the demo example given and experiment.
    Enjoy!

## Contribution
    This project is no longer maintained and is provided in AS-IS condition.
    
