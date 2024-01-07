from uuid import UUID, uuid4
import pytest

from todo.utils.generate_uuid import generate_uuid


def test_generate_uuid():
    generated_uuid = generate_uuid()

    # Check if the generated UUID is a valid UUID
    assert isinstance(UUID(generated_uuid), UUID)

    # Check if the generated UUID has the correct length
    assert len(generated_uuid) == 32

    # Check if the generated UUID does not contain hyphens
    assert "-" not in generated_uuid

    # Check if two consecutive calls produce different UUIDs
    new_generated_uuid = generate_uuid()
    assert generated_uuid != new_generated_uuid
