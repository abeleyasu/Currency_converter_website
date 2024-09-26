Currency Converter Website
Introduction
The Currency Converter Website is a web application that allows users to convert amounts between various world currencies using real-time exchange rates. It is built using Flask for the backend and modern web technologies for the frontend. The application is designed to provide a simple, user-friendly experience for anyone needing quick and accurate currency conversions.

Live site: Currency Converter Website
Project Blog Article: Final Blog Post
Authors:
Abel Eyasu – LinkedIn
ABEL Chanyalew – LinkedIn
Screenshot


Installation
Requirements
Python 3.5+
Flask
Virtualenv
Node.js (optional if using npm for frontend)
Step-by-step Guide
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/Currency_converter_website.git
Navigate into the project directory:
bash
Copy code
cd Currency_converter_website
Set up a virtual environment and activate it:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required packages:
bash
Copy code
pip install -r backend/requirements.txt
Start the application:
bash
Copy code
cd backend
python run.py
Usage
Open your browser and navigate to http://localhost:5000 to use the application.
Enter the amount and select the currencies you want to convert between, and the app will display the converted result in real-time.
Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:

Fork the repository.
Create a new branch:
bash
Copy code
git checkout -b feature-branch
Make your changes and commit them:
bash
Copy code
git commit -m "Added new feature"
Push the changes to your branch:
bash
Copy code
git push origin feature-branch
Open a pull request and describe your changes.
Related Projects
Currency Exchange API – The API used to fetch real-time exchange rates for this project.
Currency Converter by Google – A simple currency converter provided by Google.
License
This project is licensed under the MIT License - see the LICENSE file for details.
