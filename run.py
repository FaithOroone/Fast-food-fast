from app.auth.views import app
from app.models.database import DatabaseConnection


if __name__ == '__main__':
    DatabaseConnection().auto_admin()
    app.run(debug=True)
