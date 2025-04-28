# DSCI-6007-03 - AWS Stock-Analytics Pipeline  
📈 *Intraday Market Data on S3, Glue, Athena & Power BI*

---

## 📌 Project Overview
Accurate market insight depends on timely processing of high-frequency price data.  
This repository contains ingestion scripts and ETL code for a **serverless, low-latency stock-analytics platform** on AWS.  
Raw OHLCV bars captured every five minutes are landed in Amazon S3, transformed to partitioned Parquet with AWS Glue, queried via Amazon Athena, and visualised in Power BI Desktop running on a Windows EC2 instance.

---

## 🚀 Problem Statement
Traditional on-prem pipelines cannot ingest and visualise intraday data fast enough without costly databases and manual ETL.  
The goal is to **streamline ingestion, minimise operating cost, and empower analysts to build their own visuals**—all while maintaining sub-minute freshness.

---

## 🔧 Tech Stack

| Layer | Service | Purpose |
|-------|---------|---------|
| Ingestion | **Python script on Windows EC2** (Task Scheduler) | Calls Alpha Vantage API every 5 min; uploads CSV to S3 |
| Storage   | **Amazon S3** | Durable, cheap object store for raw & transformed data |
| ETL       | **AWS Glue** | Converts CSV → Parquet, enforces schema, registers tables |
| Query     | **Amazon Athena** | Serverless SQL over Parquet for ad-hoc analysis |
| Visual    | **Power BI Desktop** on the same EC2 host | Analysts create their own charts via Athena ODBC driver |
| Ops / Monitoring | **CloudWatch Logs & Alarms** | Tracks ingestion success, latency, and usage metrics |

---

## 🏗️ Architecture

