from Rubicon import db, Role

def role_original ():
    db.create_all()
    roles = ["admin", "manager", "user", "hr"]
    ww = [r.name for r in Role.query.all()]
    for r in roles:
        if r not in ww:
            db.session.add(Role(name = r))
        
    db.session.commit()
    