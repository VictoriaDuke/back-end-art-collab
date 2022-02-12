from app import db
# from app.models.collaborator import collaborators


collaborators = db.Table('collaborators',
    db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True)
)

class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable = False)
    description = db.Column(db.String(64), nullable = False)
    # make string len longer for title & description?
    location = db.Column(db.String, nullable = True)
    # separate physical location for collab vs online collaboration
    # ------------------------------------------------
    # For form:
    # Collab Online only? Check box
    # Collab at Physical location (optional): String
    # ------------------------------------------------
    art_medium = db.Column(db.String, nullable = False)
    # check boxes instead? ex. painting, drawing, multimedia, etc.
    start_date = db.Column(db.DateTime, nullable = True)
    end_date = db.Column(db.DateTime, nullable = True)
    # need to make date format consistant? i.e. month-day-year
    accepting_collaborators = db.Column(db.Boolean, nullable = False)
    # change above attribute?
    
    # -----------------------------------------------
    # Above are my searchable tags. Add as needed.
    # -----------------------------------------------

    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    owner_user = db.relationship("User", back_populates="owned_projects")
    collaborator_users = db.relationship("User", secondary=collaborators)

    
    def to_dict(self):
        return({
            "project_id": self.project_id,
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "art_medium": self.art_medium,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "accepting_collaborators": self.accepting_collaborators,
            "user_id":self.user_id,
            "owner_user": self.owner_user,
            "collaborator_users": self.collaborator_users

        })


