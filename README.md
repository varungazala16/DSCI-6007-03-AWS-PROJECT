# DSCI-6007-03-AWS-PROJECT
📈 Stock Market Analysis Using AWS

📌 Project Overview

Stock markets are highly volatile and require robust data processing for accurate insights. This project leverages AWS services to build a scalable stock market analysis pipeline, enabling real-time data processing, storage, and analysis.

🚀 Problem Statement

Traditional methods struggle with real-time stock data processing due to high data volume and velocity. Our solution efficiently handles this challenge by using Kafka on EC2, SageMaker, S3, Glue, and Athena.

🔧 Tech Stack

Amazon EC2 (Kafka for real-time data streaming)
Amazon SageMaker (Model training and prediction)
Amazon S3 (Data storage)
AWS Glue (ETL for structuring data)
Amazon Athena (Fast querying and insights)
🏗️ Architecture

Kafka on EC2 streams stock market data in real-time.
SageMaker processes the data and performs predictions.
Amazon S3 stores the raw and processed data.
AWS Glue transforms and structures the data.
Amazon Athena enables fast querying and visualization.
📅 Project Timeline

Date	Milestone
15-Feb-2025	Data Extraction
22-Feb-2025	Data Transformation
28-Feb-2025	Data Loading
12-Mar-2025	Secure Storage
19-Mar-2025	Monitoring
02-Apr-2025	Data Visualization
23-Apr-2025	Data Analysis
👨‍💻 Team Members

Varun Gazala
Devikinandan
Pravalika
🔍 How to Use

Clone the Repository
git clone https://github.com/yourusername/aws-stock-analysis.git
cd aws-stock-analysis
Deploy AWS Services
Set up Kafka on EC2 for real-time data streaming.
Train and deploy models using SageMaker.
Store data in Amazon S3 and structure it using Glue.
Query insights using Athena.
🛠️ Future Improvements

Integration with AWS Lambda for serverless execution.
Improved machine learning models for higher accuracy.
Dashboard using Amazon QuickSight for interactive insights.
📜 License

This project is licensed under the MIT License.
