# Todo-list

        #HOW TO LAUNCH LOCALLY

ENDPOINTS:
url: '/api/v1/tasks'
method: 'GET'
filters:
'is_completed=true'
'is_completed=false'

JSON REQUEST EXAMPLE
{
    "title": "title",
    "description": "description"
}

JSON ANSWER EXAMPLE
{
    "id": 0,
    "time": "d.m.y H:M:S",
    "status": "Not completed",
    "title": "title",
    "description": "description"
}

JSON DELETE REQUEST EXAMPLE
url: api/v1/tasks/{id}
method: DELETE

JSON DELETE ANSWER EXAMPLE
{
    "message": "deleted successfully"
}

ERROR CODES:
400 - wrong format
404 - data not found
422 - unavailable option
500 - internal server error
