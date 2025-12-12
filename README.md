##  How to Implement the Organization Management Service (Brief Overview)

This backend is designed using **FastAPI** and **MongoDB** to support a **multi-tenant architecture**, where each organization has its own dynamic MongoDB collection. A central **Master Database** stores global metadata, organization details, and admin credentials.

---

##  1.  Setup

 2. Install dependencies

pip install -r requirements.txt


3. Configure MongoDB

Update your connection string inside app/db.py.

A single master database is used.

New collections are created dynamically for each organization.

4. Run the FastAPI server

uvicorn app.main:app --reload  


# Architecture Overview

The service uses the following components:

Routers
Handle API endpoints for organizations and admin authentication.

Service Layer
Contains business logic such as creating organizations, validating credentials, and updating metadata.

Repositories
Interact with MongoDB through Motor (async driver).

Authentication Module
Handles secure password hashing (bcrypt) and JWT generation.

Master Database
Stores:

Organization name

Dynamic collection name

Admin credentials (hashed)

Metadata & connection details

Dynamic Collections
Each new organization gets its own MongoDB collection using the format:

org_<organization_name>


