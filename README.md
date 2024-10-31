
# Timesheet-Tracker Application

A Django-based time-tracking application that enables users to log task-specific hours, browse past entries, and manage their project times effectively. The application is designed with simplicity and functionality in mind, focusing on core features for logging and reviewing time entries.

## Features

### 1. **User Registration and Authentication**
   - **Registration**: Users can register with essential details like name, username, and email.
   - **Login/Logout**: Secure authentication to protect user data and restrict access.

### 2. **Time Entry Management**
   - **Add Time Entry**:
     - **Task Name Input**: Users can specify the name of the task they are working on.
     - **Project Selection**: A dropdown menu allows users to select the relevant project.
     - **Start and End Time**: Users can manually input start and end times.
     - **Timer Feature**: An integrated timer helps track task duration automatically for enhanced precision.
   - **Browse Time Entries**:
     - **View Past Entries**: Users can review previous entries to track productivity over time.
     - **Filter by Date**: The application allows date-based filtering for easier access to older entries.

### 3. **Dashboard and Analytics**
   - **Dashboard Overview**: The main dashboard displays recent entries, providing users with a quick overview of their latest logged hours.
   - **Time Summary**: Users can see accumulated hours by project, with options to filter by weekly or monthly views.
   - **Data Visualization**: Charts illustrate time allocation across different projects for clearer insights into time distribution.

### 4. **Data Storage and Export**
   - **Database**: All entries are securely stored in SQLite database.  
   - **Data Export**: Users can export their time entries as a CSV file, facilitating easy data transfer for payroll or analysis.


## Usage

1. **Register/Login**: Register a new account or log in with existing credentials.
2. **Create Time Entries**: Add new entries with task name, project, start and end time, or use the timer feature.
3. **Dashboard Insights**: View recent entries, total time spent, and filter by project or time range.
4. **Data Export**: Export time entries to CSV for records or further analysis.

## Project Structure and Design Principles

- **Modularity and Code Reusability**: Code is structured into reusable modules for maintainability and scalability.
- **Error Handling**: Thoughtful error handling ensures robust user interaction.
- **UI Design**: A simple, clean interface makes navigation intuitive, aligning with core user needs.
