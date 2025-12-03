# Project Walkthrough & Execution Guide

This document provides a step-by-step guide to running the **E-Commerce Inventory & Sales Intelligence Dashboard**. The project has been upgraded to a professional standard, featuring a robust SQLite backend, advanced SQL analysis, and a high-performance interactive dashboard using **Plotly**.

## 1. Prerequisites

Before running the project, ensure you have the following installed:
- **Python 3.8** or higher
- **pip** (Python package installer)
- **Git** (for cloning the repository)

## 2. Installation & Setup

### Option A: Local Execution (Recommended)

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/NajimovOtabek/Interactive-Data-Dashboard-SQLiteInteractive-Database-Application.git
    cd Interactive-Data-Dashboard-SQLiteInteractive-Database-Application
    ```

2.  **Create a Virtual Environment**:
    It is best practice to use a virtual environment to manage dependencies.
    ```bash
    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # Windows
    # venv\Scripts\activate
    ```

3.  **Install Dependencies**:
    Install all required libraries, including `plotly`, `pandas`, and `faker`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook notebooks/interactive_dashboard.ipynb
    ```

### Option B: Google Colab

1.  Download the `notebooks/interactive_dashboard.ipynb` file from this repository.
2.  Go to [Google Colab](https://colab.research.google.com/).
3.  Upload the notebook file.
4.  The notebook is self-contained and will install necessary packages (like `faker` and `plotly`) in the first cell.

## 3. Running the Dashboard

Once the notebook is open:

1.  **Run All Cells**: Click "Runtime" > "Run all" (or "Cell" > "Run All").
2.  **Data Generation**: The notebook will automatically:
    - Create the SQLite database schema.
    - Generate realistic mock data for Customers, Products, Orders, and Reviews.
    - Perform advanced SQL analysis (Ranking, Trends, Aggregations).
3.  **View the Dashboard**: Scroll to the bottom of the notebook to see the **Executive E-Commerce Dashboard**.

## 4. Using the Professional Dashboard

The dashboard is designed for executive-level insights.

-   **KPI Cards**: At the top, view real-time metrics for **Total Revenue**, **Total Orders**, and **Avg Order Value**.
-   **Filters**: Use the dropdowns to filter data by:
    -   **Region**: North, South, East, West, Central.
    -   **Category**: Electronics, Clothing, Home, Books, Sports.
-   **Interactive Charts**:
    -   **Daily Revenue Trend**: Hover over the line chart to see exact values. Use the slider at the bottom to zoom in on specific date ranges.
    -   **Revenue by Category**: A donut chart showing the revenue distribution.
    -   **Top 10 Products**: A horizontal bar chart ranking the best-selling items.
    -   **Sales by Day of Week**: Analyze which days generate the most revenue.

## 5. Verification & Testing

To verify the project is working correctly:
1.  **Check Data**: Ensure the "Data Generation" cell outputs "Data generation complete."
2.  **Check SQL**: Verify that the SQL analysis cells output DataFrames (tables) with data.
3.  **Check Dashboard**: Change the "Region" filter to "North".
    -   Observe the KPI cards updating.
    -   Check if the "Daily Revenue Trend" chart redraws.
    -   Ensure the "Revenue by Category" chart reflects the regional data.

## 6. Project Structure

-   `notebooks/interactive_dashboard.ipynb`: The core application logic.
-   `sql/schema.sql`: Defines the 5-table relational database schema.
-   `sql/queries.sql`: Contains the advanced SQL queries used for analysis.
-   `requirements.txt`: List of Python dependencies.
