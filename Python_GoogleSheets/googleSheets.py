from tkinter import *
from tkinter import ttk

import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1ucytfywlXuiylze2RhOsGaLHigGO5nIf4vkIggq1nrU"
SAMPLE_RANGE_NAME = "Dados!A1:E"

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
CREDENTIALS_FILE = 'token.json'

def main():
  creds = None
  if os.path.exists(CREDENTIALS_FILE):
    # Get the last modification time of the token file
    token_mod_time = os.path.getmtime(CREDENTIALS_FILE)
    current_time = time.time()
        
    max_age = 7200  # 2 hours
    # Check if the token is valid (older than "max_age")
    if current_time - token_mod_time > max_age:
        print("Token is older than 1 hour, refreshing...")
        os.remove(CREDENTIALS_FILE)
        creds = None
    else:
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)
        if creds and creds.expired:
            os.remove(CREDENTIALS_FILE)
            creds = None

  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              "./oAuth/credentials.json", SCOPES
          )
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open(CREDENTIALS_FILE, "w") as token:
          token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    # Read data from Google Sheets
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    # Create the Tkinter window
    root = Tk()
    root.configure(bg="white")
    root.title("Google Sheets System")

    #-------------------------------------- State ------------------------------------------------
    state_label = Label(root, text="State:", font = ("Arial", 12, "bold"), bg="white")
    state_label.grid(row=0, column=0, padx=2, pady=2, sticky="W")

    # Collect information from column A (States) starting from the 2nd row
    states = sorted(list(set(value[0] for value in values[1:])))  # Sort the list of states
    state_combobox = ttk.Combobox(root, values=states, font = ("Arial", 12, "bold"))
    state_combobox.grid(row=1, column=0, padx=2, pady=2, sticky="W")

    #-------------------------------------- City ------------------------------------------------
    city_label = Label(root, text="City:", font = ("Arial", 12, "bold"), bg="white")
    city_label.grid(row=0, column=1, padx=2, pady=2, sticky="W")

    # Collect information from column B (Cities) starting from the 2nd row
    cities = sorted(list(set(value[1] for value in values[1:])))  # Sort the list of cities
    city_combobox = ttk.Combobox(root, values=cities, font = ("Arial", 12, "bold"))
    city_combobox.grid(row=1, column=1, padx=2, pady=2, sticky="W")

    #-------------------------------------- Seller ------------------------------------------------
    seller_label = Label(root, text="Seller:", font = ("Arial", 12, "bold"), bg="white")
    seller_label.grid(row=0, column=2, padx=2, pady=2, sticky="W")

    # Collect information from column C (Sellers) starting from the 2nd row
    sellers = sorted(list(set(value[2] for value in values[1:])))  # Sort the list of sellers
    sellers_combobox = ttk.Combobox(root, values=sellers, font = ("Arial", 12, "bold"))
    sellers_combobox.grid(row=1, column=2, padx=2, pady=2, sticky="W")

    #-------------------------------------- Product ------------------------------------------------
    product_label = Label(root, text="Product:", font = ("Arial", 12, "bold"), bg="white")
    product_label.grid(row=0, column=3, padx=2, pady=2, sticky="W")

    # Collect information from column D (Products) starting from the 2nd row    
    products = sorted(list(set(value[3] for value in values[1:])))  # Sort the list of products
    products_combobox = ttk.Combobox(root, values=products, font = ("Arial", 12, "bold"))
    products_combobox.grid(row=1, column=3, padx=2, pady=2, sticky="W")

    # Create the Treeview to display the spreadsheet data
    tree = ttk.Treeview(root)
    
    # Define the Treeview columns based on the values from Row 1
    columns = values[0]
    tree["columns"] = columns
    for column in columns:
      tree.heading(column, text=column)

    # Fill the Treeview with the spreadsheet data
    for row in values[1:]:
      tree.insert("", "end", values=row)

    # Configure the Treeview
    tree.grid(row=3, column=0, columnspan=6, padx=2, pady=2,sticky="nsew")  #North, South, East, West
    
    style = ttk.Style()
    style.theme_use("clam") # Change the appearance of the Treeview
    style.configure("Treeview", background="#FFFFE0", foreground="black", 
                    font=("Arial", 12), rowheight=25, fieldbackground="#FFFFE0", bordercolor="#808080", borderwidth=1)
    style.map("Treeview", background=[("selected", "#347083")], foreground=[("selected", "white")])  #blue

    # Configure the scrollbar
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=3, column=6, sticky="ns")

    tree.column("#0", width=0, stretch=NO)

    # Function to filter the Treeview data
    def filter():
      # Read information from the spreadsheet
      sheet = service.spreadsheets()
      result = (
          sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
      )
      # Read data from Google Sheets
      values = result['values']

      # Filter options with texts from the comboboxes
      state = state_combobox.get()
      city = city_combobox.get()
      seller = sellers_combobox.get()
      product = products_combobox.get()

      filtered_data = [values[0]]
      for row in values[1:]:
        if (not state or row[0] == state) and \
           (not city or row[1] == city) and \
           (not seller or row[2] == seller) and \
           (not product or row[3] == product):
          filtered_data.append(row)

      # Clear the Treeview
      for row in tree.get_children():
        tree.delete(row)

      # Add the filtered data to the Treeview
      for row in filtered_data[1:]:
        tree.insert("", "end", values=row)
      
      sum_prices()

    # Button to filter the Treeview data
    filter_button = Button(root, text="Filter",  font=("Arial", 16), command=filter)
    filter_button.grid(row=4, column=1, padx=2, pady=2, sticky="NSEW")

    #--------------------------------------
    def update_cities(event):
      # Get the selected state
      state = state_combobox.get()

      # Filter the cities based on the selected state
      cities = sorted(list(set([value[1] for value in values[1:] if value[0] == state])))

      # Update the cities in the combobox
      city_combobox['values'] = cities

      filter()
    state_combobox.bind("<<ComboboxSelected>>", update_cities)

    #--------------------------------------
    def update_sellers(event):
      # Get the selected city
      city = city_combobox.get()

      # Filter the sellers based on the selected city
      sellers = sorted(list(set([value[2] for value in values[1:] if value[1] == city])))

      # Update the sellers in the combobox
      sellers_combobox['values'] = sellers

      filter()
    city_combobox.bind("<<ComboboxSelected>>", update_sellers)

    #--------------------------------------
    def update_products(event):
      # Get the selected seller
      seller = sellers_combobox.get()

      # Filter the products based on the selected seller
      products = sorted(list(set([value[3] for value in values[1:] if value[2] == seller])))

      # Update the products in the combobox
      products_combobox['values'] = products

      filter()
    sellers_combobox.bind("<<ComboboxSelected>>", update_products)

    #--------------------------------------
    def call_filter_on_change(event):
      filter()
    products_combobox.bind("<<ComboboxSelected>>", call_filter_on_change)

    def new_record():
      # Create a secondary window to add a new record
      registration_window = Toplevel(root)
      registration_window.title("Register Product")

      # Create the widgets for the registration window
      Label(registration_window, text="State:", font=("Arial", 16)).grid(row=0, column=0, padx=2, pady=2)
      state_entry = Entry(registration_window, font=("Arial", 16))
      state_entry.grid(row=0, column=1, padx=2, pady=2, sticky="W")

      Label(registration_window, text="City:", font=("Arial", 16)).grid(row=1, column=0, padx=2, pady=2)
      city_entry = Entry(registration_window, font=("Arial", 16))
      city_entry.grid(row=1, column=1, padx=2, pady=2, sticky="W")

      Label(registration_window, text="Seller:", font=("Arial", 16)).grid(row=2, column=0, padx=2, pady=2)
      seller_entry = Entry(registration_window, font=("Arial", 16))
      seller_entry.grid(row=2, column=1, padx=2, pady=2, sticky="W")

      Label(registration_window, text="Product:", font=("Arial", 16)).grid(row=3, column=0, padx=2, pady=2)
      product_entry = Entry(registration_window, font=("Arial", 16))
      product_entry.grid(row=3, column=1, padx=2, pady=2, sticky="W")

      Label(registration_window, text="Price:", font=("Arial", 16)).grid(row=4, column=0, padx=2, pady=2)
      price_entry = Entry(registration_window, font=("Arial", 16))
      price_entry.grid(row=4, column=1, padx=2, pady=2, sticky="W")

      def save_data_to_google_sheets():
        # Get the values from the input fields
        state = state_entry.get()
        city = city_entry.get()
        seller = seller_entry.get()
        product = product_entry.get()
        price = price_entry.get()

        creds = None
        if os.path.exists(CREDENTIALS_FILE):  # Check if the credentials file exists
          creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)

        if not creds or not creds.valid:    # Check if the credentials are valid or non-existent
          if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresh the credentials with the refresh token
          else:
            # If there are no credentials or they are invalid, open the Google Sheets authentication flow
            flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0) # Run the authentication flow on the local server
            with open(CREDENTIALS_FILE, 'w') as token:  # Open the credentials file for writing
              token.write(creds.to_json())  # Write the credentials to the file

        service = build('sheets', 'v4', credentials=creds)  # Create a service object to interact with the Google Sheets API

        values = [[state, city, seller, product, price]]  # Create a list with the data to be added to the spreadsheet

        body = { 'values': values }  # Create a dictionary with the data to be added to the spreadsheet

        # Call the API to add the data to the spreadsheet
        result = service.spreadsheets().values().append(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, 
                    valueInputOption="USER_ENTERED", insertDataOption="INSERT_ROWS", body=body).execute() # Add the data to the spreadsheet
        tree.delete(*tree.get_children())  # Clear the Treeview
        result = service.spreadsheets().values().get(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()  # Execute the API call to get the spreadsheet data
        values = result['values']  # Get the values from the spreadsheet
        for row in values[1:]:  # For each row in the spreadsheet
          tree.insert("", "end", values=row)  # Insert the row into the Treeview

        # Close the registration window
        registration_window.destroy()

        filter()  # or only sum_prices()
        
      # Create the button to save the data
      register_button = Button(registration_window, text="Register",  font=("Arial", 14),  command=save_data_to_google_sheets)
      register_button.grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky="NSEW")

    # Button to save the data in the Treeview
    new_button = Button(root, text="New", font=("Arial", 16), command=new_record)
    new_button.grid(row=4, column=0, padx=2, pady=2, sticky="NSEW")

    #--------------------------------------
    def edit_record(event):
      # Get the selected item
      selected_item = tree.selection()[0]

      # Get the values of the selected item
      selected_values = tree.item(selected_item)["values"]

      # Create a secondary window to edit the record
      edit_window = Toplevel(root)
      edit_window.title("Edit Product")

      # Create the widgets for the edit window
      Label(edit_window, text="State:", font=("Arial", 16)).grid(row=0, column=0, padx=2, pady=2)
      state_entry = Entry(edit_window, font=("Arial", 16), textvariable=StringVar(value=selected_values[0]))
      state_entry.grid(row=0, column=1, padx=2, pady=2, sticky="W")

      Label(edit_window, text="City:", font=("Arial", 16)).grid(row=1, column=0, padx=2, pady=2)
      city_entry = Entry(edit_window, font=("Arial", 16), textvariable=StringVar(value=selected_values[1]))
      city_entry.grid(row=1, column=1, padx=2, pady=2, sticky="W")

      Label(edit_window, text="Seller:", font=("Arial", 16)).grid(row=2, column=0, padx=2, pady=2)
      seller_entry = Entry(edit_window, font=("Arial", 16), textvariable=StringVar(value=selected_values[2]))
      seller_entry.grid(row=2, column=1, padx=2, pady=2, sticky="W")

      Label(edit_window, text="Product:", font=("Arial", 16)).grid(row=3, column=0, padx=2, pady=2)
      product_entry = Entry(edit_window, font=("Arial", 16), textvariable=StringVar(value=selected_values[3]))
      product_entry.grid(row=3, column=1, padx=2, pady=2, sticky="W")

      Label(edit_window, text="Price:", font=("Arial", 16)).grid(row=4, column=0, padx=2, pady=2)
      price_entry = Entry(edit_window, font=("Arial", 16), textvariable=StringVar(value=selected_values[4]))
      price_entry.grid(row=4, column=1, padx=2, pady=2, sticky="W")

      def edit_data_in_google_sheets():
        # Get the values from the input fields
        state = state_entry.get()
        city = city_entry.get()
        seller = seller_entry.get()
        product = product_entry.get()
        price = price_entry.get()

        creds = None
        if os.path.exists(CREDENTIALS_FILE):  # Check if the credentials file exists
          creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)

        if not creds or not creds.valid:    # Check if the credentials are valid or non-existent
          if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())  # Refresh the credentials with the refresh token
          else:
            # If there are no credentials or they are invalid, open the Google Sheets authentication flow
            flow = InstalledAppFlow.from_client_secrets_file(
              'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0) # Run the authentication flow on the local server
            with open(CREDENTIALS_FILE, 'w') as token:  # Open the credentials file for writing
              token.write(creds.to_json())  # Write the credentials to the file

        service = build('sheets', 'v4', credentials=creds)  # Create a service object to interact with the Google Sheets API

        # Define that the data will be added to the spreadsheet as is (without formatting)
        value_input_option = "RAW"

        values = [
            [
                state, 
                city, 
                seller, 
                product, 
                price
              ]
            ]

        # Convert the selected item to a string
        row = str(tree.index(selected_item) + 2)

        # Use string formatting to create the range we will edit
        range_ = f'Dados!A{row}:E{row}'  # Define the spreadsheet range

        body = {
          'values': values
        }

        # Call the API to edit the data in the spreadsheet
        result = sheet.values().update(
                    spreadsheetId=SAMPLE_SPREADSHEET_ID, range=range_,
                    valueInputOption=value_input_option, body=body).execute() # Add the data to the spreadsheet
        
        # Update the data in the Treeview with the new data
        tree.item(selected_item, values=values[0])  
       
        # Close the edit window
        edit_window.destroy()

        # Call the function to update the sum of prices and the number of rows
        #sum_prices()
        filter()
        
      # Create the button to save the data
      edit_button = Button(edit_window, text="Save Changes",  font=("Arial", 14),  command=edit_data_in_google_sheets)
      edit_button.grid(row=6, column=0, padx=2, pady=2, sticky="NSEW")  #columnspan=2, 

    # Double click on the tree-view that calls the edit_record function
    tree.bind("<Double-1>", edit_record)
    #--------------------------------------

    def delete_record():
      selected_item = tree.focus()
      index = tree.index(selected_item)

      # Call the API to delete the data in the spreadsheet
      request = {
        "deleteRange": {
          "range": {
            "sheetId": 0,   # ID of the spreadsheet tab
            "startRowIndex": index + 1,
            "endRowIndex": index + 2,
            "startColumnIndex": 0,
            "endColumnIndex": 5
          },
          "shiftDimension": "ROWS"   # Indicates that the cells below should be removed
        }
      }
      service = build('sheets', 'v4', credentials=creds)
      service.spreadsheets().batchUpdate(spreadsheetId=SAMPLE_SPREADSHEET_ID, body={"requests": [request]}).execute()
      tree.delete(selected_item)
      filter()

    # Create the button to delete the data
    delete_button = Button(root, text="Delete", font=("Arial", 16), command=delete_record)
    delete_button.grid(row=4, column=2, padx=2, pady=2, sticky="NSEW")

    # Create the label to display the total of prices and the number of rows
    total_label = Label(root, text="Total: R$ 0", font=("Arial", 16))
    total_label.grid(row=5, column=0, columnspan=5, padx=2, pady=2, sticky="W")

    def sum_prices():
      total = 0.0
      rows = 0.0
      data = tree.get_children()
      for row in data:
          row_values = tree.item(row)["values"]
          prices = []
          for v in row_values[4:]:
              if isinstance(v, str):
                  price = float(v.replace(",", "."))
                  prices.append(price)
              else:
                  prices.append(v)
          total += sum(prices)
          rows += 1

      total_label.configure(text="Total: R$ {:,.2f} - Rows: {:,.0f}".format(total, rows), bg="white")
    sum_prices()

    # Library that allows working with Excel files
    import openpyxl

    def export_to_excel():
      workbook = openpyxl.Workbook()  # Create an Excel file
      worksheet= workbook.active

      columns = [tree.heading(col)["text"] for col in tree["columns"]]  # Get the column names from the Treeview
      worksheet.append(columns)  # Add the column names to the first row of the worksheet

      # Read the data from the Google Sheets
      for row in tree.get_children():
        values = [tree.item(row)["values"] [i] for i in range(len(columns))] #[tree["columns"].index(col)])
        worksheet.append(values)

      workbook.save("data.xlsx")  # Save the Excel file

      # Create an Excel workbook object
    export_button = Button(root, text="Export Data",  font=("Arial", 14),  command=export_to_excel)
    export_button.grid(row=4, column=3, padx=2, pady=2, sticky="NSEW")

    def export_and_separate():

      # Create a dictionary to store the worksheets
      worksheets = {}
      # Iterate through the rows of the treeview and add each row to the worksheet
      for row in tree.get_children():
        # Get the value of column A to use as the worksheet name
        column_a_value = tree.item(row)["values"][0]
        # Check if the worksheet already exists in the dictionary and create a new one if it doesn't
        if column_a_value not in worksheets:
          worksheets[column_a_value] = []
        # Add the row data to the worksheet
        worksheets[column_a_value].append([str(value) for value in tree.item(row)["values"]])

      # Iterate through the worksheet and save each column grouped by column A in a separate file
      for worksheet_name, rows in worksheets.items():
        # Create an Excel file
        workbook = openpyxl.Workbook()  # Create an Excel file
        worksheet= workbook.active
        worksheet.title = worksheet_name

        # Write the column headers
        columns = [tree.heading(col)["text"] for col in tree["columns"]]  # Get the column names from the Treeview
        worksheet.append(columns)  # Add the column names to the first row of the worksheet

        # Read the data from the Google Sheets
        for row in rows:
          worksheet.append(row)

        workbook.save(f"{worksheet_name}.xlsx")  # Save the Excel file

      # Create an Excel workbook object
    export_and_separate_button = Button(root, text="Export and Separate",  font=("Arial", 14),  command=export_and_separate)
    export_and_separate_button.grid(row=4, column=4, padx=2, pady=2, sticky="NSEW")    

    root.mainloop()

  except HttpError as err:
    print(err)

if __name__ == "__main__":
  main()