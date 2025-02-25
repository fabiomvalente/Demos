# 📊 Google Sheets Integration Project  

This project integrates with **Google Sheets API** to manage and visualize data through a **Python GUI application**.  
It demonstrates a **simple product sales system** with filtering, exporting, and real-time updates.  

## 📄 Google Sheet Structure  

The application expects a Google Sheet with the following structure:  

| 📍 Estado (State) | 🏙️ Cidade (City) | 👨‍💼 Vendedor (Seller) | 📦 Produto (Product) | 💰 Preço (Price) |
|-------------------|-----------------|-----------------|----------------|------------|
| SP               | São Paulo        | João           | Notebook       | 2500.00    |
| RJ               | Rio de Janeiro   | Maria          | Mouse         | 50.00      |

🔹 **Note:** The sheet name **must** match the name used in the code and `.xlsx` file.  

---

## 🚀 Key Features  

✅ **Data Filtering**: Filter by **State, City, Seller, and Product**  
✅ **Data Management**: **Add, edit, and delete** records  
✅ **Data Export**: Export to **Excel** (single file or by state)  
✅ **Real-time Updates**: Sync with **Google Sheets**  
✅ **User-Friendly GUI**: Built with **Tkinter**  

---

## 🛠️ Main Dependencies  

📌 `tkinter` - Python's standard GUI package  
📌 `google-auth` - Google API authentication  
📌 `google-api-python-client` - Google API client  
📌 `google-auth-oauthlib` - OAuth 2.0 support  
📌 `openpyxl` - Excel file manipulation  

---

## 🔧 Installation  

### 1️⃣ Install required packages  

Run the following command:  

`pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client openpyxl`  

### 2️⃣ Set up Google API credentials  
- Create a **project** in **Google Cloud Console**  
- Enable **Google Sheets API**  
- Download `credentials.json`  
- Place it inside the `./oAuth/` directory  

### 3️⃣ Share your Google Sheet with the **service account email**  

---

## ▶️ Usage  

Run the application:  

`python googleSheets.py`  

🔹 The application will:  
1. Authenticate with **Google Sheets API**  
2. Load data from the specified spreadsheet  
3. Provide a **GUI interface** for data management  

---

## ⚙️ Configuration  

Edit these constants in the code:  

```python
SAMPLE_SPREADSHEET_ID = "your-spreadsheet-id"  
SAMPLE_RANGE_NAME = "Dados!A1:E"  # Sheet name and range  
CREDENTIALS_FILE = 'token.json'  # Authentication token
```

---

## 🔄 Application Workflow
1️⃣ Authentication: Uses OAuth 2.0 to access Google Sheets  
2️⃣ Data Loading: Reads data from the specified range  
3️⃣ Data Filtering: Comboboxes for State, City, Seller, and Product  
4️⃣ Data Management:  
- ➕ Add new records
- ✏️ Edit existing records
- ❌ Delete records
5️⃣ Data Export:
- 📂 Export to a single Excel file
- 📁 Export separated by state
