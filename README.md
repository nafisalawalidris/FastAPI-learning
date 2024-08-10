# FastAPI Learning Journey 

Welcome to my FastAPI learning journey, this repository documents my progress, projects and insights as I explore the FastAPI framework. 

## Overview

As a Data Scientist with 3 years of experience, I am expanding my skill set to include FastAPI a modern web framework for building APIs with Python. This repo will serve as a portfolio of my learning process and practical implementations.

## Table of Contents

- [Introduction](#introduction)
- [Why FastAPI?](#why-fastapi)
- [Learning Objectives](#learning-objectives)
- [Setup and Installation](#setup-and-installation)
- [Learning Progress](#learning-progress)
  - [1. Setting Up a Virtual Environment](#1-setting-up-a-virtual-environment)
  - [2. Basic FastAPI Application](#2-basic-fastapi-application)
  - [3. API Endpoints and CRUD Operations](#3-api-endpoints-and-crud-operations)
  - [4. Database Integration](#4-database-integration)
  - [5. Authentication and Authorisation](#5-authentication-and-authorisation)
  - [6. Testing and Debugging](#6-testing-and-debugging)
  - [7. Deploying FastAPI Applications](#7-deploying-fastapi-applications)
- [Projects](#projects)
- [Resources](#resources)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository is dedicated to documenting my journey as I learn and master FastAPI a powerful and efficient web framework for building APIs in Python.

## Why FastAPI?

FastAPI is known for its speed, ease of use and modern features like asynchronous programming and automatic validation. It’s an excellent tool for building high-performance APIs and it complements my background in data science by enabling me to create robust scalable APIs for data-driven applications.

## Learning Objectives

- Understand the basics of FastAPI and its core features.
- Build RESTful APIs with CRUD functionality.
- Integrate databases and manage data with FastAPI.
- Implement authentication and authorisation mechanisms.
- Deploy FastAPI applications to production.
- Explore advanced features like background tasks, WebSockets and more.

## Setup and Installation

### 1. Creating a Virtual Environment

```bash
python -m venv fastapi-env
source fastapi-env/bin/activate  # On Windows use `fastapi-env\Scripts\activate`

## 2. Installing Dependencies

Install the necessary dependencies:

```bash
pip install fastapi uvicorn

Additional dependencies can be installed as needed:

pip install sqlalchemy pydantic jinja2 passlib httpx

## 3. Running a Basic FastAPI Application
Create a simple FastAPI application:
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

Run the application using uvicorn:
uvicorn main:app --reload
