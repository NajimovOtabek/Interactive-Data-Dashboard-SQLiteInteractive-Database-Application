# 📊 Interactive Dashboard Assignment

---

## 🎯 Objective
Demonstrate mastery of database application development by designing and implementing a comprehensive interactive dashboard using **Python**, **SQLite3**, and **Google Colab**. The assignment covers the full data lifecycle:
- Schema design
- Batch data generation
- Advanced SQL queries
- Interactive visualisation

---

## 🛠️ Task Description
You must build a **single, cohesive database application** that satisfies the following requirements.

### 1. Relational Schema
- Create a multi‑table SQLite3 database (minimum **3 related tables**) relevant to a specific domain.

### 2. Batch Data Simulation
- Write Python code to programmatically generate and insert a **large volume of realistic mock data** (batch processing) for performance testing.

### 3. Advanced SQL Implementation
- Implement complex queries via Python functions, including:
  - **Aggregations** (`SUM`, `AVG`, `COUNT`)
  - **Joins** across multiple tables
  - **Window functions** or **sub‑queries**

### 4. Interactive Visualization
- Build a dashboard inside the Colab notebook (e.g., `ipywidgets`, `plotly`, `matplotlib`, or `seaborn`).
- Enable user interaction such as filtering by date, category, or region and display dynamic graphs.

### 5. Constraints
- Must use **Google Colab**, **Python**, and **SQLite3**.
- Code must be **modular** (functions) and **heavily commented**.

---

## 📚 Suggested In‑Depth Scenarios
Choose one scenario below **or design your own** (ensure it meets the complexity requirements).

### 1️⃣ E‑Commerce Inventory & Sales Intelligence
- **Tables:** Customers, Products, Orders, Reviews
- **SQL Challenge:** Compute *Customer Lifetime Value* and identify top‑selling product categories per region using window functions.
- **Visualization:** Heatmap of sales density by region + line graph of daily revenue trends.

### 2️⃣ IoT Sensor Network for Smart Cities
- **Tables:** Sensors, Locations, Readings, MaintenanceLogs
- **SQL Challenge:** Detect pollution anomalies with moving averages and correlate traffic spikes.
- **Visualization:** Real‑time stream for a selected sensor (temperature/pollution).

### 3️⃣ Fintech Portfolio Management System
- **Tables:** Users, Stocks, Transactions, DailyPrices
- **SQL Challenge:** Calculate *Realized vs. Unrealized Gains* and portfolio volatility (standard deviation).
- **Visualization:** Candlestick chart for stock prices + pie chart of portfolio allocation.

### 4️⃣ Healthcare Patient Monitoring Hub
- **Tables:** Patients, Doctors, VitalsLog, Medications
- **SQL Challenge:** Flag high‑risk patients (average heart rate > threshold) and find busiest doctor shift hours.
- **Visualization:** Time‑series of patient vitals + bar chart of medication usage.

### 5️⃣ University Academic Analytics Platform
- **Tables:** Students, Courses, Enrollments, Assignments, Attendance
- **SQL Challenge:** Correlate *Attendance Rate* with *Final Grade* and rank courses by difficulty (average failing rate).
- **Visualization:** Scatter plot of attendance vs. grades with hover details.

---

## 📦 Submission Requirements
Provide a **Google Colab notebook** containing:
1. **Executive Summary** – markdown cell describing the chosen scenario and schema (ER diagram description).
2. **Implementation Code** –
   - Database setup (DDL)
   - Data‑generation script (e.g., `Faker` library)
   - Query logic (Python wrappers around SQL)
   - Interactive dashboard cells (output).
3. **Reflection** – brief (max 200 words) on challenges faced.

---

## 📊 Grading Criteria
| Score | Criteria |
|------:|----------|
| 0/20 | No submission, late, or irrelevant. |
|10/20 | Basic functional DB, data inserted, simple queries; minimal or no interactivity. |
|15/20 | Good schema, substantial data volume, dashboard works but lacks complex SQL insights. |
|20/20 | Outstanding: complex schema, advanced SQL (window functions, aggregates), highly interactive professional dashboard, modular & well‑commented code. |

---

*Good luck!*