# Churn Analysis Prediction

## Table of Contents
1. [Introduction](#introduction)
2. [Setup and Installation](#setup-and-installation)
3. [Implementation Details](#implementation-details)
   - [Parse Log](#parse-log)
   - [Log Combined](#log-combined)
   - [Features Engineering](#features-engineering)
   - [Model Training](#model-training)
4. [Future Considerations](#future-considerations)
5. [Conclusion](#conclusion)

## Introduction
This project is a Churn Analysis model designed to predict customer churn in the context of HD TV service usage. It allows businesses to protect their revenue, improve customer satisfaction, and gain a competitive edge, all while optimizing resources and ensuring long-term success.

## Setup and Installation
To run the model locally, follow these steps:

1. Install python3.11.9.
2. Set up Python development environment.
3. Clone this repository.

## Implementation Details

### Parse Log
Run the 'Task 1 - Parse Log.py' to select only all of following features for analyzing:
1. Mac 
2. SessionMainMenu
3. AppName
4. LogID
5. Event 
6. ItemID
7. RealTimePlaying 

You will have a new log file with all above features as column name.

### Log Combined
Join the new log file with user_info.txt using 'Task 2 - Combined Log.py' to find customer segmentation.

Then, run the 'Transformed SessionMainMenu.py' to convert the time data type into datetime.

### Feature Engineering
Run 'Task 3 - Feature Engineering.py' for adding more features to define churn in customers.

Then, run 'Label Created.py' to label as Churn '1' and not Churn '0' among customers based on their sevice interation amount.

### Model Training
Run 'Task 4 - Modeling Training.ipynb' to train the prediction model with Random Forest algorithm.
