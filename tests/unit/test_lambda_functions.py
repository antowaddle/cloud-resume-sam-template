import sys
import os
import pytest
from unittest.mock import patch, MagicMock
from botocore.exceptions import ClientError
from decimal import Decimal

# Adjust the paths to import the lambda functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../get-function')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../put-function')))

from app import lambda_handler as lambda_handler_get
from app import lambda_handler as lambda_handler_put

@pytest.fixture
def dynamodb_mock():
    with patch('app.boto3.resource') as mock:
        yield mock

def test_lambda_handler_get_success(dynamodb_mock):
    table_mock = dynamodb_mock().Table()
    table_mock.get_item.return_value = {
        'Item': {
            'ID': 'visitors',
            'visitors': Decimal(5)
        }
    }

    event = {}
    context = {}

    response = lambda_handler_get(event, context)
    
    assert response['statusCode'] == 200
    assert response['body'] == '{"count": 5}'

def test_lambda_handler_get_not_found(dynamodb_mock):
    table_mock = dynamodb_mock().Table()
    table_mock.get_item.return_value = {}

    event = {}
    context = {}

    response = lambda_handler_get(event, context)
    
    assert response['statusCode'] == 500
    assert "The item with ID 'visitors' does not exist in the table." in response['body']

if __name__ == "__main__":
    pytest.main()
