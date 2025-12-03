# Comprehensive Guide to the Final Project: IBT3205 Database Management and Practice

## 1.0 Understanding the Course Landscape and Professor's Expectations

### 1.1 Deconstructing the Course Vision and Objectives

To excel in any academic endeavor, it is strategically vital to first understand the instructor's core vision for the course. For IBT3205, Professor Mehdi Pirahandeh has laid out a clear roadmap that directly informs the expectations for the final project. By deconstructing these objectives, you can align your project work with the fundamental principles being taught, ensuring your final submission is not only technically sound but also conceptually relevant.

The high‑level goals for **"Database Management and Practice"** are designed to provide a comprehensive and practical foundation in the field. These objectives include:

- Understanding the basic concept and structure of database systems.
- Understanding and applying the relational query language SQL.
- Understanding the basic concept of query processing and database optimization.

The course overview expands on these goals, indicating a curriculum that covers fundamental database concepts, progresses from basic to advanced SQL, delves into query processing, and culminates in practical data‑science applications using both SQL and Python. This structure demonstrates a clear emphasis on bridging theoretical knowledge with hands‑on, applicable skills. The final project serves as the primary vehicle to demonstrate mastery of these interconnected topics, linking the course goals directly to how your performance is ultimately measured.

### 1.2 Analyzing the Evaluation Framework and Key Policies

A clear understanding of the course's grading scheme and administrative policies is critical for strategic planning and success. The evaluation framework for IBT3205 highlights the importance of consistent engagement and practical application, with the final project falling under the heavily weighted **"Assignment"** and **"ETC"** categories.

To ensure a fair and productive learning environment, Professor Pirahandeh has established several key policies that have a direct bearing on project work and overall academic conduct:

- **Late Submissions**: Assignments submitted late will incur a penalty or may not be accepted at all. Timely submission of project milestones is therefore essential.
- **Academic Integrity**: All assignments, including the final project, must be your own original work. It is also considered unethical to request an unfair grade increase, and such actions may be reported to university authorities.
- **Attendance**: Punctuality and presence are mandatory. Each absence results in a 2‑point deduction from the final grade, and accumulating five absences will automatically result in an **'F'** grade for the course.
- **Communication**: All official course information and updates will be disseminated via GitHub, the E‑class system, and a dedicated Kakao Group. It is your responsibility to monitor these channels.

This framework of rules and evaluation metrics sets the stage for the final project, which is the primary instrument for assessing your mastery of the course's practical skills.

### 1.3 Interpreting the Final Project's Role and Milestones

The final project is not merely an assignment; it is the capstone of this course. It is designed to be a comprehensive exercise where you synthesize theoretical knowledge with practical application. Professor Pirahandeh emphasizes that the lab sessions and assignments are stepping stones toward building a professional portfolio, which is essential for future job opportunities. The project is the centerpiece of that portfolio for this course.

The core of the final project involves **"designing a database model and implementing a program in Python language using the database."** This requires a combination of conceptual design skills and technical programming ability. The course schedule outlines a clear path with critical milestones to guide the development process:

1. **Week 9**: Project Proposal Submission
2. **Week 13**: Project Demo Submission

Throughout this process, students will have multiple opportunities to present their work and receive constructive feedback. The professor has built multiple tutoring sessions into the course structure to provide guidance and support, ensuring that you have the resources needed to succeed. The following sections will provide the necessary conceptual and technical knowledge to successfully complete these project milestones.

## 2.0 Mastering Foundational Concepts for Your Project

### 2.1 The Database Design Process: From Concept to Schema

A successful database project is built upon a robust and well‑conceived design. This process acts as the blueprint for the entire system, ensuring data integrity, efficiency, and scalability. The design process moves from a high‑level conceptual model (independent of any specific DBMS) to a detailed physical design tailored to the chosen technology.

The main phases of the database design process are:

1. Requirements Collection and Analysis
2. Conceptual Design
3. Logical Design
4. Physical Design

This course focuses heavily on the **conceptual design** phase, which involves modeling the *"mini‑world"* of the application. The primary methodologies for this phase are **Entity‑Relationship (ER) Diagrams** and **UML Class Diagrams**. To illustrate these concepts throughout the lectures, the course uses the **"COMPANY"** database as a recurring example application. This systematic approach ensures that before any code is written, a clear and logical data structure has been established.

### 2.2 Core Principles of the Entity‑Relationship (ER) Model

The ER model is the fundamental tool for conceptual data modeling. It provides a visual language to represent the data requirements of a system, allowing developers and stakeholders to visualize the primary data objects, their properties, and the connections between them. A strong ER model is the cornerstone of a well‑structured relational database.

