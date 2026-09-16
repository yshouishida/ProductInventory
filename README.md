# Product Inventory API

This Flask API exposes CRUD endpoints for products stored in MySQL.

## Setup

1. Install Python dependencies: `python -m pip install -r requirements.txt`
2. Create the MySQL database and tables with `backend/database/database.sql`.
3. Copy `backend/.env.example` to `backend/.env` and fill in the database credentials. Set `JWT_SECRET_KEY` to a random secret of at least 32 bytes.
4. Start the server with `python run.py`.

The database must be reachable from the machine running Flask. The app reads `backend/.env` regardless of the working directory.
If a TCP connection to port 3306 succeeds but no MySQL greeting arrives, check that a healthy MySQL server is listening on that port.

## Endpoints

| Method | Path | Action |
| --- | --- | --- |
| GET | `/products` | List products |
| GET | `/products/<id>` | Get one product |
| POST | `/products` | Add a product |
| PUT | `/products/<id>` | Replace a product |
| DELETE | `/products/<id>` | Delete a product |
| POST | `/login` | Sign in and receive a JWT |

POST and PUT accept JSON with `code` (1–20 characters), `name` (1–100 characters), optional `description`, nonnegative integer `qty`, and nonnegative `price` with at most two decimal places. Missing products return 404, malformed product data returns 400, and unexpected server errors return 500.

To add a login user, generate a password hash with `python -c "from getpass import getpass; from werkzeug.security import generate_password_hash; print(generate_password_hash(getpass('Password: ')))"`, then run `INSERT INTO tblUsers (username, password, role) VALUES ('alice', '<generated hash>', 'admin');` with the generated hash substituted. Passwords must be stored as Werkzeug hashes, not plain text.

Send `POST /login` with JSON such as `{"username":"alice","password":"your-password"}`. A successful response contains `data.access_token` and a user object without the password hash. Invalid credentials return 401. Product routes are currently public; the JWT helpers can be applied when route protection is desired.

Run the API checks with `python -m unittest discover -s tests -v`. They use mocks and do not require MySQL.
