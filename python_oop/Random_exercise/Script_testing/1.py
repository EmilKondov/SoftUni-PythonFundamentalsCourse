import requests
import random
import string
import json

# Replace these with your Grafana instance details
GRAFANA_URL = 'http://your-grafana-instance.com'
API_TOKEN = 'your_grafana_api_token'

# Headers for authentication
headers = {
    'Authorization': f'Bearer {API_TOKEN}',
    'Content-Type': 'application/json'
}


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))


def create_team(team_name):
    url = f'{GRAFANA_URL}/api/teams'
    payload = {"name": team_name}
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    return response.json()


def create_user(username, email):
    url = f'{GRAFANA_URL}/api/admin/users'
    password = generate_random_password()
    payload = {
        "name": username,
        "email": email,
        "login": username,
        "password": password
    }
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    return response.json(), password


def add_user_to_team(user_id, team_id):
    url = f'{GRAFANA_URL}/api/teams/{team_id}/members'
    payload = {"userId": user_id}
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    return response.json()


def create_dashboard_folder(folder_name):
    url = f'{GRAFANA_URL}/api/folders'
    payload = {"title": folder_name, "uid":
        ''.join(random.choice(string.ascii_letters) for i in range(10))}
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    return response.json()


def update_folder_permissions(folder_uid, team_id):
    url = f'{GRAFANA_URL}/api/folders/{folder_uid}/permissions'
    payload = [{"role": "Viewer", "permission": 1, "teamId": team_id}]
    response = requests.post(url, headers=headers,
                             data=json.dumps(payload))
    return response.json()


def create_dashboard_from_template(folder_uid, dashboard_title,
                                   template_file):
    url = f'{GRAFANA_URL}/api/dashboards/db'
    with open(template_file) as f:
        template_json = json.load(f)
    template_json['dashboard']['title'] = dashboard_title
    template_json['folderId'] = folder_uid
    response = requests.post(url, headers=headers,
                             data=json.dumps(template_json))
    return response.json()

    # Example usage


client_name = 'ClientXYZ'
users_info = [
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"}
    ]

#Example usage
client_name = 'ClientXYZ'
users_info = [
    {"username": "user1", "email": "user1@example.com"},
    {"username": "user2", "email": "user2@example.com"}
]

# Step 1: Create a Team
team_response = create_team(client_name)
team_id = team_response.get('teamId')

# Step 2 & 3: Create Users and Add them to the Team
for user_info in users_info:
    user_response, password = create_user(user_info['username'],
                                          user_info['email'])
    user_id = user_response.get('id')
    add_user_to_team(user_id, team_id)
    print(f"Created user {user_info['username']} with password {password}")

# Step 4: Create a Dashboard Folder
folder_response = create_dashboard_folder(f'{client_name}_Dashboards')
folder_uid = folder_response.get('uid')

# Step 5: Edit Folder Permissions
update_folder_permissions(folder_uid, team_id)

# Step 6: Create a Dashboard from a Template
dashboard_template_file = 'path/to/dashboard_template.json'  # Adjust the
path
to
your
template
file
create_dashboard_from_template(folder_uid, f'{client_name}_Dashboard',
                               dashboard_template_file)

print("Client onboarding process completed successfully.")