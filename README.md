# Flight Booking System

A Django-based web application for searching and booking flights. This project allows users to search for flights between destinations, view available options, and make bookings with their personal details.

## Features

- **Flight Search**: Search for flights by source and destination
- **Flight Booking**: Book flights with passenger name and email
- **User Authentication**: Register new accounts and login/logout functionality
- **Responsive Design**: Clean, user-friendly interface with HTML templates
- **Database Integration**: SQLite database with Django ORM

## Technologies Used

- **Backend**: Django 6.0.3
- **Database**: SQLite
- **Frontend**: HTML, CSS (SCSS)
- **Python**: 3.x

## Installation

### Prerequisites

- Python 3.x installed on your system
- Git (optional, for cloning the repository)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd Tickets
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install Django**
   ```bash
   pip install django
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Open your browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```

### Available Pages

- **Home** (`/`): Landing page
- **Search Flights** (`/search/`): Search for flights by source and destination
- **Book Flight** (`/book/<id>/`): Book a specific flight
- **Success** (`/success/`): Confirmation page after booking
- **Register** (`/register/`): Create a new user account
- **Login** (`/login/`): User authentication
- **Logout** (`/logout/`): User logout

### Admin Panel

Access the Django admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials to manage flights and bookings.

## Project Structure

```
Tickets/
├── manage.py              # Django management script
├── db.sqlite3            # SQLite database
├── Project/              # Main Django project
│   ├── settings.py       # Project settings
│   ├── urls.py          # Main URL configuration
│   └── ...
├── App/                  # Main Django application
│   ├── models.py        # Database models (Flight, Booking)
│   ├── views.py         # View functions
│   ├── urls.py          # App URL configuration
│   ├── templates/       # HTML templates
│   │   └── App/
│   │       ├── home.html
│   │       ├── search.html
│   │       ├── book.html
│   │       ├── success.html
│   │       ├── login.html
│   │       └── register.html
│   └── static/          # Static files (CSS, JS, images)
│       └── scss/
│           └── style.css
└── migrations/          # Database migrations
```
## Models

### Flight
- `flight_name`: Name of the flight
- `source`: Departure location
- `destination`: Arrival location
- `date`: Flight date
- `price`: Ticket price


### Booking
- `passenger_name`: Name of the passenger
- `email`: Passenger's email address
- `flight`: Foreign key to Flight model

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

For questions or issues, please open an issue in the repository or contact the development team.