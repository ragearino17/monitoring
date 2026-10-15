# Flask Monitoring Application

A simple and secure web application built with **Flask** and **Flask-WTF**. This application features a robust custom login validation system, user session tracking, and a dynamic dashboard layout using **Bootstrap**.

## 🚀 Features
* **User Authentication:** Bare-bones login form protected against empty or invalid submissions.
* **Session Tracking:** Secure route protection preventing unauthorized users from accessing internal endpoints directly via the browser address bar.
* **Dynamic Layouts:** A unified Bootstrap navigation bar that automatically changes its item views based on whether the active user is logged in or out.
* **Modern Form Processing:** Uses custom error messages handled seamlessly through Flask view route dictionaries.

## 🛠️ Installation & Setup

Follow these quick commands to set up the project locally on your machine:

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd monitoring
   ```

2. **Install required dependencies:**
   ```bash
   pip install Flask Flask-WTF
   ```

3. **Run the local development server:**
   ```bash
   python app.py
   ```

4. **Access the application:**
   Open your preferred web browser and navigate to `http://127.0.0`

## 🔐 Credentials
* **Username:** `admin`
* **Password:** `admin`
