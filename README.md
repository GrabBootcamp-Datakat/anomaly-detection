# Anomaly Detection on Spark with Machine Learning Models

This project demonstrates how to perform anomaly detection using machine learning models on Apache Spark. It is designed to handle large-scale datasets efficiently by leveraging Spark's distributed computing capabilities.

## Overview

Anomaly detection is crucial in various domains such as fraud detection, network security, and system health monitoring. This repository provides a framework to preprocess data, engineer features, train machine learning models, and detect anomalies in a scalable manner using PySpark.

## Features

* **Data Preprocessing**: Clean and prepare raw data for analysis.
* **Feature Engineering**: Generate relevant features to improve model performance.
* **Model Training**: Train machine learning models suitable for anomaly detection.
* **Anomaly Detection**: Identify outliers or anomalies in the dataset.

## Getting Started

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/GrabBootcamp-Datakat/anomaly-detection.git
   cd anomaly-detection
   ```

2. **Install required Python packages**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Feature Engineering**

   Apply feature engineering techniques using the `merge.py` script and add data directory path.

   ```bash
   python merge.py data_path
   ```

2. **Model Training and Anomaly Detection**

   Train your model and detect anomalies using the `label.py` script.

   ```bash
   python label.py 
   ```

3. **Data Preprocessing**

   Use the `parse.py` script to preprocess your raw data.

   ```bash
   python parse/main.py
   ```
   
4. **Training and Demo with models**
5. 
   Go to the demo directory
   
   ```bash
   cd module/demo
   ```

   Use the `*_demo.py` script to preprocess train whichever model you desired in the listed options. Example:

   ```bash
   python decision_tree_demo.py
   ```
   
   Remember to replace the data paths with your actual directories.

## Project Structure

```
anomaly-detection/
├── module/                               # Directory to train and demo models
anomaly-detection/
├── module/
│   ├── demo/
│   │   ├── decision_tree_demo.py
│   │   ├── invariants_miner_demo.py
│   │   ├── invariants_miner_without_labels_demo.py
│   │   ├── isolation_forecast_demo.py
│   │   ├── log_clustering_demo.py
│   │   ├── lr_demo.py
│   │   └── svm_demo.py
│   └── train/
│       ├── models/
│       │   ├── **init**.py
│       │   ├── decision_tree.py
│       │   ├── invariants_miner.py
│       │   ├── isolation_forest.py
│       │   ├── log_clustering.py
│       │   ├── lr.py
│       │   └── svm_demo.py
│       ├── dataloader.py
│       ├── preprocessing.py
│       └── utils.py
├── parse/                               # Script for data preprocessing   
│   └── drain.py
│   └── main.py
├── merge.py                             # Script for feature engineering
├── label.py                             # Script for model training and anomaly detection
├── requirements.txt                     # Python dependencies
└── README.md                            # Project documentation
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## Acknowledgments

This project is part of the GrabBootcamp initiative, aiming to provide practical machine learning solutions for real-world problems.
