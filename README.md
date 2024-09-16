# Booking Hotel

A Basic Hotel System for a startup to let users manage Customers and Hotel Bookings.
## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/HadyHany23/Booking
    cd Booking
    ```
2. **Install pip (if not already installed):**

   **For Windows:**
    ```bash
    python -m ensurepip --upgrade
    ```

   **For macOS/Linux:**
    ```bash
    sudo apt-get install python3-pip  # For Debian-based distributions
    sudo yum install python3-pip      # For Red Hat-based distributions
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

