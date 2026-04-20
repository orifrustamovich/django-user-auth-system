# 🔐 Django User Authentication System
 
A production-ready Django authentication system with email verification, built following clean architecture principles and Django best practices.
 
---
 
## ✨ Features
 
- 👤 **Custom User Model** — fully extensible for future fields
- 📝 **User Registration** — clean signup flow with validation
- 📧 **Email Verification** — confirmation code sent via Gmail SMTP
- 🔑 **Secure Login** — only verified users can access the system
- 🚪 **Logout** — session-based, safe sign-out
- 🧾 **Crispy Forms** — Bootstrap 5 powered UI forms
- ⚙️ **Environment Config** — `.env` based settings, no hardcoded secrets
- 🧠 **Clean Architecture** — readable, maintainable, scalable codebase
---
 
## 🛠️ Tech Stack
 
| Layer | Technology |
|---|---|
| Backend | Django (Python 3.x) |
| Environment | Pipenv |
| Forms UI | django-crispy-forms + Bootstrap 5 |
| Email | SMTP (Gmail) |
| Config | python-dotenv |
 
---
 
## 📁 Project Structure
 
```
django-user-auth-system/
│
├── accounts/        # Custom user model, auth views, forms, email logic
├── pages/           # Static pages (home, about, etc.)
├── config/          # Django project settings
├── templates/       # HTML templates (base, auth pages)
│
├── .env             # Environment variables (NOT committed to git)
├── .env.example     # Example config for quick setup
├── Pipfile          # Dependency management
└── manage.py
```
 
---
 
## ⚙️ Setup & Installation
 
### 1. Clone the Repository
 
```bash
git clone https://github.com/orifrustamovich/django-user-auth-system.git
cd django-user-auth-system
```
 
### 2. Install Dependencies
 
```bash
pipenv install
pipenv shell
```
 
### 3. Configure Environment Variables
 
```bash
cp .env.example .env
```
 
Fill in the required values in `.env`:
 
```env
SECRET_KEY=your_django_secret_key
DEBUG=True
 
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```
 
### 4. Apply Migrations & Run
 
```bash
python manage.py migrate
python manage.py runserver
```
 
Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
 
### 5. Create Admin User (Optional)
 
```bash
python manage.py createsuperuser
```
 
Admin panel: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
 
---
 
## 📧 Gmail SMTP Setup
 
To enable real email sending:
 
**Step 1:** Go to your Google Account → **Security** → Enable **2-Step Verification**
 
**Step 2:** Visit [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
- Select **Mail** → **Other (Custom name)** → Enter `Django App`
- Click **Generate** — you'll receive a 16-character password
**Step 3:** Copy the password (remove spaces) into your `.env`:
 
```env
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```
 
> ⚠️ Never use your real Gmail password. Always use an App Password.
 
---
 
## 🔄 Authentication Flow
 
```
User Signs Up
     ↓
Confirmation Code Sent via Email
     ↓
User Enters Code → Email Verified
     ↓
Account Activated
     ↓
User Can Now Log In
```
 
---
 
## 🔒 Security Notes
 
- `.env` is excluded from version control via `.gitignore`
- App Passwords are used instead of real Gmail credentials
- Email verification prevents unauthorized or bot registrations
- Sessions are properly invalidated on logout
---
 
## 🗺️ Roadmap
 
- [ ] JWT Authentication (REST API support)
- [ ] Password Reset via Email
- [ ] Docker Deployment
- [ ] Production Deployment (AWS / GCP / Render)
- [ ] Rate Limiting & Brute-Force Protection
- [ ] OAuth (Google, GitHub login)
---
 
## 🤝 Contributing
 
Contributions are welcome! Here's how:
 
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request
Please make sure your code follows the existing style and includes relevant comments.
 
---
 
## 📄 License
 
This project is open-source and available under the [MIT License](LICENSE).
 
---
 
## 👨‍💻 Developer
 
**Orifjon Toshtemirov** — Backend Developer (Python / Django)
Focused on building clean, scalable, and production-ready systems.
 
- 🌐 GitHub: [@orifrustamovich](https://github.com/orifrustamovich)
- 📍 Based in South Korea
---
 
⭐ If you found this project useful, consider giving it a star!
 