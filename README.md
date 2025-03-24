# Bookstore Web Application

This is a simple bookstore web application built using Streamlit. The application allows users to browse books, add them to a cart, and proceed to checkout. It also includes a chatbot to assist users with common queries.

## Features

- Home page with a welcome message
- Books page to browse available books
- Cart page to view and manage items in the cart
- Checkout page to complete the purchase
- Chatbot to assist users with common queries

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/ecommerce-web-app.git
    cd ecommerce-web-app
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS/Linux
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```sh
    streamlit run src/app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to access the application.

## Project Structure

```
ecommerce-web-app/
├── src/
│   ├── app.py
│   ├── chatbot.py
│   ├── pages/
│   │   ├── home.py
│   │   ├── products.py
│   │   ├── cart.py
│   │   └── checkout.py
├── requirements.txt
└── README.md
```

## Dependencies

- `streamlit`: Web application framework
- `fpdf`: Library for generating PDF bills
- `chatbot`: Custom chatbot implementation