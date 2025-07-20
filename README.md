# Skill Sensei CLI 🧠📚

A Command Line Interface (CLI) application built with Python and PostgreSQL to help users **track, manage, and improve their skills** over time. Perfect for self-learners, developers, and students who want to monitor their learning progress and organize their study resources.

---

## 🚀 Features

- ✅ Add, update, delete, and search **skills**
- 📈 Track your **proficiency level**, **target level**, **start date**, and **goal date**
- 🔗 Manage **resources** for each skill (e.g. tutorials, books, videos)
- 🔍 Search and filter skills and resources
- 💾 Persistent storage using **PostgreSQL**

---

## 📂 Project Structure

Skill-Sensei-CLI/
├── .idea/ # IDE settings (ignored)
├── DataBase/ # Database setup & table creation
│ └── init_db.py
├── logic/ # Core logic for skills and resources
│ ├── skill.py
│ └── resource.py
├── utils/ # Helper functions (e.g., DB connection)
│ └── db_utils.py
├── .env # Environment variables (ignored by Git)
├── .gitignore # Git ignore file
├── main.py # Main CLI interface
├── requirements.txt # Python dependencies
└── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/santoryuZ/Skill-Sensei-CLI.git
cd Skill-Sensei-CLI
### 2. Set Up Your Virtual Environment


python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
### 3. Install Dependencies

pip install -r requirements.txt
### 4. Configure Environment Variables
Create a .env file in the root directory and add:

env

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
### 5. Initialize the Database

python DataBase/init_db.py
### 6. Run the App

Copy code
python main.py
