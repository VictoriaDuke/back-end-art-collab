from app import db
# from app.models.collaborator import collaborators
from sqlalchemy import ForeignKey



# collaborators = db.Table('collaborators',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
#     db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True)
# )

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    bio_note = db.Column(db.String)
    # set length limits?
    owned_projects = db.relationship("Project", back_populates="owner_user")
    # collaborator_projects = db.relationship("Project", secondary="collaborators")
    # collaborator = db.relationship("Collaborator", back_populates="collaborator")

    def to_dict(self):
        response_body = {
            "user_id": self.user_id,
            "name": self.name,
            "bio_note": self.bio_note
        }
    
        # include title of all user's projects?
        # ------------------------------------------------
        # TODO: flesh this out later, if we want to list cards when reading boards
        # method would also take cards_list=None as a param
        #
        # if cards_list is not None:
        #     response_body["card"] = cards_list
        # ------------------------------------------------

        return response_body

    # may not need
    def to_dict_collaborators(self):
        response_body = {
            "user_id": self.user_id,
            "name": self.name,
            "bio_note": self.bio_note
        }
        return response_body

