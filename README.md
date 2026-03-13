# DatasetExplorer v1.0


DatasetExplorer is a lightweight web application that allows users to upload a CSV file and quickly inspect its structure and quality. Built to demonstrate backend development, data processing with Python, and basic web integration.

---

## Features

- Dataset shape (rows and columns)
- Preview of the first and last rows
- Column data types
- Missing values per column
- Duplicate row count

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Web server and routing |
| pandas | Dataset analysis |
| HTML/CSS | Frontend interface |

---

## Project Structure

```
DatasetExplorer/
│
├── app.py              # Main Flask application
├── analyzer.py         # Dataset analysis logic
│
├── uploads/
│   └── data.csv        # Uploaded CSV files (temporary)
│
├── templates/
│   ├── index.html      # Upload page
│   └── result.html     # Results page
│
└── static/
    └── style.css       # Frontend styles
```

---

## File Descriptions

### `app.py`
Main Flask application. Handles routing, file uploads, and passes analysis results to the templates.

### `analyzer.py`
Contains the dataset analysis logic using pandas. Computes all statistics displayed on the results page.

### `templates/`
HTML pages rendered by Flask — `index.html` for the upload form and `result.html` for displaying results.

### `static/`
CSS styles for the frontend interface.

### `uploads/`
Directory where uploaded CSV files are temporarily stored during processing.

---

## How It Works

1. The user uploads a CSV file through the web interface.
2. Flask saves the file to the `uploads/` directory.
3. The `analyzer` module reads the dataset using pandas.
4. Several dataset statistics are calculated.
5. Results are passed to `result.html` and displayed in the browser.