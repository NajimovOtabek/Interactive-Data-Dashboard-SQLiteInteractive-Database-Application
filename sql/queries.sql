-- 1. Revenue by Product Category
SELECT 
    p.Category,
    COUNT(oi.OrderItemID) as ItemsSold,
    SUM(oi.Quantity * oi.UnitPrice) as TotalRevenue,
    AVG(oi.UnitPrice) as AvgPrice
FROM OrderItems oi
JOIN Products p ON oi.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY TotalRevenue DESC;

-- 2. Top Customers by Region (Window Function: Rank)
WITH CustomerSpending AS (
    SELECT 
        c.CustomerID,
        c.FullName,
        c.Region,
        SUM(o.TotalAmount) as TotalSpent
    FROM Customers c
    JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY c.CustomerID
),
RankedCustomers AS (
    SELECT 
        Region,
        FullName,
        TotalSpent,
        RANK() OVER (PARTITION BY Region ORDER BY TotalSpent DESC) as RankInRegion
    FROM CustomerSpending
)
SELECT *
FROM RankedCustomers
WHERE RankInRegion <= 3;

-- 3. Daily Revenue Trends (Window Function: Running Total & Moving Average)
WITH DailySales AS (
    SELECT 
        OrderDate,
        SUM(TotalAmount) as DailyTotal
    FROM Orders
    GROUP BY OrderDate
)
SELECT 
    OrderDate,
    DailyTotal,
    SUM(DailyTotal) OVER (ORDER BY OrderDate ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as MovingAvg7Day,
    SUM(DailyTotal) OVER (ORDER BY OrderDate) as CumulativeRevenue
FROM DailySales
ORDER BY OrderDate;

-- 4. Dashboard: Key Performance Indicators (Dynamic Filters)
SELECT 
    COUNT(DISTINCT o.OrderID) as TotalOrders,
    SUM(oi.Quantity * oi.UnitPrice) as TotalRevenue,
    AVG(oi.Quantity * oi.UnitPrice) as AvgOrderValue
FROM Orders o
JOIN OrderItems oi ON o.OrderID = oi.OrderID
JOIN Products p ON oi.ProductID = p.ProductID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Region = ? AND p.Category = ?; -- Placeholders for filters

-- 5. Dashboard: Filtered Daily Trend
SELECT o.OrderDate, SUM(oi.Quantity * oi.UnitPrice) as Revenue
FROM Orders o
JOIN OrderItems oi ON o.OrderID = oi.OrderID
JOIN Products p ON oi.ProductID = p.ProductID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Region = ? AND p.Category = ?
GROUP BY o.OrderDate 
ORDER BY o.OrderDate;

-- 6. Dashboard: Top 10 Products (Filtered)
SELECT p.ProductName, SUM(oi.Quantity) as UnitsSold, SUM(oi.Quantity * oi.UnitPrice) as Revenue
FROM OrderItems oi
JOIN Products p ON oi.ProductID = p.ProductID
JOIN Orders o ON oi.OrderID = o.OrderID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Region = ? AND p.Category = ?
GROUP BY p.ProductName 
ORDER BY Revenue DESC 
LIMIT 10;

-- 7. Dashboard: Sales by Day of Week
SELECT 
    strftime('%w', o.OrderDate) as DayIndex,
    SUM(oi.Quantity * oi.UnitPrice) as Revenue
FROM Orders o
JOIN OrderItems oi ON o.OrderID = oi.OrderID
JOIN Products p ON oi.ProductID = p.ProductID
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.Region = ? AND p.Category = ?
GROUP BY DayIndex 
ORDER BY DayIndex;
