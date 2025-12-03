-- Database Schema for E-Commerce Inventory & Sales Intelligence

DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS OrderItems;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FullName TEXT NOT NULL,
    Email TEXT UNIQUE,
    Region TEXT CHECK(Region IN ('North', 'South', 'East', 'West', 'Central')),
    JoinDate DATE
);

CREATE TABLE Products (
    ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductName TEXT NOT NULL,
    Category TEXT,
    Price REAL,
    StockLevel INTEGER
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    OrderDate DATE,
    TotalAmount REAL DEFAULT 0,
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
);

CREATE TABLE OrderItems (
    OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderID INTEGER,
    ProductID INTEGER,
    Quantity INTEGER,
    UnitPrice REAL,
    FOREIGN KEY(OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID)
);

CREATE TABLE Reviews (
    ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    ProductID INTEGER,
    CustomerID INTEGER,
    Rating INTEGER CHECK(Rating BETWEEN 1 AND 5),
    Comment TEXT,
    ReviewDate DATE,
    FOREIGN KEY(ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID)
);