The ER model is built on three main concepts:

- **Entities**: Objects or concepts about which data is stored (e.g., Machine, Product, Order).
- **Attributes**: Properties that describe an entity. Types include:
  - *Simple*: Cannot be broken down further (e.g., Sex).
  - *Composite*: Can be subdivided (e.g., Address → Street, City, State, Zip).
  - *Multi‑valued*: Can hold multiple values for a single entity (e.g., Color of a Car).
- **Relationships**: Connections that relate two or more distinct entities (e.g., **WORKS_FOR** linking **EMPLOYEE** to **DEPARTMENT**).

Within an entity, a **Key Attribute** uniquely identifies each instance; in ER diagrams, key attributes are typically underlined.

#### Relationship Constraints

- **Cardinality Ratio**: Specifies the maximum number of relationship instances an entity can participate in.
  - *One‑to‑One (1:1)*
  - *One‑to‑Many (1:N)*
  - *Many‑to‑Many (M:N)*
- **Participation Constraint**: Indicates whether the existence of an entity depends on its being related to another entity.
  - *Total (Mandatory)* – shown with a double line.
  - *Partial (Optional)* – shown with a single line.

Once the conceptual ER model is finalized, it serves as the direct input for creating the logical‑level relational model, which is the structure implemented in the database.

### 2.3 Fundamentals of the Relational Data Model

The relational model, first proposed by Dr. E.F. Codd in 1970, provides the logical structure for most modern database systems. All practical work in this course, from writing SQL queries to building the final project application, is based on the principles of this model. It organizes data into two‑dimensional tables, formally known as **relations**.

| Informal Term | Formal Relational Model Term |
|---------------|------------------------------|
| Table         | Relation                     |
| Column Header | Attribute                    |
| Row           | Tuple                        |
| Data Type     | Domain                       |

The integrity and consistency of data within the relational model are maintained through a series of constraints:

- **Superkey**: A set of one or more attributes that uniquely identify a tuple.
- **Key (Candidate Key)**: A minimal superkey.
- **Primary Key**: The chosen candidate key that uniquely identifies tuples.

Two fundamental integrity constraints are at the core of the relational model:

- **Entity Integrity**: No primary key value can be **NULL**.
- **Referential Integrity**: A foreign key must either be **NULL** or match an existing primary key value in the referenced relation.

SQL is the standard language used to define the schema, manipulate the data, and execute queries on databases built upon this powerful and enduring relational model.

## 3.0 Core Technical Skills: Mastering SQL

### 3.1 Basic SQL: Data Definition and Manipulation

Proficiency in basic SQL is the first practical step in bringing a database design to life. This involves using **Data Definition Language (DDL)** to create the database structure and **Data Manipulation Language (DML)** to perform fundamental operations like adding, modifying, and removing data.

Key DDL/DML commands introduced in the course:

- `CREATE TABLE` – defines a new table and its attributes.
- Constraints within `CREATE TABLE`:
  - `PRIMARY KEY`
  - `UNIQUE`
  - `FOREIGN KEY`
- `INSERT` – adds new rows.
- `DELETE` – removes rows (usually with a `WHERE` clause).
- `UPDATE` – modifies existing rows (also typically with a `WHERE` clause).

The basic query structure (`SELECT … FROM … WHERE …`) forms the foundation for all data retrieval, with optional `ORDER BY` for sorting.

### 3.2 Intermediate SQL: Joining Tables and Aggregating Data

The true power of a relational database lies in its ability to **join** related data from multiple tables and to **aggregate** that data into meaningful summaries.

- **JOIN Operations**:
  - `INNER JOIN` – records with matching values in both tables.
  - `LEFT JOIN` – all records from the left table plus matching right‑table records (NULL when no match).
  - `FULL JOIN` – not directly supported in SQLite but can be emulated.
- **Subqueries** – nested `SELECT` statements used as conditions or data sources.
- **Aggregate Functions** – e.g., `COUNT()`, `SUM()`, `AVG()`, `MAX()`, `MIN()`.
- **GROUP BY** – groups rows for aggregation.
- **HAVING** – filters groups after aggregation.

Mastering these intermediate skills enables sophisticated data analysis, essential for building advanced programmatic capabilities into the database.

### 3.3 Advanced SQL: Procedural Logic and Security

Advanced SQL extends the language into a robust programming environment, allowing for reusable code, automation, and secure interaction with external applications.

Key advanced topics covered in Week 10:

