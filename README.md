# Web Mafia
Web Mafia is the modern successor to the original web-based Mafia game, which was initially built purely with Python and Django.

This version introduces a decoupled architecture:

- 🛠️ Backend: Django REST API
- 🎨 Frontend: React

The goal is to streamline functionality, improve scalability, and make the project easier to maintain and contribute to.

---

# 🚀 TODOs
- Port over API functionality
- Create UI components for Game Host
- Create UI components for players
- Implement web sockets communication for lobby and role distribution

---

# 🛠️ Development Setup
1. It is recommended that you set up a virtual env using Python to keep your dependencies managed in one place.
    ```bash
    python -m venv env_name # Replace 'env_name' with your preferred environment name
    ```

    Activate the virtual environment:
    - Linux/Mac:
        ``` bash
            source env_name/bin/activate
        ```
    - Windows:
        ``` bash
            env_name\Scripts\activate
        ```


    Then install the necessary dependencies 
    ``` bash 
    pip install -r requirements.txt
    ```

    Next, you need to create the database for the service locally. 
    ``` bash
    python manage.py makemigrations
    python manage.py migrate
    ```
    from inside of ./webmafia

2. Frontend Setup (React)

    Navigate to the frontend project ./webmafia
    ``` bash
    npm install
    ``` 
---

# 🏃 Running the Project Locally
from the backend project ./webmafia2
``` bash
python manage.py runserver
```

from the frontend directory ./webmafia
``` bash
npm run dev
```

---
# 🤝 Contributing
If you’d like to contribute, feel free to fork the repository, open issues, or submit pull requests. Collaboration is welcome!
Have a look at the steps that the game follows in STEPS.md and for clues about which endpoints have been created so far, look in service/urls.py

---
# ✅ Notes
- Make sure Python and Node.js are installed on your system.

- This project aims to use WebSockets for real-time communication in the lobby and during role distribution.

- The frontend and backend are developed independently but are tightly integrated through the REST API.