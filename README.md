# Django E-commerce Platform

A full-featured e-commerce web application built with Django, providing a complete online shopping experience with product catalog, shopping cart, user authentication, order management, and integrated payment processing.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [API Integration](#api-integration)
- [License](#license)

## Overview

This Django-based e-commerce platform provides a robust solution for online retail operations. The application is designed with a modular architecture, separating concerns into distinct apps for products, shopping cart, user management, orders, and payment processing. The platform supports product variants with size and stock management, session-based and persistent cart functionality, and secure payment processing through Stripe integration.

## Key Features

### Product Management
- **Product Catalog**: Browse products organized by categories with detailed product pages
- **Product Variants**: Support for multiple sizes with individual stock tracking per size
- **Search and Filter**: Advanced product search and filtering capabilities
- **Category System**: Hierarchical category organization with slug-based URLs
- **Image Management**: Product image uploads with dedicated media storage

### Shopping Cart
- **Session-Based Cart**: Persistent cart functionality across sessions
- **Real-Time Updates**: Dynamic cart updates without page reload
- **Stock Validation**: Automatic stock checking during cart operations
- **Cart Middleware**: Custom middleware for cart management across the application
- **Quantity Management**: Add, update, and remove items with quantity controls

### User Management
- **Custom User Model**: Extended user model with email-based authentication
- **User Profiles**: Comprehensive user profiles with shipping information
- **Authentication System**: Secure login, registration, and password management
- **Address Management**: Save and manage multiple shipping addresses
- **Order History**: Users can view their complete order history

### Order Processing
- **Checkout Flow**: Multi-step checkout process with form validation
- **Order Tracking**: Order status tracking (pending, processing, shipped, delivered, cancelled)
- **Order Details**: Complete order information including items, quantities, and prices
- **Email Integration**: Order confirmation and notification system
- **Guest Checkout**: Support for guest user purchases

### Payment Integration
- **Stripe Integration**: Secure payment processing through Stripe API
- **Payment Success/Cancel Pages**: Dedicated pages for payment outcomes
- **Webhook Support**: Stripe webhook handling for payment verification
- **Order Confirmation**: Automatic order creation upon successful payment
- **Transaction Security**: PCI-compliant payment processing

### Additional Features
- **Responsive Design**: Mobile-friendly interface with template inheritance
- **Admin Panel**: Comprehensive Django admin interface for management
- **Context Processors**: Custom context processors for global data availability
- **Template Tags**: Custom template tags for cart functionality
- **Database Transactions**: Atomic database operations for data integrity

## Technology Stack

### Backend
- **Django 5.2.4**: High-level Python web framework
- **Python 3.x**: Programming language
- **PostgreSQL**: Relational database management system
- **psycopg2**: PostgreSQL adapter for Python

### Frontend
- **Django Templates**: Server-side template rendering
- **HTML/CSS**: Markup and styling
- **JavaScript**: Client-side interactivity

### Payment Processing
- **Stripe 12.4.0**: Payment processing and API integration

### Additional Libraries
- **Pillow 11.3.0**: Python Imaging Library for image handling
- **python-dotenv 1.1.1**: Environment variable management
- **requests 2.32.5**: HTTP library for API calls

### Development Tools
- **Django Debug Toolbar**: Development debugging (optional)
- **SQLParse**: SQL parsing and formatting

## Project Structure

```
E-commerce/
├── ecommerce/                  # Main project directory
│   ├── manage.py              # Django management script
│   ├── ecommerce/             # Project configuration
│   │   ├── settings.py        # Application settings
│   │   ├── urls.py            # Root URL configuration
│   │   ├── wsgi.py            # WSGI configuration
│   │   └── asgi.py            # ASGI configuration
│   ├── main/                  # Product catalog app
│   │   ├── models.py          # Product, Category, Size models
│   │   ├── views.py           # Product views
│   │   ├── urls.py            # Product URL patterns
│   │   ├── forms.py           # Product forms
│   │   └── templates/         # Product templates
│   ├── cart/                  # Shopping cart app
│   │   ├── models.py          # Cart and CartItem models
│   │   ├── views.py           # Cart views
│   │   ├── cart.py            # Cart business logic
│   │   ├── middleware.py      # Cart middleware
│   │   ├── context_processors.py  # Cart context processor
│   │   ├── templatetags/      # Custom template tags
│   │   └── templates/         # Cart templates
│   ├── users/                 # User management app
│   │   ├── models.py          # CustomUser model
│   │   ├── views.py           # User views
│   │   ├── forms.py           # User forms
│   │   └── templates/         # User templates
│   ├── orders/                # Order management app
│   │   ├── models.py          # Order and OrderItem models
│   │   ├── views.py           # Order views
│   │   ├── forms.py           # Order forms
│   │   └── templates/         # Order templates
│   └── payment/               # Payment processing app
│       ├── views.py           # Payment views
│       ├── urls.py            # Payment URL patterns
│       └── templates/         # Payment templates
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

## Installation

### Prerequisites

- Python 3.8 or higher
- PostgreSQL 12 or higher
- pip (Python package manager)
- Virtual environment tool (venv or virtualenv)

### Steps

1. Clone the repository:
```bash
git clone <repository-url>
cd E-commerce
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Configuration

### Environment Variables

Create a `.env` file in the `ecommerce` directory with the following variables:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Configuration
POSTGRES_DB=your_database_name
POSTGRES_USER=your_database_user
POSTGRES_PASSWORD=your_database_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Stripe Configuration
STRIPE_SECRET_KEY=your_stripe_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret
```

### Security Notes

- Never commit the `.env` file to version control
- Generate a strong SECRET_KEY for production
- Set DEBUG=False in production environments
- Configure ALLOWED_HOSTS for production deployment

## Database Setup

1. Create a PostgreSQL database:
```sql
CREATE DATABASE your_database_name;
CREATE USER your_database_user WITH PASSWORD 'your_database_password';
GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_database_user;
```

2. Run migrations:
```bash
cd ecommerce
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser:
```bash
python manage.py createsuperuser
```

4. Load initial data (optional):
```bash
python manage.py loaddata initial_data.json
```

## Running the Application

### Development Server

Start the Django development server:
```bash
cd ecommerce
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.

### Static and Media Files

Collect static files for production:
```bash
python manage.py collectstatic
```

## Usage

### For Administrators

1. **Product Management**: Add products, categories, and sizes through the admin panel
2. **Order Management**: View and update order statuses
3. **User Management**: Manage user accounts and permissions
4. **Inventory Control**: Monitor and update stock levels

### For Customers

1. **Browse Products**: View product catalog and search for items
2. **Add to Cart**: Select sizes and add products to cart
3. **User Registration**: Create an account for faster checkout
4. **Checkout**: Complete purchase with saved address information
5. **Payment**: Securely pay with credit/debit card through Stripe
6. **Order Tracking**: View order history and status

## API Integration

### Stripe Payment Integration

The application uses Stripe for payment processing. Configure your Stripe account:

1. Create a Stripe account at https://stripe.com
2. Obtain your API keys from the Stripe Dashboard
3. Add the keys to your `.env` file
4. Configure webhook endpoints for payment verification

### Webhook Configuration

Set up Stripe webhooks to handle payment events:
- Endpoint URL: `https://your-domain.com/payment/webhook/`
- Events to listen: `checkout.session.completed`, `payment_intent.succeeded`

## License

This project is proprietary software. All rights reserved.

---

For support or inquiries, please contact the development team.
