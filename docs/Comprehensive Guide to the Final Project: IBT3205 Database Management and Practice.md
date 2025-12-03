Comprehensive Guide to the Final Project: IBT3205 Database Management and Practice

1.0 Understanding the Course Landscape and Professor's Expectations

1.1 Deconstructing the Course Vision and Objectives

To excel in any academic endeavor, it is strategically vital to first understand the instructor's core vision for the course. For IBT3205, Professor Mehdi Pirahandeh has laid out a clear roadmap that directly informs the expectations for the final project. By deconstructing these objectives, you can align your project work with the fundamental principles being taught, ensuring your final submission is not only technically sound but also conceptually relevant.

The high-level goals for "Database Management and Practice" are designed to provide a comprehensive and practical foundation in the field. These objectives include:

* Understanding the basic concept and structure of database systems.
* Understanding and applying the relational query language SQL.
* Understanding the basic concept of query processing and database optimization.

The course overview expands on these goals, indicating a curriculum that covers fundamental database concepts, progresses from basic to advanced SQL, delves into query processing, and culminates in practical data science applications using both SQL and Python. This structure demonstrates a clear emphasis on bridging theoretical knowledge with hands-on, applicable skills. The final project serves as the primary vehicle to demonstrate mastery of these interconnected topics, linking the course goals directly to how your performance is ultimately measured.

1.2 Analyzing the Evaluation Framework and Key Policies

A clear understanding of the course's grading scheme and administrative policies is critical for strategic planning and success. The evaluation framework for IBT3205 highlights the importance of consistent engagement and practical application, with the final project falling under the heavily weighted "Assignment" and "ETC" categories.

The course evaluation is broken down as follows:


To ensure a fair and productive learning environment, Professor Pirahandeh has established several key policies that have a direct bearing on project work and overall academic conduct:

* Late Submissions: Assignments submitted late will incur a penalty or may not be accepted at all. Timely submission of project milestones is therefore essential.
* Academic Integrity: All assignments, including the final project, must be your own original work. It is also considered unethical to request an unfair grade increase, and such actions may be reported to university authorities.
* Attendance: Punctuality and presence are mandatory. Each absence results in a 2-point deduction from the final grade, and accumulating five absences will automatically result in an 'F' grade for the course.
* Communication: All official course information and updates will be disseminated via GitHub, the E-class system, and a dedicated Kakao Group. It is your responsibility to monitor these channels.

This framework of rules and evaluation metrics sets the stage for the final project, which is the primary instrument for assessing your mastery of the course's practical skills.

1.3 Interpreting the Final Project's Role and Milestones

The final project is not merely an assignment; it is the capstone of this course. It is designed to be a comprehensive exercise where you synthesize theoretical knowledge with practical application. Professor Pirahandeh emphasizes that the lab sessions and assignments are stepping stones toward building a professional portfolio, which is essential for future job opportunities. The project is the centerpiece of that portfolio for this course.

The core of the final project involves "designing a database model and implementing a program in Python language using the database." This requires a combination of conceptual design skills and technical programming ability. The course schedule outlines a clear path with critical milestones to guide the development process:

1. Week 9: Project Proposal Submission
2. Week 13: Project Demo Submission

Throughout this process, students will have multiple opportunities to present their work and receive constructive feedback. The professor has built multiple tutoring sessions into the course structure to provide guidance and support, ensuring that you have the resources needed to succeed. The following sections will provide the necessary conceptual and technical knowledge to successfully complete these project milestones.

2.0 Mastering Foundational Concepts for Your Project

2.1 The Database Design Process: From Concept to Schema

A successful database project is built upon a robust and well-conceived design. This process acts as the blueprint for the entire system, ensuring data integrity, efficiency, and scalability. The design process moves from a high-level conceptual model, which is independent of any specific database management system (DBMS), to a detailed physical design tailored to the chosen technology.

The main phases of the database design process, as illustrated in the course materials, are as follows:

1. Requirements Collection and Analysis
2. Conceptual Design
3. Logical Design
4. Physical Design

