# DatasetExplorer V 1.0
Dataset Explorer is a simple web application that allows users to upload a CSV dataset and quickly inspect its structure and quality. The tool performs basic exploratory data analysis (EDA) and displays useful information about the dataset directly in the browser.
This project is built to demonstrate backend development, data processing with Python, and basic web integration.
Features
The application provides several useful insights about uploaded datasets:
Dataset shape (rows and columns)
Preview of the first rows
Preview of the last rows
Column data types
Missing values per column
Duplicate row count
These features help users quickly understand the structure and quality of a dataset before performing deeper analysis.
Technologies Used
The project is built using the following technologies:
Python
Flask
pandas
HTML
CSS
Flask handles the web server and routing, while pandas is used for dataset analysis.
Project Structure
DatasetExplorer
│
├── app.py
├── analyzer.py
│
├── uploads
│   └── data.csv
│
├── templates
│   ├── index.html
│   └── result.html
│
└── static
    └── style.css
File Descriptions
app.py
Main Flask application. Handles routing, file uploads, and passes analysis results to templates.
analyzer.py
Contains the dataset analysis logic using pandas.
templates
HTML pages rendered by Flask.
static
CSS styles used for the frontend interface.
uploads
Directory where uploaded CSV files are temporarily stored.
How It Works
The user uploads a CSV file through the web interface.
Flask saves the file in the uploads directory.
The analyzer module reads the dataset using pandas.
Several dataset statistics are calculated.
The results are sent to a result page and displayed in the browser.