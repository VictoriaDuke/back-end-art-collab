from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.project import Project
from app.models.user import User
# from above - collaborators
from sqlalchemy.orm import Session
from sqlalchemy import select
# from app.models.collaborator import Collaborator
# necessary to import User or Collaborator?

bp = Blueprint("projects", __name__, url_prefix="/projects")

# Helper functions
# def validate_request_body(request_body):
#     """Validates that mandatory fields present in request body.
#     Aborts with a 400 if required data missing.
#     """
#     mandatory_fields = ["name", "bio_note"]
#     for field in mandatory_fields:
#         if field not in request_body:
#             abort(make_response({"error": f"User must include {field}."}, 400))
#     return True

# GET /projects
# gets all projects from all users (don't need POST or DELETE as those will be under /users/<user_id>)
@bp.route("", methods=["GET"])
def get_projects():
    """Reads all created projects"""
    projects_response = []
    projects = Project.query.all()

    for project in projects:
        projects_response.append(project.to_dict())

    # response = jsonify(projects_response)
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return jsonify(projects_response), 200

# GET /projects/<project_id>
@bp.route("/<project_id>", methods=["GET"])
def handle_projects(project_id):
    project = Project.query.get(project_id)
    if project is None:
        return "The project does not exist!", 404




# GET /projects/<project_id>/collaborators
# gets all collaborators for a specific project
@bp.route("/<project_id>/collaborators", methods=["GET"])
def get_collaborators(project_id):
    """Reads all collaborators for specific project"""
    project = Project.query.get(project_id)

    collaborators_response = []
    # collaborator_users = select(collaborators).where(collaborators.project_id == id)
    # [collaborators.c.project_id, collaborators.c.user_id]).filter(collaborators.c.project_id == project_id).all()
    # project_collaborators = db.select([collaborators.c.project_id, collaborators.c.user_id])
    # collaborators = User.query.get('project_id')
    # collaborators = User.query.join(collaborators).join(Project).filter((collaborators.columns.user_id == User.user_id) & (collaborators.columns.project_id == Project.project_id)).all()

    # add owner_user too? and to the jsonify?

    # if current_user = project[owner_user]
    # above only if I have sign-in feature for current_user
    
    for user in project.collaborator_users:
        collaborators_response.append(user.to_dict_collaborators())

    return jsonify(collaborators_response), 200

# for security - should require user auth to delete projects for user_id
# # Move delete over to /users/<user_id>/projects so that an authenticated user/owner can be the only one to delete
# #DELETE
# @bp.route("/<project_id>", methods = ["DELETE"])
# def delete_project(project_id):
    
#     if not project_id.isnumeric():
#         return { "Error": "Project id must be numeric."}, 404
#     project_id = int(project_id)
#     project = Project.query.get(project_id)
    
#     if not project:
#         return "Project does not exist", 404
            
#     db.session.delete(project)
#     db.session.commit()

#     return {
#         'message': f'Project {project.project_id} by owner {project.user_id.name} (user_id:{project.user_id}) was successfully deleted'
#     }, 200

# Add more as needed


# Below unneeded

# #LIKE PUT
# @bp.route("/<project_id>/like", methods = ["PUT"])
# def like_card(card_id):
#     card_id = int(card_id)
#     card = Card.query.get(card_id)
#     card.likes_count +=1

#     db.session.commit()
#     return ({
#         "message": "+1 Like!",
#         "likes_count": card.likes_count
#         }),200