This course focuses heavily on the conceptual design phase, which involves modeling the "mini-world" of the application. The primary methodologies for this phase are Entity-Relationship (ER) Diagrams and UML Class Diagrams. To illustrate these concepts throughout the lectures, the course uses the "COMPANY" database as a recurring example application. This systematic approach ensures that before any code is written, a clear and logical data structure has been established.

2.2 Core Principles of the Entity-Relationship (ER) Model

The Entity-Relationship (ER) model is the fundamental tool for conceptual data modeling. It provides a visual language to represent the data requirements of a system, allowing developers and stakeholders to visualize the primary data objects, their properties, and the connections between them. A strong ER model is the cornerstone of a well-structured relational database.

The ER model is built on three main concepts:

* Entities: Objects or concepts about which data is stored. They can be tangible (like a Machine or Product) or intangible (like an Order).
* Attributes: The properties or characteristics that describe an entity. Attributes can be classified into several types:
  * Simple: An attribute that cannot be broken down further (e.g., Sex from the EMPLOYEE entity).
  * Composite: An attribute that can be subdivided into smaller parts (e.g., Address can be broken down into Street_address, City, State, and Zip).
  * Multi-valued: An attribute that can hold multiple values for a single entity (e.g., the Color of a CAR).
* Relationships: A connection that relates two or more distinct entities with a specific meaning. For example, a WORKS_FOR relationship connects an EMPLOYEE entity to a DEPARTMENT entity.

Within an entity, a Key Attribute is a property whose value uniquely identifies each specific entity instance. In ER diagrams, key attributes are typically underlined.

Relationship Constraints

To accurately model the real world, relationships are further defined by constraints that govern how entities can participate in them.

* Cardinality Ratio: This specifies the maximum number of relationship instances that an entity can participate in. The common ratios are:
  * One-to-One (1:1): An employee manages one department, and a department is managed by one employee.
  * One-to-Many (1:N): One department can have many employees, but each employee works for only one department.
  * Many-to-Many (M:N): An employee can work on multiple projects, and a project can have multiple employees.
* Participation Constraint: This specifies whether the existence of an entity depends on its being related to another entity.
  * Total (Mandatory): An entity must participate in the relationship (e.g., every EMPLOYEE must work for a DEPARTMENT). This is shown with a double line in ER diagrams.
  * Partial (Optional): An entity may or may not participate (e.g., not every EMPLOYEE manages a department). This is shown with a single line.

Once the conceptual ER model is finalized, it serves as the direct input for creating the logical-level relational model, which is the structure implemented in the database.

2.3 Fundamentals of the Relational Data Model

The relational model, first proposed by Dr. E.F. Codd in 1970, provides the logical structure for most modern database systems. All the practical work in this course, from writing SQL queries to building the final project application, is based on the principles of this model. It organizes data into two-dimensional tables, formally known as relations.

To understand the relational model, it's helpful to map its formal terminology to the more common, informal terms used in practice:

Informal Term	Formal Relational Model Term
Table	Relation
Column Header	Attribute
Row	Tuple
Data Type	Domain

The integrity and consistency of data within the relational model are maintained through a series of constraints:

* Superkey: A set of one or more attributes that, taken collectively, can uniquely identify a tuple within a relation.
* Key (Candidate Key): A minimal superkey. This means it is a superkey from which no attribute can be removed without it losing its unique identification property. A relation can have multiple candidate keys.
* Primary Key: The candidate key that is chosen by the database designer to be the principal means of uniquely identifying tuples within a relation.

Two fundamental integrity constraints are at the core of the relational model:

* Entity Integrity: This rule states that no primary key value can be NULL. This is because the primary key is used to identify individual tuples; a NULL value would mean there is a tuple that cannot be identified.
* Referential Integrity: This constraint is maintained using a foreign key. A foreign key is an attribute in one relation that refers to the primary key of another relation. The rule states that the value of a foreign key must either be NULL or match an existing primary key value in the referenced relation. For example, in the COMPANY schema, the Dno attribute in the EMPLOYEE table is a foreign key that references the Dnumber primary key in the DEPARTMENT table, ensuring every employee is assigned to a valid department.

