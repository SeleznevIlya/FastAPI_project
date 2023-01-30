from pydantic import BaseModel


class BaseUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone: str
    is_active: bool


class UserList(BaseUser):
    id: int


class UserCreate(BaseUser):
    pass


class UserUpdate(BaseUser):
    pass