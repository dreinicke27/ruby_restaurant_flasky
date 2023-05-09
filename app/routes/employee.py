from flask import Blueprint, jsonify, request, make_response, abort
from app import db
from app.models.employee import Employee

employee_bp = Blueprint("employee", __name__, url_prefix="/employee")

@employee_bp.route("", methods=["POST"])
def add_employee():
    request_body = request.get_json()
    new_employee = Employee.from_dict(request_body)

    db.session.add(new_employee)
    db.session.commit()

    return {"id": new_employee.id}, 201
    # could use make_response if imported return make_response(f"Restaurant {new_restaurant.title} successfully created with id {new_restaurant.id}", 201)

@employee_bp.route("", methods=["GET"])
def get_employees():
    response = []
    name_query = request.args.get("name")
    #add ability to query by name 
    
    if name_query is None:
        all_employees = Employee.query.all()
    else:
        all_employees = Employee.query.filter_by(name=name_query)

    for employee in all_employees: 
        response.append(employee.to_dict())

    return jsonify(response), 200

@employee_bp.route("/<emp_id>", methods=["GET"])
def get_one_employee(emp_id):
    employee = validate_item(Employee, emp_id)
    
    return employee.to_dict(), 200

@employee_bp.route("/<emp_id>", methods=["PUT"])
def update_employee(emp_id):
    employee = validate_item(Employee, emp_id)

    request_data = request.get_json()

    employee.name = request_data["name"]
    employee.salary = request_data["salary"]

    db.session.commit()

    return {"msg": f"Employee {employee.id} successfully updated"}, 200

@employee_bp.route("/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    employee = validate_item(Employee, emp_id)

    db.session.delete(employee)
    db.session.commit()

    return {"msg": f"Employee {emp_id} successfully deleted"}, 200


def validate_item(model, item_id):
    try:
        item_id = int(item_id)
    except ValueError:
        return abort(make_response({"msg": f"Invalid id: {item_id}"}, 400))
    # use abort and make response here so that when validate fails, the function that called it also stops

    return model.query.get_or_404(item_id, {"msg":"id not found"})