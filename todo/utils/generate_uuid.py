from uuid import uuid4


def generate_uuid() -> str:
    unique_uuid: str = str(uuid4())
    unique_uuid = unique_uuid.replace("-", "")
    return unique_uuid
