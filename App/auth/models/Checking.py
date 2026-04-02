from Rubicon import db, Role

def role ():
    db.create_all()
    
    if not Role.query.first():
        user = Role(name = "user")
        admin = Role(name = "admin")
        manager = Role(name = "manager")
        staff = Role(name = "staff")
        
        
        db.session.add_all([admin, user, manager, staff])
        db.session.commit()
    