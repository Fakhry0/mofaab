from app import create_app, db
from app.models import User

def create_admin():
    app = create_app()

    with app.app_context():
        username = 'Fakhry0'
        email = 'alylolo223344@gmail.com'
        password = 'Qwe1Asd2Zxc3#'
        
        # Check if the admin user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user is None:
            admin_user = User(username=username, email=email, is_admin=True)
            admin_user.set_password(password)
            db.session.add(admin_user)
            db.session.commit()
            print('Admin user created successfully.')
        else:
            print('Admin user already exists.')
