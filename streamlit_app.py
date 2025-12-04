import streamlit as st
import plotly.express as px
import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os
import datetime

# --- Configuration ---
st.set_page_config(page_title="Executive E-Commerce Dashboard", page_icon="📊", layout="wide")
DB_NAME = 'ecommerce_analytics.db'

# --- Database Manager Class (Professional OOP Design) ---
class DatabaseManager:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_connection(self):
        """Establishes a connection to the SQLite database."""
        if os.path.exists(self.db_path):
            return sqlite3.connect(self.db_path)
        # Check alternative paths
        elif os.path.exists(f"data/{self.db_path}"):
            return sqlite3.connect(f"data/{self.db_path}")
        elif os.path.exists(f"notebooks/{self.db_path}"):
            return sqlite3.connect(f"notebooks/{self.db_path}")
        return None

    def init_triggers(self):
        """Creates SQL triggers for automated business logic (Advanced SQL)."""
        conn = self.get_connection()
        if not conn: return
        try:
            cursor = conn.cursor()
            # Trigger: Auto-decrement stock when an item is ordered
            cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS update_stock_after_order
            AFTER INSERT ON OrderItems
            BEGIN
                UPDATE Products
                SET StockLevel = StockLevel - NEW.Quantity
                WHERE ProductID = NEW.ProductID;
            END;
            """)
            conn.commit()
        except Exception as e:
            st.error(f"Failed to initialize triggers: {e}")
        finally:
            conn.close()

    def get_kpis(self, region, category):
        conn = self.get_connection()
        if not conn: return None
        
        query = """
        SELECT 
            COUNT(DISTINCT o.OrderID) as TotalOrders,
            SUM(oi.Quantity * oi.UnitPrice) as TotalRevenue,
            AVG(oi.Quantity * oi.UnitPrice) as AvgOrderValue
        FROM Orders o
        JOIN OrderItems oi ON o.OrderID = oi.OrderID
        JOIN Products p ON oi.ProductID = p.ProductID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE 1=1
        """
        params = []
        if region != 'All':
            query += " AND c.Region = ?"
            params.append(region)
        if category != 'All':
            query += " AND p.Category = ?"
            params.append(category)
            
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        return df.iloc[0]

    def get_trend_data(self, region, category):
        conn = self.get_connection()
        if not conn: return pd.DataFrame()
        
        query = """
        SELECT o.OrderDate, SUM(oi.Quantity * oi.UnitPrice) as Revenue
        FROM Orders o
        JOIN OrderItems oi ON o.OrderID = oi.OrderID
        JOIN Products p ON oi.ProductID = p.ProductID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE 1=1
        """
        params = []
        if region != 'All':
            query += " AND c.Region = ?"
            params.append(region)
        if category != 'All':
            query += " AND p.Category = ?"
            params.append(category)
        
        query += " GROUP BY o.OrderDate ORDER BY o.OrderDate"
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        return df

    def get_top_products(self, region, category):
        conn = self.get_connection()
        if not conn: return pd.DataFrame()
        
        query = """
        SELECT p.ProductName, SUM(oi.Quantity) as UnitsSold, SUM(oi.Quantity * oi.UnitPrice) as Revenue
        FROM OrderItems oi
        JOIN Products p ON oi.ProductID = p.ProductID
        JOIN Orders o ON oi.OrderID = o.OrderID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE 1=1
        """
        params = []
        if region != 'All':
            query += " AND c.Region = ?"
            params.append(region)
        if category != 'All':
            query += " AND p.Category = ?"
            params.append(category)
            
        query += " GROUP BY p.ProductName ORDER BY Revenue DESC LIMIT 10"
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        return df

    def get_category_share(self, region):
        conn = self.get_connection()
        if not conn: return pd.DataFrame()
        
        query = """
        SELECT p.Category, SUM(oi.Quantity * oi.UnitPrice) as Revenue
        FROM OrderItems oi
        JOIN Products p ON oi.ProductID = p.ProductID
        JOIN Orders o ON oi.OrderID = o.OrderID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE 1=1
        """
        params = []
        if region != 'All':
            query += " AND c.Region = ?"
            params.append(region)
            
        query += " GROUP BY p.Category"
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        return df

    def get_day_of_week_stats(self, region, category):
        conn = self.get_connection()
        if not conn: return pd.DataFrame()
        
        # Using CASE statement for advanced SQL logic
        query = """
        SELECT 
            strftime('%w', o.OrderDate) as DayIndex,
            CASE strftime('%w', o.OrderDate)
                WHEN '0' THEN 'Sunday'
                WHEN '1' THEN 'Monday'
                WHEN '2' THEN 'Tuesday'
                WHEN '3' THEN 'Wednesday'
                WHEN '4' THEN 'Thursday'
                WHEN '5' THEN 'Friday'
                WHEN '6' THEN 'Saturday'
            END as DayName,
            SUM(oi.Quantity * oi.UnitPrice) as Revenue
        FROM Orders o
        JOIN OrderItems oi ON o.OrderID = oi.OrderID
        JOIN Products p ON oi.ProductID = p.ProductID
        JOIN Customers c ON o.CustomerID = c.CustomerID
        WHERE 1=1
        """
        params = []
        if region != 'All':
            query += " AND c.Region = ?"
            params.append(region)
        if category != 'All':
            query += " AND p.Category = ?"
            params.append(category)
            
        query += " GROUP BY DayIndex ORDER BY DayIndex"
        df = pd.read_sql_query(query, conn, params=params)
        conn.close()
        return df

    def get_customers(self):
        conn = self.get_connection()
        if not conn: return []
        df = pd.read_sql_query("SELECT CustomerID, FullName FROM Customers ORDER BY FullName LIMIT 50", conn)
        conn.close()
        return df

    def get_products(self):
        conn = self.get_connection()
        if not conn: return []
        df = pd.read_sql_query("SELECT ProductID, ProductName, Price, StockLevel FROM Products ORDER BY ProductName", conn)
        conn.close()
        return df

    def place_order(self, customer_id, product_id, quantity, price):
        conn = self.get_connection()
        if not conn: return False
        try:
            cursor = conn.cursor()
            # 1. Create Order
            order_date = datetime.date.today().strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO Orders (CustomerID, OrderDate, TotalAmount) VALUES (?, ?, ?)", 
                           (customer_id, order_date, quantity * price))
            order_id = cursor.lastrowid
            
            # 2. Create OrderItem (Trigger will auto-update Stock)
            cursor.execute("INSERT INTO OrderItems (OrderID, ProductID, Quantity, UnitPrice) VALUES (?, ?, ?, ?)",
                           (order_id, product_id, quantity, price))
            
            conn.commit()
            return True
        except Exception as e:
            st.error(f"Error placing order: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

# --- Main Application ---
def main():
    st.title("📊 Executive E-Commerce Dashboard")
    st.markdown("Real-time insights into sales performance, trends, and product analytics.")
    
    # Initialize DB Manager
    db = DatabaseManager(DB_NAME)
    
    # Ensure Triggers are set up
    db.init_triggers()

    conn = db.get_connection()
    if not conn:
        st.error(f"Database '{DB_NAME}' not found. Please run the notebook to generate data.")
        return
    conn.close()

    # --- Tabs for Dashboard vs Operations ---
    tab1, tab2 = st.tabs(["📈 Dashboard Analysis", "🛠️ Operations (CRUD)"])

    with tab1:
        # --- Sidebar Filters ---
        st.sidebar.header("Filter Analysis")
        region_options = ['All', 'North', 'South', 'East', 'West', 'Central']
        category_options = ['All', 'Electronics', 'Clothing', 'Home', 'Books', 'Sports']
        
        region = st.sidebar.selectbox("🌍 Region", region_options)
        category = st.sidebar.selectbox("📦 Category", category_options)
        
        st.sidebar.markdown("---")
        st.sidebar.caption("Data Source: SQLite Database")
        st.sidebar.caption("v2.0.0 Professional Edition")

        # --- Fetch Data ---
        kpis = db.get_kpis(region, category)
        trend_df = db.get_trend_data(region, category)
        top_prod_df = db.get_top_products(region, category)
        cat_share_df = db.get_category_share(region)
        dow_df = db.get_day_of_week_stats(region, category)
        
        # --- KPI Section ---
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric("Total Revenue", f"${kpis['TotalRevenue']:,.0f}" if pd.notnull(kpis['TotalRevenue']) else "$0", delta="YTD")
        with c2:
            st.metric("Total Orders", f"{kpis['TotalOrders']:,}" if pd.notnull(kpis['TotalOrders']) else "0")
        with c3:
            st.metric("Avg Order Value", f"${kpis['AvgOrderValue']:,.0f}" if pd.notnull(kpis['AvgOrderValue']) else "$0.00")
        
        st.markdown("---")

        # --- Charts Row 1 ---
        col1, col2 = st.columns([2, 1])
        with col1:
            st.subheader("📈 Daily Revenue Trend")
            if not trend_df.empty:
                fig_trend = px.line(trend_df, x='OrderDate', y='Revenue', markers=True)
                fig_trend.update_layout(xaxis_title="Date", yaxis_title="Revenue ($)", hovermode="x unified")
                fig_trend.update_traces(line_color='#2E86C1', line_width=3)
                st.plotly_chart(fig_trend, use_container_width=True)
            else:
                st.info("No trend data available.")

        with col2:
            st.subheader("🍩 Revenue by Category")
            if not cat_share_df.empty:
                # FIX: Use px.pie with hole argument instead of px.donut
                fig_pie = px.pie(cat_share_df, values='Revenue', names='Category', hole=0.4)
                fig_pie.update_layout(showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("No category data available.")

        # --- Charts Row 2 ---
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("🏆 Top 10 Products")
            if not top_prod_df.empty:
                fig_bar = px.bar(top_prod_df, x='Revenue', y='ProductName', orientation='h', text_auto='.2s')
                fig_bar.update_layout(yaxis={'categoryorder':'total ascending'}, xaxis_title="Revenue ($)", yaxis_title="")
                fig_bar.update_traces(marker_color='#28B463')
                st.plotly_chart(fig_bar, use_container_width=True)
            else:
                st.info("No product data available.")

        with col4:
            st.subheader("📅 Sales by Day of Week")
            if not dow_df.empty:
                order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
                fig_dow = px.bar(dow_df, x='DayName', y='Revenue', color='Revenue', text_auto='.2s')
                fig_dow.update_layout(xaxis={'categoryorder':'array', 'categoryarray': order}, xaxis_title="", yaxis_title="Revenue ($)")
                st.plotly_chart(fig_dow, use_container_width=True)
            else:
                st.info("No daily data available.")

    with tab2:
        st.header("🛠️ Operations Management")
        st.markdown("Execute transactional operations (CRUD) with automated inventory updates via SQL Triggers.")
        
        st.subheader("📝 Place New Order")
        
        # Fetch dropdown data
        customers = db.get_customers()
        products = db.get_products()
        
        if not customers.empty and not products.empty:
            with st.form("order_form"):
                col_a, col_b = st.columns(2)
                with col_a:
                    cust_id = st.selectbox("Select Customer", customers['CustomerID'], format_func=lambda x: customers[customers['CustomerID'] == x]['FullName'].values[0])
                with col_b:
                    prod_id = st.selectbox("Select Product", products['ProductID'], format_func=lambda x: f"{products[products['ProductID'] == x]['ProductName'].values[0]} (${products[products['ProductID'] == x]['Price'].values[0]:.2f})")
                
                quantity = st.number_input("Quantity", min_value=1, max_value=100, value=1)
                
                submitted = st.form_submit_button("✅ Submit Order")
                
                if submitted:
                    # Get price
                    price = products[products['ProductID'] == prod_id]['Price'].values[0]
                    success = db.place_order(cust_id, prod_id, quantity, price)
                    if success:
                        st.success(f"Order placed successfully! Inventory for Product ID {prod_id} has been auto-updated via SQL Trigger.")
                        st.rerun()
                    else:
                        st.error("Failed to place order.")
            
            st.divider()
            st.subheader("📦 Current Inventory Levels")
            # Show updated stock to verify trigger
            st.dataframe(db.get_products()[['ProductName', 'StockLevel', 'Price']], use_container_width=True)
            
        else:
            st.warning("No customers or products found. Please generate data first.")

if __name__ == "__main__":
    main()
