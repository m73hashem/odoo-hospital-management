# Odoo Hospital Management System

🚀 **An Odoo module for managing hospital operations, including patients, doctors, appointments, prescriptions, and medicines.**  

## 📌 Overview
This Odoo module provides a hospital management system that allows users to:  
✔ Register and manage **patients** and **doctors**.  
✔ Schedule and track **appointments**.  
✔ Maintain **prescriptions** for each appointment.  
✔ Manage **medicines** and their details.  
✔ Streamline hospital transactions via an easy-to-use interface.  

## 🏗 Features
### ✅ Patients Management
- Extend `res.partner` to include patient-related details (Age, Birthdate, Appointments).  
- Track the number of appointments per patient.  

### ✅ Doctors Management
- Extend `res.users` to add **Doctor** and **Supervisor** roles.  
- Display doctors in a dedicated list view.  

### ✅ Appointments Management
- Auto-generate appointment **IDs**.  
- Assign **patients and doctors** to appointments.  
- Track the **status** of an appointment (Draft, Confirmed, Done, Canceled).  
- Allow doctors to add **notes and prescriptions**.  

### ✅ Prescriptions & Medicines Management
- Link **prescriptions** to appointments.  
- Manage a **list of medicines** with effective ingredients.  

### ✅ Odoo UI Integration
- Custom **menus** for Patients, Doctors, Appointments, and Medicines.  
- **Buttons** to manage appointment workflows.  
- **Kanban, List, and Form views** for easy navigation.  

## 🔧 Installation

### 1️⃣ Prerequisites
- Odoo 14+ (Ensure your Odoo environment is set up)  
- Python 3.x  
- PostgreSQL  

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/m73hashem/odoo-hospital-management.git
```

### 3️⃣ Move to Odoo Addons Directory
```bash
mv odoo-hospital-management /path/to/odoo/custom/addons/
```

### 4️⃣ Restart Odoo Server
```bash
cd /path/to/odoo/
./odoo-bin --addons-path=addons,custom/addons/ -u the_app
```

## 🚀 Usage
1️⃣ **Activate Developer Mode** in Odoo.  
2️⃣ Navigate to **Hospital → Appointments / Doctors / Patients / Medicines**.  
3️⃣ Manage patients, schedule appointments, and track medical records.  

## 📜 Technical Details
- **Models Defined:**
  - `res.partner` (Extended for Patients)  
  - `res.users` (Extended for Doctors)  
  - `the.appointments` (Manages Appointments)  
  - `the.prescription` (Stores Prescriptions)  
  - `the.medicines` (Stores Medicine Info)  

- **Views Included:**  
  ✔ Tree, Form, Kanban for appointments, prescriptions, and doctors.  
  ✔ Custom buttons for workflow management.  
  ✔ Dynamic statistics on patients.  

## 👨‍💻 Contributing
Want to improve this module? Follow these steps:  
1️⃣ Fork this repository.  
2️⃣ Create a new branch: `git checkout -b feature-name`.  
3️⃣ Commit your changes: `git commit -m "Added new feature XYZ"`.  
4️⃣ Push to your fork and submit a **Pull Request**.  

## 📜 License
This project is licensed under the **MIT License**.  

## 📩 Contact
💡 **Need help or want to collaborate?**  
📧 Email: [m73.hashem@gmail.com]  
🔗 GitHub: [github.com/m73hashem]  
🔗 LinkedIn: [linkedin.com/in/mahmoudhashem]  