- **Accessing SQL from Programming Languages** – using APIs such as JDBC or ODBC.
- **Functions & Procedures** – stored code blocks executed on demand.
- **Triggers** – automatic execution on `INSERT`, `UPDATE`, or `DELETE` events.
- **CASE Statement** – conditional logic within queries (useful for categorisation).

#### Critical Security Consideration: SQL Injection

SQL Injection is a dangerous vulnerability that occurs when applications construct queries by concatenating user‑supplied input. To mitigate this risk, **always use prepared statements and placeholders**. This practice treats user input as data, not executable code, and is essential for building a secure database backend.

## 4.0 Practical Implementation: The Course Toolkit

### 4.1 Your Development Environment: Google Colab and Python

All lab work and project development will be conducted using **Google Colab**, a cloud‑based notebook environment that supports Python programming and data analysis.

Key steps for setting up Colab:

1. Create a new notebook.
2. Connect to a hosted runtime (optionally enable GPU/TPU).
3. Upload necessary files (datasets, scripts).
4. Install required Python packages using `!pip install`.
5. Import datasets (e.g., via the Kaggle API with a personal token).

The primary Python libraries used throughout the course are:

- `sqlite3` – for database interaction.
- `pandas` – for loading query results into DataFrames, enabling easy analysis and visualization.

### 4.2 Implementing CRUD Operations with Python and SQLite

CRUD (Create, Read, Update, Delete) operations form the foundation of any database‑driven application. The course provides an object‑oriented approach for performing these operations by connecting Python code to an SQLite database.

Typical mapping of CRUD to Python functions and SQL commands:

| Operation | Python Function Example | SQL Command |
|-----------|------------------------|-------------|
| Create    | `insert_emp(emp)`      | `INSERT INTO …` |
| Read      | `get_emps_by_name(lastname)` | `SELECT * FROM …` |
| Update    | `update_pay(emp, pay)` | `UPDATE … SET …` |
| Delete    | `remove_emp(emp)`      | `DELETE FROM …` |

Consistent use of **placeholders** (e.g., `:first`, `:last`) within SQL queries is crucial for preventing SQL injection.

## 5.0 Planning and Executing Your Final Project

### 5.1 Step 1: Conceptualization and Database Design

This is the most critical phase. A well‑designed database is easy to build, maintain, and query, whereas a poor design leads to complications later.

**Checklist for Conceptual Design**:

1. **Identify Entities** – primary objects (e.g., Student, Course, Product).
2. **Define Attributes** – list properties, specify types, and identify key attributes.
3. **Establish Relationships** – define how entities interact, including cardinality and participation constraints.
4. **Create the ERD** – visualize the schema using tools like Luna Modeler, ERWin, or ER Studio.
5. **Validate with Normalization** – apply normalization principles to eliminate redundancy.
6. **Normalize the Schema** – ensure at least **Third Normal Form (3NF)** compliance.

The finalized, normalized ERD becomes the primary deliverable for the project proposal and guides the implementation phase.

### 5.2 Step 2: Implementation and Application Development

Translate the design blueprint into a functional database and a working Python application.

Implementation steps:

1. **Translate ERD to Relational Schema** – write `CREATE TABLE` statements with appropriate data types, primary keys, and foreign keys.
2. **Set Up the Environment** – initialize a Google Colab notebook and connect to an SQLite database via `sqlite3.connect()`.
3. **Populate the Database** – use `INSERT` statements (or a data‑generation script) to add realistic sample data.
4. **Develop the Python Application** – create functions or classes to handle all database interactions (CRUD operations).
5. **Build Complex Queries** – implement advanced queries (joins, aggregates, subqueries, CASE statements) to demonstrate mastery.
6. **Ensure Security** – review all query‑building code to guarantee the use of prepared statements and placeholders.

### 5.3 Step 3: Demonstration and Final Submission

The project demo is the culmination of the semester's work and the primary opportunity to showcase the functionality and robustness of your application.

**Success Checklist for the Demo**:

- **Clear Presentation of Design** – justify ERD and schema choices, discussing entities, relationships, cardinality, and normalization.
- **Functional Application** – demonstrate that all core CRUD operations work as expected.
- **Advanced Functionality** – showcase complex queries that provide valuable insights (e.g., summary reports, multi‑table joins).
- **Adherence to Best Practices** – highlight how the project follows database best practices, including 3NF normalization and protection against SQL injection.
- **Code Clarity and Structure** – ensure the Python code is well‑organized, commented, and professional.
- **Alignment with Course Goals** – explicitly connect project features back to the course objectives of understanding database structure and proficient SQL application.

Remember, this project is a key component of your professional portfolio. A well‑executed project will serve as a powerful testament to your skills.
