import sys, os

sys.path.append(os.getcwd() + '/web_app') #sesuai dgn mark directory sources

from app import create_app
from models import Page, db, Role, User

app = create_app()

with app.app_context():

    admin_role = Role()
    admin_role.name = 'admin'
    db.session.add(admin_role)
    db.session.commit()

    root = User()
    root.email = 'alustea@gmail.com'
    root.password = '123456'
    root.active = True
    root.roles.append(admin_role)
    db.session.add(root)

    page = Page()
    page.title = 'Halaman Awal'
    page.contents = '<h1>Selamat Datang!</h1>'
    page.is_homepage = True

    db.session.add(page)
    db.session.commit()