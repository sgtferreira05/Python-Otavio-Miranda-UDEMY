# The module "requests" to request HTTP resources in Python
# HTTP is a protocol used to transfer data over the internet. It works as a request-response protocol between a client and a server, where the client(your browser, for example) sends a request to the server(sites, for instance) and the server responds with the requested data.
# The client requests messages must to include data such as:
# - The HTTP method (GET, POST, PUT, DELETE, etc.)
#   - Readings(safe) - GET, HEAD, OPTIONS
#   - Writing(unsafe) - POST, PUT, PATCH, DELETE
# - The URL of the resource being requested (/users/)
# - Headers (metadata about the request, such as content type, user agent, Authorization, etc.)
# - Body (optional data sent with the request, used in POST and PUT requests)

# The server responds messages must to include data such as:
# - The HTTP status code (indicating the success or failure of the request - 200, 404, 500, etc.)
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Reference/Status
# - Headers (metadata about the response, such as content type, length, etc.)
# - Body (the actual data being returned, such as HTML, JSON, etc.)
