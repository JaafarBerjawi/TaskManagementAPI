import urllib.parse


class Config:
    password = "p@ssw0rd"
    encoded_password = urllib.parse.quote(password)

    connection_string = f"postgresql://postgres:{encoded_password}@localhost:5432/task_manager"

    # Database for user-related data
    SECURITY_DB_URI = connection_string

    # Database for task management data
    TASKMANAGEMENT_DB_URI = connection_string
