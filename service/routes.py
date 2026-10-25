"""
Account Service

This microservice handles the lifecycle of Accounts.
"""

from flask import abort, jsonify, request
from service import app
from service.models import Account, DataValidationError
from service.common import status


######################################################################
# HEALTH ENDPOINT
######################################################################

@app.route("/health")
def health():
    """Health Status."""
    return jsonify(status="OK"), status.HTTP_200_OK


######################################################################
# GET INDEX
######################################################################

@app.route("/")
def index():
    """Root URL response."""
    return jsonify(
        name="Account REST API Service",
        version="1.0",
    ), status.HTTP_200_OK


######################################################################
# CREATE AN ACCOUNT
######################################################################

@app.route("/accounts", methods=["POST"])
def create_account():
    """Creates an Account."""
    app.logger.info("Request to create an Account")
    check_content_type("application/json")

    data = request.get_json()
    if data is None:
        abort(status.HTTP_400_BAD_REQUEST, "Request body must be JSON")

    account = Account()

    try:
        account.deserialize(data)
        account.create()
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    location_url = "/"
    return jsonify(account.serialize()), status.HTTP_201_CREATED, {
        "Location": location_url
    }


######################################################################
# LIST ALL ACCOUNTS
######################################################################

@app.route("/accounts", methods=["GET"])
def list_accounts():
    """Returns all Accounts."""
    app.logger.info("Request to list Accounts")

    accounts = Account.all()
    results = [account.serialize() for account in accounts]

    return jsonify(results), status.HTTP_200_OK


######################################################################
# READ AN ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """Reads an Account."""
    app.logger.info("Request to read Account with id: %s", account_id)

    account = Account.find(account_id)

    if account is None:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id '{account_id}' was not found.",
        )

    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# UPDATE AN EXISTING ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """Updates an Account."""
    app.logger.info("Request to update Account with id: %s", account_id)
    check_content_type("application/json")

    account = Account.find(account_id)

    if account is None:
        abort(
            status.HTTP_404_NOT_FOUND,
            f"Account with id '{account_id}' was not found.",
        )

    data = request.get_json()
    if data is None:
        abort(status.HTTP_400_BAD_REQUEST, "Request body must be JSON")

    try:
        account.deserialize(data)
        account.update()
    except DataValidationError as error:
        abort(status.HTTP_400_BAD_REQUEST, str(error))

    return jsonify(account.serialize()), status.HTTP_200_OK


######################################################################
# DELETE AN ACCOUNT
######################################################################

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_account(account_id):
    """Deletes an Account."""
    app.logger.info("Request to delete Account with id: %s", account_id)

    account = Account.find(account_id)

    if account is not None:
        account.delete()

    return "", status.HTTP_204_NO_CONTENT


######################################################################
# CONTENT TYPE VALIDATION
######################################################################

def check_content_type(content_type):
    """Checks whether the request has the expected content type."""
    if request.headers.get("Content-Type") != content_type:
        abort(
            status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            f"Content-Type must be {content_type}",
        )
