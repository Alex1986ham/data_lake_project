# Project: Data Lake


## Introduction

The music streaming startup, Sparkify, has grown and wants to convert its data warehouse into a Data Lake. The app's data is stored in S3 as JSON files. The log file contains the user activity of the app. The songs file contains metadata for the songs in the app.

The task is to build an ETL pipeline that extracts the data from S3, processes it with Spark, and loads the data back into S3 as a set of dimension tables. With the help of this star scheme, the analysis team can gain insight into which songs the users listen to.

The database can be tested using the SQLs of the analysis team. 


## Project

The aim of the project is to load raw data from S3, process them with Spark and then load them back into S3 in the form of a star scheme.


## Procedure

The database was modelled with the Star Schema model. Using Apache Spark, the DAten were built on a cluster based on Amazon Elastic MapReduce that allows developers to process large amounts of data easily and cost-effectively. There is a fact table, "songplays" and four other dimension tables with the names "users", "songs", "artists" and "time". The Pipline writes all information from JSON files, which are also stored in the Cloud (S3) with Python into the cluster to transfer. Then, after processing the data, we have the tables back in a repository stored in S3.
