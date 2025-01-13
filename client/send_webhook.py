import requests

# URL del webhook receptor
webhook_url = "http://localhost:3000/webhook"

# Datos del nuevo usuario
data = {
    "id": 123,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "registered_at": "2025-01-12T10:00:00Z"
}

# Envío de la solicitud POST
response = requests.post(webhook_url, json=data)

# Comprobación de la respuesta
if response.status_code == 200:
    print("Webhook enviado con éxito")
else:
    print("Error al enviar el webhook:", response.text)
