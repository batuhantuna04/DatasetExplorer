# Dataset Explorer

Dataset Explorer is a high-performance, visually stunning web application built to analyze CSV datasets in seconds. It transforms raw data into a beautiful, interactive, data-dense dashboard offering immediate insights, statistics, structural previews, and automated visualizations.

---

## 🌟 Key Features

- **Instant Dataset Overview:** Automatically parses dataset shape, feature counts, and structural details.
- **Data Quality Score:** Evaluates your dataset's health (0-100) based on missing values, duplicate ratios, and empty columns to give an automated "Excellent", "Good", "Medium", or "Poor" label.
- **Duplicate Control:** High-level overview of total rows vs. duplicate rows, providing a clear duplicate ratio and status.
- **Smart Data Visualization:** Automatically detects data types and suggests/generates the best visual charts (Histograms, Bar Charts, Pie Charts) using Seaborn & Matplotlib. Features a built-in paginated gallery.
- **Interactive Data Preview:** Tabbed interface to effortlessly toggle between Dataset Head and Dataset Tail.
- **In-depth Statistics:** Neatly formatted HTML summaries for `df.describe()` and `df.info()`.
- **Beautiful UI/UX:** A modern, premium interface with carefully crafted color palettes, an animated score ring, sleek hover animations, and an intuitive file upload system.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Core backend programming language |
| **Flask** | Web framework and routing |
| **Pandas** | Powerful data manipulation and analysis |
| **Matplotlib / Seaborn** | Automated data visualization and charting |
| **HTML / CSS** | Modern, responsive frontend design |

---

## 📂 Project Structure

```text
DatasetExplorer/
│
├── app.py              # Main Flask application and URL routing
├── analyzer.py         # Advanced dataset analysis, scoring, and chart generation logic
│
├── uploads/
│   └── data.csv        # Secure, temporary storage for uploaded files
│
├── templates/
│   ├── index.html      # Hero landing page & upload interface
│   └── result.html     # Comprehensive analysis dashboard with tabs and data wrappers
│
└── static/
    ├── styleindex.css  # Landing page styles
    └── style.css       # Core dashboard styles
```

---

## 🚀 How It Works

1. **Upload:** From the modern landing page, the user selects or drops a `.csv` file. 
2. **Handle:** Flask securely saves the file into the `uploads/` directory.
3. **Analyze:** `analyzer.py` loads the CSV into a Pandas DataFrame. It calculates duplicates, null values, column statistics, robust quality scores, and automatically paints Seaborn charts directly in memory.
4. **Display:** The results are mapped to `result.html` where users can seamlessly view data types, descriptive statistics, interactive tabs, and a beautifully presented chart gallery.

---

## 🏃 Getting Started

1. Clone this repository to your local machine.
2. (Optional but recommended) Create and activate a Python virtual environment.
3. Install the required dependencies:
   ```bash
   pip install flask pandas matplotlib seaborn
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Navigate to `http://127.0.0.1:5000` in your web browser to start exploring your datasets.