SQL is the standard language used to define the schema, manipulate the data, and execute queries on databases that are built upon this powerful and enduring relational model.

3.0 Core Technical Skills: Mastering SQL

3.1 Basic SQL: Data Definition and Manipulation

Proficiency in basic SQL is the first practical step in bringing a database design to life. This involves using Data Definition Language (DDL) to create the database structure and Data Manipulation Language (DML) to perform fundamental operations like adding, modifying, and removing data.

The course materials introduce the essential DDL and DML commands needed to build and manage a database:

* CREATE TABLE: This is the main DDL command used to define a new table. It specifies the table's name, its attributes, and the data type for each attribute.
* Constraints: Within the CREATE TABLE statement, constraints are defined to enforce data integrity. The most critical ones are:
  * PRIMARY KEY: Designates an attribute as the unique identifier for each tuple.
  * UNIQUE: Ensures that all values in a column are distinct.
  * FOREIGN KEY: Creates a link between tables and enforces referential integrity.
* INSERT: The DML command used to add new tuples (rows) into an existing table.
* DELETE: This command removes one or more tuples from a table, typically used with a WHERE clause to specify which rows to remove.
* UPDATE: Used to modify the attribute values of existing tuples in a table, also commonly paired with a WHERE clause to target specific rows.

The foundation of data retrieval in SQL is the basic query structure, which consists of SELECT, FROM, and WHERE clauses. Results can then be sorted using the ORDER BY clause. These commands form the building blocks for all database interactions, paving the way for more complex data retrieval.

3.2 Intermediate SQL: Joining Tables and Aggregating Data

The true power of a relational database is its ability to connect related data from different tables and to summarize that data into meaningful information. This section covers the essential intermediate SQL skills required to perform these more complex and valuable operations.

* JOIN Operations: The purpose of a JOIN is to combine rows from two or more tables based on a related column between them. The lab sessions provide visualizations and practical examples of the primary join types:
  * INNER JOIN: Retrieves records that have matching values in both tables.
  * LEFT JOIN: Retrieves all records from the left table and the matched records from the right table. If there is no match, the result is NULL on the right side.
  * FULL JOIN: While not directly supported in SQLite, it can be emulated. It returns all records when there is a match in either the left or the right table.
* Subqueries: A subquery, or nested query, is a SELECT statement embedded inside another query. Its primary purpose is to return a result set that will be used by the main query as a condition for filtering, comparison, or data retrieval.
* Aggregate Functions: These functions perform a calculation on a set of values and return a single, summary value. The key function covered is COUNT(), which returns the number of rows. Aggregate functions are almost always used with the GROUP BY clause.
  * GROUP BY: This clause groups rows that have the same values in specified columns into summary rows, such as counting the number of employees in each department.
  * HAVING: This clause is used to filter the results produced by the GROUP BY clause. While WHERE filters rows before they are grouped, HAVING filters groups after they have been created.

Mastering these intermediate skills allows you to move beyond simple data storage and enables sophisticated data analysis, which is crucial for building advanced programmatic capabilities into the database.

3.3 Advanced SQL: Procedural Logic and Security

Advanced SQL extends the language from a data query tool into a robust programming environment. It allows for creating reusable code, automating database actions, and, most importantly, ensuring secure interaction with external applications.

The Week 10 lecture introduces several advanced topics critical for building a complete database application:

* Accessing SQL from Programming Languages: Applications use Application Programming Interfaces (APIs) like JDBC (for Java) and ODBC to establish connections, send SQL commands, and process results.
* Functions and Procedures: These are blocks of pre-compiled SQL code that can be stored in the database and executed on demand, allowing for the encapsulation and reuse of complex business logic.
* Triggers: A trigger is a special type of stored procedure that automatically executes when a specific event occurs, such as an INSERT, UPDATE, or DELETE on a particular table. They are useful for automating business rules.
* The CASE Statement: As demonstrated in the Week 11 lab, the CASE statement provides a way to implement IF-THEN-ELSE conditional logic directly within an SQL query. For your final project, the CASE statement is invaluable for creating derived categories, such as assigning 'High Priority' or 'Low Priority' labels to orders based on their value, or categorizing products into performance tiers ('Top Seller', 'Average', 'Discontinued') within a single query.

