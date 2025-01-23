from pydantic import BaseModel


class ORMSchema(BaseModel):

    class Config:
        from_attributes = True
