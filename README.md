# Sophos User Import Application

This project is a web application designed to facilitate the import of user data into a Sophos XG Firewall using a user-friendly interface. It allows users to input their credentials, configure options, and manage user data efficiently.

## Features

- User authentication system to secure access to the application.
- Form for importing users from a CSV file.
- Dashboard to display user-specific information and options.
- Configurable input fields for user data.
- Options for various switches to customize user import settings.

## Project Structure

```
sophos-user-import-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   └── user_import.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd sophos-user-import-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the application settings in `config.py`.

## Usage

1. Run the application:
   ```
   python run.py
   ```

2. Access the application in your web browser at `http://localhost:5000`.

3. Log in with your credentials to access the dashboard and user import functionalities.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.