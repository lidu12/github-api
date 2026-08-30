# GitHub API Beginner Project

A beginner Python project that demonstrates how to consume a REST API using the `requests` library.

## What this project does

The program sends an HTTP GET request to the GitHub API and retrieves information about the `octocat` GitHub user.

API endpoint:

`https://api.github.com/users/octocat`

The program displays:

* Username
* Name
* Number of public repositories
* Followers
* Following
* GitHub profile URL

## Technologies

* Python
* Requests
* GitHub REST API

## How to run

### 1. Clone the repository

```bash
git clone <repository-url>
cd github-api-beginner
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the program

```bash
python github_api.py
```

## API Flow

```text
Python application
       |
       | HTTP GET request
       v
GitHub REST API
       |
       | JSON response
       v
Python application
       |
       v
Extract and display data
```
