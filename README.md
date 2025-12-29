# Anomaly-Detection-Project

Detecting anomalies in cloud systems using machine learning techniques, with support for centralized and federated learning workflows.

---

## 📌 Overview

Modern cloud infrastructures generate large volumes of system metrics such as CPU usage, memory consumption, disk I/O, and network traffic. Detecting anomalous behavior in these metrics is crucial for:

- Early failure detection
- Performance monitoring
- Security threat identification

This project implements an **unsupervised anomaly detection pipeline** using **autoencoders**, with optional **federated learning** support to enable privacy-preserving, decentralized model training.

---

## 🧠 Core Concepts Used

- **Unsupervised Learning** – No labeled anomalies required
- **Autoencoders** – Reconstruction-error-based anomaly detection
- **Feature Engineering** – Rolling statistics over time-series data
- **Federated Learning** – Distributed training without sharing raw data
- **Threshold-based Detection** – Statistical decision boundaries

---

## 🗂️ Project Structure

```text
anomaly_fl_project/
│
├── data/
│   ├── raw/                # Raw system metrics (CSV or logs)
│   ├── processed/          # Cleaned and normalized data
│
├── feature_engineering/
│   └── features.py         # Rolling mean & std feature extraction
│
├── model/
│   ├── autoencoder.py      # Autoencoder architecture
│   └── train_centralized.py# Centralized training pipeline
│
├── thresholding/
│   └── threshold.py        # Anomaly threshold computation
│
├── evaluation/
│   └── metrics.py          # Evaluation metrics (precision, recall, etc.)
│
├── federated/
│   ├── client.py           # Federated learning client
│   ├── server.py           # Federated aggregation server
│   └── data_partition.py   # Client-side data splitting
│
├── experiments/            # Logs, results, and experiments
│
└── README.md
