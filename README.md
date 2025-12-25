Image Gallery Metadata Management Application

A cloud-based web application that allows users to upload images, store them securely in Azure Blob Storage, manage metadata in Azure Cosmos DB, and view or download images through a web interface.

🚀 Features

Upload images with title and tags

Store images in Azure Blob Storage

Store metadata (URL, title, tags) in Azure Cosmos DB

Fetch and display images dynamically

Download images directly from cloud

Secure environment-based configuration

RESTful Flask API backend

🏗 Architecture
Frontend (HTML, CSS, JS)
        |
        v
Flask REST API (Python)
        |
        v
Azure Blob Storage (Images)
Azure Cosmos DB (Metadata)

🛠 Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python Flask
Storage	Azure Blob Storage
Database	Azure Cosmos DB
Hosting	Azure App Service / Static Web Apps
📂 Project Structure
ImageGalleryProject/
│
├── backend/
│   ├── app.py
│   ├── uploads/
│   ├── .env
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   └── style.css
│
├── docker-compose.yml
└── README.md

⚙ Environment Setup

Create backend/.env

BLOB_CONN=your_blob_connection_string
COSMOS_URI=your_cosmos_uri
COSMOS_KEY=your_cosmos_key

▶ Running Locally
Backend
cd backend
pip install -r requirements.txt
python app.py

Frontend
cd frontend
python -m http.server 5500


Open:

http://127.0.0.1:5500/

🌐 Deployment

Backend hosted on Azure App Service

Frontend hosted on Azure Static Web Apps

Data stored in Azure Blob Storage & Cosmos DB

📌 Future Enhancements

Image delete option

Search by tags

User authentication

Admin panel

Image categories

👨‍💻 Author

Shubhanshu Kumar
Engineering Student – Cloud Computing Enthusiast
