from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.user import User
from app.models.project import Project
# from app.models.collaborator import Collaborator
# necessary to import Collaborator?

bp = Blueprint("users", __name__, url_prefix="/users")

# Helper functions
def validate_request_body(request_body):
    """Validates that mandatory fields present in request body.
    Aborts with a 400 if required data missing.
    """
    mandatory_fields = ["name", "bio_note"]
    for field in mandatory_fields:
        if field not in request_body:
            abort(make_response({"error": f"User must include {field}."}, 400))
    return True

def validate_project_body(request_body):
    """Validates that mandatory fields present in project request body.
    Aborts with a 400 if required data missing.
    """
    mandatory_fields = ["title", "description", "art_medium", "accepting_collaborators"]
    for field in mandatory_fields:
        if field not in request_body:
            abort(make_response({"error": f"Project must include {field}."}, 400))
    return True

# GET /users
@bp.route("", methods=["GET"])
def get_users():
    """Reads all created users"""
    users_response = []
    users = User.query.all()

    for user in users:
        users_response.append(user.to_dict())

    return jsonify(users_response), 200

# POST /user
@bp.route("", methods=["POST"])
def post_user():
    """Creates a new user from user input."""
    data = request.get_json()
    validate_request_body(data)

    new_user = User(
        name=data["name"],
        bio_note=data["bio_note"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user.to_dict()), 201

# DELETE /users/<user_id>
@bp.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if not user_id.isnumeric():
        return {"Error": "User id must be numeric"}, 404

    user_id = int(user_id)
    user = User.query.get(user_id)

    if not user:
        return "User does not exist", 404
    
    db.session.delete(user)
    db.session.commit()

    return {
        'message': f'User {user.user_id} was successfully deleted'
    }, 200


# GET and POST for  /users/<user_id>/projects
@bp.route("/<user_id>/projects", methods=["GET", "POST"])
def handle_projects(user_id):
    user = User.query.get(user_id)
    if user is None:
        return "The user does not exist!", 404

    if request.method == "POST":
        request_body = request.get_json()
        validate_project_body(request_body)
        new_project = Project(
        title=request_body["title"],
        description=request_body["description"],
        location=request_body["location"],
        art_medium=request_body["art_medium"],
        start_date=request_body["start_date"],
        end_date=request_body["end_date"],
        accepting_collaborators=bool(request_body["accepting_collaborators"]), 
        user_id=user_id
    )
        db.session.add(new_project)
        db.session.commit()
        return jsonify(new_project.to_dict()), 201

    elif request.method == "GET":
        owned_projects_response = []
    for project in user.owned_projects:
        owned_projects_response.append(project.to_dict())

    return jsonify({
        "user_id":user.user_id,
        "name":user.name,
        "bio_note":user.bio_note,
        "owned_projects" :owned_projects_response
        })

# Move delete over from /projects to /users/<user_id>/projects so that an authenticated user/owner can be the only one to delete
#DELETE
@bp.route("/<user_id>/projects/<project_id>", methods = ["DELETE"])
def delete_project(project_id):
    
    if not project_id.isnumeric():
        return { "Error": "Project id must be numeric."}, 404
    project_id = int(project_id)
    project = Project.query.get(project_id)
    
    if not project:
        return "Project does not exist", 404
            
    db.session.delete(project)
    db.session.commit()

    return {
        'message': f'Project {project.project_id} by owner {project.user_id.name} (user_id:{project.user_id}) was successfully deleted'
    }, 200

# for security - should require user auth to delete user or post & delete projects for user_id
# also use user auth for post/patch/delete collaborators from projects they own


# GET collaborators for project
####### does this interfer with /projects/<project_id>/collaborators route in project.py?
@bp.route("/<user_id>/projects/<project_id>/collaborators", methods = ["GET"])
def get_collaborator_users(user_id, project_id):
    """Reads all collaborator users for specific project_id"""
    # owner_user = User.query.get(user_id)
    project = Project.query.get(project_id)
    collaborator_users_response = []
    collaborator_users_response.append(project.owner_user.to_dict())

    for collaborator_user in project.collaborator_users:
        collaborator_users_response.append(collaborator_user.to_dict_collaborators())
        # need diff to_dict?
    
    # res = {"owner_user": owner_user, "collaborators": collaborator_users_response}

    return jsonify(collaborator_users_response), 200
