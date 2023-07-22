from typing import Any, Dict, Optional, Union

from pydantic import BaseModel


class EsDocument(BaseModel):
    index: str
    id: Optional[str] = None
    document: Union[str, Dict[str, Any]]
