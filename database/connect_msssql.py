import pyodbc

DRIVER_NAME = 'SQL SERVER'
SERVER = 'Avijit-PC\\SQLEXPRESS'
DATABASE = 'TSQLV6'
connectionString = f"""
DRIVER={{{DRIVER_NAME}}};
SERVER={SERVER};
DATABASE={DATABASE};
Trusted_Connection=yes;
"""

conn = pyodbc.connect(connectionString)

SQL_QUERY = """
SELECT TOP (10) [SalesOrderID]
      ,[RevisionNumber]
      ,[OrderDate]
      ,[DueDate]
      ,[ShipDate]
      ,[Status]
      ,[OnlineOrderFlag]
      ,[SalesOrderNumber]
      ,[PurchaseOrderNumber]
      ,[AccountNumber]
      ,[BillToAddressID]
      ,[ShipToAddressID]
      ,[ShipMethodID]
      ,[CreditCardID]
      ,[CreditCardApprovalCode]
      ,[CurrencyRateID]
      ,[SubTotal]
      ,[TaxAmt]
  FROM [AdventureWorks2022].[Sales].[SalesOrderHeader]

"""

sales_query = """
SELECT TOP (10) [custid]
      ,[companyname]
      ,[contactname]
      ,[contacttitle]
      ,[address]
      ,[city]
      ,[region]
      ,[postalcode]
      ,[country]
      ,[phone]
      ,[fax]
  FROM [TSQLV6].[Sales].[Customers]

"""

cursor = conn.cursor()
cursor.execute(sales_query)

record = cursor.fetchall()
# for r in record:
#     print(f"Order Date: {r.OrderDate}\t ShipDate: {r.ShipDate}\t Total: {r.SubTotal}\t Tax Amount{r.TaxAmt}\t")

for r in record:
    print(f"Name: {r.contactname}\t City: {r.city}\t\t Region: {r.region}\t")