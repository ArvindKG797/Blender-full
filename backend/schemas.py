from pydantic import BaseModel
from typing import List, Optional

class ChatInput(BaseModel):
    conversation_id: Optional[str] = None
    prompt: str
    model_name: str

class MessageResponse(BaseModel):
    role: str
    content: str
    class Config:
        from_attributes = True

class ConversationResponse(BaseModel):
    id: str
    title: str
    messages: List[MessageResponse] = []
    class Config:
        from_attributes = True