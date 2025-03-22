from humps import camelize
from pydantic import BaseModel


class BaseSchema(BaseModel):
    model_config = {
        "from_attributes": True,
        "populate_by_name": True,
        "alias_generator": camelize,
        "str_strip_whitespace": True,
    }
