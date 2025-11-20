import hashlib

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def register(PUsername: str, PPassword: str) -> None:
    with open(CREDENTIALS_FILE, "a+") as file:
        file.seek(0)
        lines = file.readlines()
        
    new_id = len(lines)
    hashed_password = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{new_id}{DELIMITER}{PUsername}{DELIMITER}{hashed_password}\n")


def login(PUsername: str, PPassword: str) -> bool:
    hashed_input = hash_password(PPassword)

    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3:
                _, username, stored_hash = parts
                if username == PUsername and stored_hash == hashed_input:
                    return True
    return False

def viewProfile(PUsername: str) -> list[str]:
    with open(CREDENTIALS_FILE, "r") as file:
        for line in file:
            parts = line.strip().split(DELIMITER)
            if len(parts) == 3:
                user_id, username, _ = parts
                if username == PUsername:
                    return [user_id, username]
    return []
def change_password(PUsername: str, PNewPassword: str) -> None:
    with open(CREDENTIALS_FILE, "r") as file:
        lines = file.readlines()
        
    updated_lines = []
    hashed_new_password = hash_password(PNewPassword)
    
    for line in lines:
        parts = line.strip().split(DELIMITER)
        if len(parts) == 3:
            user_id, username, stored_hash = parts
            if username == PUsername:
                updated_lines.append(f"{user_id}{DELIMITER}{username}{DELIMITER}{hashed_new_password}\n")
            else:
                updated_lines.append(line)
        else:
            updated_lines.append(line)
    with open(CREDENTIALS_FILE, "w") as file:
        file.writelines(updated_lines)
