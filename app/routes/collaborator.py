# from flask import Blueprint, request, jsonify, make_response
# from app import db
# from app.models.collaborator import Collaborator
# from app.models.user import User
# from app.models.project import Project
# # necessary to import User or Project?


# bp = Blueprint("collaborators", __name__, url_prefix="/collaborators")

# # Put within /projects/<project_id>/collaborators
# # will need GET, POST, and DELETE
# #POST to add a collaborator (would I use the collaborator_id or user_id?)
# # ==== Instead of below, use post method from user.py? ====

# # @bp.route("/<collaborator_id>", methods = ["POST"])
# # def post_collaborator(collaborator_id):
    
# #     if not collaborator_id.isnumeric():
# #         return { "Error": "Collaborator id must be numeric."}, 404
# #     collaborator_id = int(collaborator_id)
# #     collaborator = Collaborator.query.get(collaborator_id)
    
# #     if not collaborator:
# #         return "Collaborator does not exist",404
            
# #     db.session.delete(Collaborator)
# #     db.session.commit()

# #     return {
# #         'message': f'Collaborator {collaborator.collaborator_id} from the project {collaborator.project_id.title} (project_id: {collaborator.project_id}) was successfully deleted'
# #     }, 200

# #DELETE a collaborator (would I use the collaborator_id or user_id?)
# @bp.route("/<collaborator_id>", methods = ["DELETE"])
# def delete_collaborator(collaborator_id):
    
#     if not collaborator_id.isnumeric():
#         return { "Error": "Collaborator id must be numeric."}, 404
#     collaborator_id = int(collaborator_id)
#     collaborator = Collaborator.query.get(collaborator_id)
    
#     if not collaborator:
#         return "Collaborator does not exist",404
            
#     db.session.delete(Collaborator)
#     db.session.commit()

#     return {
#         'message': f'Collaborator {collaborator.user_id.name} (collaborator_id: {collaborator.collaborator_id}) from the project {collaborator.project_id.title} (project_id: {collaborator.project_id}) was successfully deleted'
#     }, 200

# # Add more as needed


# # Below unneeded

# # #LIKE PUT
# # @bp.route("/<card_id>/like", methods = ["PUT"])
# # def like_card(card_id):
# #     card_id = int(card_id)
# #     card = Card.query.get(card_id)
# #     card.likes_count +=1

# #     db.session.commit()
# #     return ({
# #         "message": "+1 Like!",
# #         "likes_count": card.likes_count
# #         }),200


