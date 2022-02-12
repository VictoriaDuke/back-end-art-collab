from app import db
from sqlalchemy import ForeignKey

# collaborators = db.Table('collaborators',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.user_id'), primary_key=True),
#     db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True)
# )

# class Collaborator(db.Model):
#     collaborator_id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, ForeignKey('user.user_id'))
#     project_id = db.Column(db.Integer, ForeignKey('project.project_id'))
#     user = db.relationship("User", back_populates="collaborator")
#     project = db.relationship("Project", back_populates="collaborator")



#     def to_dict(self):
#         response_body = {
#             "collaborator_id": self.collaborator_id,
#             "user_id": self.user_id,
#             "project_id": self.project_id
#         }

#         return response_body