Critical Security Consideration: SQL Injection

A major focus of the advanced SQL lecture is security. SQL Injection is a dangerous vulnerability that occurs when an application insecurely constructs SQL queries by concatenating them with user-supplied input.

For example, an attacker could input X' or 'Y' = 'Y into a username field, which could bypass authentication by tricking the database into returning all rows. An even more malicious attack could use input like X'; update instructor set salary = salary + 10000; -- to execute unauthorized commands that modify or destroy data.

The professor's warning is unequivocal: NEVER create a query by concatenating user input strings. To prevent this vulnerability, you must ALWAYS use prepared statements and placeholders, which treat user input as data and not as executable code. These advanced skills are the final piece of the puzzle, enabling the creation of a secure and powerful database backend in the practical environment where these skills will be applied.

4.0 Practical Implementation: The Course Toolkit

4.1 Your Development Environment: Google Colab and Python

Mastering the course's designated development environment is essential for translating theoretical knowledge into practical results. For this course, all lab work and project development will be conducted using Google Colab, a cloud-based notebook environment that provides a powerful and accessible platform for Python programming and data analysis.

Based on the Week 2 lab materials, the key steps for setting up and working within Google Colab are:

* Creating a new notebook.
* Connecting to a hosted runtime to execute code, with the option to enable a GPU or TPU if needed.
* Uploading necessary files (such as datasets) to the Colab environment.
* Installing any required Python packages directly within the notebook using the !pip install command.
* Importing datasets, for instance, by using the Kaggle API with a personal API token.

The primary Python libraries leveraged throughout the course are sqlite3 for database interaction and pandas for data analysis. The pandas library is particularly useful for fetching the results of your SQL queries into a clean, tabular DataFrame, allowing you to easily analyze, print, and potentially visualize your data within the Colab notebook—a key technique demonstrated in the intermediate SQL labs. This toolkit provides everything needed for the core task of database interaction.

4.2 Implementing CRUD Operations with Python and SQLite

Implementing CRUD (Create, Read, Update, Delete) operations is the fundamental skill required to build any database-driven application. The course provides a clear, object-oriented approach for performing these operations by connecting Python code to an SQLite database. This method ensures that the application logic is clean, maintainable, and secure.

The process, as detailed in the "SQLite and Python CRUD Operations" lab note, involves defining Python functions that execute specific SQL commands. To facilitate an object-oriented approach, the Employee class is used to represent and manage data as Python objects before they are passed to or retrieved from the database.

The mapping between the four core CRUD operations and their corresponding Python functions and SQL commands is summarized below:

Operation	Python Function Example	SQL Command
Create	insert_emp(emp)	INSERT INTO ...
Read	get_emps_by_name(lastname)	SELECT * FROM ...
Update	update_pay(emp, pay)	UPDATE ... SET ...
Delete	remove_emp(emp)	DELETE FROM ...

A critical aspect of this implementation is the consistent use of placeholders (e.g., :first, :last) within the SQL queries executed by the Python functions. This practice is a crucial security measure that prevents SQL injection attacks by ensuring that user-supplied data is treated as literal values rather than executable code. With this foundation, you can integrate all this knowledge into a coherent project plan.

5.0 Planning and Executing Your Final Project

5.1 Step 1: Conceptualization and Database Design

This is the most crucial phase of the project. A well-designed database is easy to build, maintain, and query, while a poorly designed one will lead to complications at every subsequent step. This stage embodies the professor's experiential learning philosophy: "I do and I understand." The effort invested here in creating a solid blueprint will pay dividends throughout the implementation process.

First, define a clear "mini-world" or problem domain for your project. This could be a system for managing student enrollments, a small e-commerce inventory, or a project management tool.

