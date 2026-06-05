from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json
from urllib.parse import urlparse
from urllib.parse import parse_qs

import rest_crud as rc

PATH = '/employees'

class EmployeeAPI(BaseHTTPRequestHandler):
    """
        API request handler
    """
    def send_json(self, data, status=200):
        self.send_response(status)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(data).encode()
        )

    # GET Request
    def do_GET(self):
        parsed = urlparse(self.path)

        if parsed.path != PATH:
            self.send_json({'error': "Invalid Endpoint"}, 400)
            return

        params = parse_qs(parsed.query)  

        if 'id' in params:
            emp_id = int(params["id"][0])
            result = rc.get_employee_by_id(emp_id=emp_id)
        else:
            result = rc.get_all_employees()

        self.send_json(result)

    # POST request
    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))

            if length == 0:
                self.send_json({"error": "Empty request body"}, 400)
                return

            body = self.rfile.read(length)
            employee = json.loads(body)

            result = rc.add_employee(employee)
            self.send_json(result, 201)  

        except json.JSONDecodeError:
            self.send_json({"error": "Invalid JSON"}, 400)

        except KeyError as e:
            self.send_json({"error": f"Missing field: {e}"}, 400)

        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    # PUT request
    def do_PUT(self):
        try:
            parsed = urlparse(self.path)

            if parsed.path != PATH:
                self.send_json({"error": "Invalid endpoint"}, 400)
                return

            params = parse_qs(parsed.query)

            if 'id' not in params:
                self.send_json({"error": "Missing employee id"}, 400)
                return

            emp_id = int(params["id"][0])

            length = int(self.headers.get("Content-Length", 0))

            if length == 0:
                self.send_json({"error": "Empty request body"}, 400)
                return

            body = self.rfile.read(length)
            employee = json.loads(body)

            result = rc.update_employee(emp_id=emp_id, data=employee)

            if not result:
                self.send_json({"error": "Employee not found"}, 404)
                return

            self.send_json(result)

        except json.JSONDecodeError:
            self.send_json({"error": "Invalid JSON"}, 400)

        except KeyError as e:
            self.send_json({"error": f"Missing field: {e}"}, 400)

        except Exception as e:
            self.send_json({"error": str(e)}, 500)

    # DELETE request
    def do_DELETE(self):
        try:
            parsed = urlparse(self.path)

            if parsed.path != PATH:
                self.send_json({"error": "Invalid endpoint"}, 400)
                return

            params = parse_qs(parsed.query)

            if 'id' not in params:
                self.send_json({"error": "Missing employee id"}, 400)
                return

            emp_id = int(params["id"][0])

            result = rc.delete_employee(emp_id=emp_id)

            if not result:
                self.send_json({"error": "Employee not found"}, 404)
                return

            self.send_json({"message": f"Employee {emp_id} deleted successfully"})

        except ValueError:
            self.send_json({"error": "Invalid employee id"}, 400)

        except Exception as e:
            self.send_json({"error": str(e)}, 500)   


# starting the http server
server = HTTPServer(
    ("localhost", 8090),
    EmployeeAPI
)

print("Server is running on port 8090")

server.serve_forever()
