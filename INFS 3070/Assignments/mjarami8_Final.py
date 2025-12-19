"""Final assignment for INFS 3070 by mjarami8
1. When launched your application should connect to the class database.
2. When launched your code should check to see if the appropriate database tables exist.
    If they do, the app should proceed. If they do not, your application should create the tables.
3. Your application must have a user interface with the appropriate elements.
4. When you enter information in the input fields and select "Save Sale" the field should
    clear the values and insert the records into the appropriate database tables and fields.
5. When you select "Show Sales Graph" a bar graph should appear in the application window that
    displays the total sales (revenue) for each product that has been entered.
"""

import tkinter as tk
from tkinter import messagebox
from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine("mysql+pymysql://finalUser:itsover!@128.198.162.191/finaldb")

def init_db():
    with engine.connect() as conn:

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS mjarami8_products (
            productID INT AUTO_INCREMENT PRIMARY KEY,
            productName VARCHAR(45),
            productPrice DECIMAL(8,2)
        )
        """))

        conn.execute(text("""
        CREATE TABLE IF NOT EXISTS mjarami8_sales (
            PK INT AUTO_INCREMENT PRIMARY KEY,
            productID INT,
            unitSales INT,
            salesDate DATE
        )
        """))

def gui():
    # Create method variables
    global product_name, product_price, units_sold, sales_date

    # Create main window
    main_window = tk.Tk()
    main_window.title('Sales Entry')
    main_window.geometry("800x600")
    main_window.configure(bg='lightblue')

    label_font = ("Arial", 14)
    entry_font = ("Arial", 12)
    button_font = ("Arial", 12)
    
    # Create input fields
    tk.Label(main_window, text = 'Product Name', bg='lightblue', font=label_font).pack(pady=1)
    product_name = tk.Entry(main_window, font=entry_font)
    product_name.pack(pady=5)
    
    tk.Label(main_window, text = 'Product Price', bg='lightblue', font=label_font).pack(pady=1)    
    product_price = tk.Entry(main_window, font=entry_font)
    product_price.pack(pady=5)

    tk.Label(main_window, text = 'Units Sold', bg='lightblue', font=label_font).pack(pady=1)
    units_sold = tk.Entry(main_window, font=entry_font)
    units_sold.pack(pady=5)

    tk.Label(main_window, text = 'Sales Date (YYYY-MM-DD)', bg='lightblue', font=label_font).pack(pady=1)
    sales_date = tk.Entry(main_window, font=entry_font)
    sales_date.pack(pady=5)

    # Create buttons
    tk.Button(main_window, text = 'Save Sale', font=button_font, command=save_sale).pack(pady=5)
    tk.Button(main_window, text = 'Show Sales Graph', font=button_font, command=show_sales_graph).pack(pady=5)
    
    # Start the main event loop
    tk.mainloop()

def save_sale():
    # Create variables
    product_name_value = product_name.get()
    product_price_value = product_price.get()
    units_sold_value = units_sold.get()
    sales_date_value = sales_date.get()

    # Checks for all fields
    if not all([product_name_value, product_price_value, units_sold_value, sales_date_value]):
        messagebox.showerror("Error", "All fields are required")
        return
    
    # Insert the sale into the database
    with engine.begin() as conn:
        result = conn.execute(text("""
            SELECT productID FROM mjarami8_products
            WHERE productName = :name
        """), {"name": product_name_value}).fetchone()

        if result is None:
            conn.execute(text("""
                INSERT INTO mjarami8_products (productName, productPrice)
                VALUES (:name, :price)
            """), {"name": product_name_value, "price": product_price_value})
            product_id = conn.execute(text("""
                SELECT productID FROM mjarami8_products
                WHERE productName = :name
            """), {"name": product_name_value}).fetchone()[0]
        else:
            product_id = result[0]

        conn.execute(text("""
            INSERT INTO mjarami8_sales (productID, unitSales, salesDate)
            VALUES (:productID, :unitSales, :salesDate)
        """), {"productID": product_id, "unitSales": units_sold_value, "salesDate": sales_date_value})

        messagebox.showinfo("Success", "Sale saved successfully")
        # Clear the fields
        product_name.delete(0, tk.END)
        product_price.delete(0, tk.END)
        units_sold.delete(0, tk.END)
        sales_date.delete(0, tk.END)

def show_sales_graph():
    query = """
    SELECT p.productName,
           SUM(p.productPrice * s.unitSales) AS revenue
    FROM mjarami8_products p
    JOIN mjarami8_sales s ON p.productID = s.productID
    GROUP BY p.productName
    """

    df = pd.read_sql_query(query, engine)

    df.plot(kind='bar', x='productName', y='revenue', legend=False, rot=45, figsize=(12,8), title="Total Sales by Product")
    plt.gca().set_facecolor('lightblue')
    plt.gcf().canvas.manager.set_window_title("Sales Revenue by Product")
    plt.ylabel("Total Revenue")
    plt.xlabel("Product Name")
    plt.show()

if __name__=="__main__":
   
    init_db()
    gui()