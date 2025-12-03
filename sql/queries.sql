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
