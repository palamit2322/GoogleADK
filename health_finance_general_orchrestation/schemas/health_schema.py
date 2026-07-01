from enum import Enum as PyEnum
from typing import List, Optional

from pydantic import BaseModel, Field


class ConsultantTypeEnum(str, PyEnum):
    PSYCHOLOGIST = "psychologist"
    PSYCHIATRIST = "psychiatrist"
    THERAPIST = "therapist"
    NUTRITIONIST = "nutritionist"
    PERSONAL_TRAINER = "personal_trainer"
    LIFE_COACH = "life_coach"
    GENERAL_HELPER = "general_helper"


class ProblemAnalysis(BaseModel):
    consultant_type: ConsultantTypeEnum
    identified_issues_summary: str = Field(
        description="A brief summary of the core issues identified from the user's query."
    )


class ConsultationResp(BaseModel):
    consultant_type: ConsultantTypeEnum
    identified_issues_summary: str
    suitability_explanation: str
    key_questions_to_consider: List[str]
    initial_actionable_steps: List[str]
    disclaimer: str