Next, follow this checklist to develop a complete conceptual design:

1. Identify Entities: Determine the primary objects or concepts in your domain (e.g., Student, Course, Product).
2. Define Attributes: List the properties for each entity, specifying types (simple, composite) and identifying key attributes.
3. Establish Relationships: Define how entities interact and determine their cardinality and participation constraints.
4. Create the ERD: Visualize the complete schema by drawing an Entity-Relationship Diagram (ERD). Tools such as Luna Modeler (as shown in the Datensen video) or commercial enterprise tools like ERWin/ER Studio can be used to create a professional ERD.
5. Validate with Normalization: After creating your initial ERD, systematically apply normalization principles as a validation check. This process often reveals opportunities to refine your design, such as splitting a large entity into smaller, more coherent ones to eliminate redundancy.
6. Normalize the Schema: Analyze your design to ensure it meets at least the Third Normal Form (3NF). This is not an academic exercise; failure to normalize properly will lead to data redundancy and introduce insertion, update, and deletion anomalies that can break your application's logic during the demo.

The completed and normalized ERD is the primary deliverable for the project proposal and serves as the definitive guide for the implementation phase.

5.2 Step 2: Implementation and Application Development

This phase involves translating the design blueprint from Step 1 into a functional database and a working Python application. It is where the conceptual model becomes a tangible, interactive system.

Follow these implementation steps to build your project:

1. Translate ERD to Relational Schema: Convert each entity from the ERD into a SQL CREATE TABLE statement. Define all attributes with appropriate data types and implement relationships by defining PRIMARY KEY and FOREIGN KEY constraints correctly.
2. Set Up the Environment: Initialize a Google Colab notebook and write the Python code to create and connect to an SQLite database file using sqlite3.connect().
3. Populate the Database: Use SQL INSERT statements to populate the tables with a sufficient amount of sample data. This is essential for testing your application's functionality.
4. Develop the Python Application: Create Python functions or classes to handle all interactions with the database. Implement the core CRUD (Create, Read, Update, Delete) operations for each entity, following the object-oriented approach demonstrated in the course labs.
5. Build Complex Queries: Go beyond basic CRUD. Implement sophisticated queries that provide meaningful analysis or advanced features, demonstrating your mastery of JOINs, aggregate functions, subqueries, and CASE statements.
6. Ensure Security: As a final and critical check, review all Python functions that execute SQL queries. Verify that every query incorporating external or user-provided data uses placeholders to prevent SQL injection vulnerabilities.

This systematic process ensures that all components of the system are built correctly, leading to the final step of demonstrating your work.

5.3 Step 3: Demonstration and Final Submission

The project demo is the culmination of the semester's work and the primary opportunity to showcase the functionality of the application and the robustness of the underlying database design. A successful demonstration clearly communicates not only what your project does but also why it was designed and built in a particular way, connecting it back to the core principles of the course.

To prepare for a successful final presentation and submission, use the following success checklist:

* [ ] Clear Presentation of Design: Be prepared to present and justify your ERD and relational schema choices, especially concerning entities, relationships, cardinality, and normalization.
* [ ] Functional Application: Clearly demonstrate that all core CRUD operations work as expected for each entity.
* [ ] Advanced Functionality: Showcase the implementation of complex queries that go beyond simple data retrieval, such as generating summary reports or joining data from multiple tables to provide valuable insights.
* [ ] Adherence to Best Practices: During the demo, explicitly mention how your project adheres to database best practices, highlighting that the schema is normalized (to 3NF) and the application is secure against SQL injection.
* [ ] Code Clarity and Structure: Ensure the Python code you submit is well-organized, commented, and easy to read, reflecting a professional standard.
* [ ] Alignment with Course Goals: Explicitly connect your project's features and design back to the course's main objectives: demonstrating an understanding of database structure and the proficient application of SQL.

Remember that this project is a key component for building a professional portfolio—a point the professor has highlighted. A well-executed project is a powerful testament to your skills. Use this guide to structure your work, and you will be well on your way to building a successful and impressive final project.
