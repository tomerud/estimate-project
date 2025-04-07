# Estimate Project

Estimate Project is a Flask-based web application that helps users estimate the cost of their trips based on destination, duration, and travel type. The application provides a simple interface for users to input their travel details and receive an estimated cost based on predefined rules.

---

## **Features**
- Input travel destination, duration, and travel type (Backpacker, Average, or Expensive).
- Calculate trip costs based on travel type and duration.
- Validate destinations against a database of cities.
- Display a message if the destination is unavailable.

---

## **How to Run the Project**

### **1. Prerequisites**
Before running the project, ensure you have the following installed:
- Python 3.10 or higher
- pip (Python package manager)
- MySQL server

---

### **2. Clone the Repository**
Clone the project repository to your local machine:
```bash
git clone git@github.com:tomerud/estimate-project.git
cd estimate-project
```

### **3. Create and Activate a Virtual Environment**
Create a virtual environment:
```bash
python -m venv .venv
```

Activate the virtual environment:
```bash
# On Windows:
.venv\Scripts\activate
```

Install the required packages:
```bash
pip install -r requirements.txt
```

### **4. Create the Database**
Create the database:
```sql
CREATE DATABASE estimate;
```

Run the database creation script:
```bash
python DB/create_tables.py
```

### **5. Configure the Database Connection**
Create a `.env` file in the project root directory and add the following configuration:
```markdown
DB_HOST=127.0.0.1
DB_USER=root
DB_PASSWORD=your_password_here
DB_NAME=estimate
```

### **6. Run the Application**
Run the application:
```bash
python app.py
```