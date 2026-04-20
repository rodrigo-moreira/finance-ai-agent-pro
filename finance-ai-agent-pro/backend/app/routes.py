from fastapi import APIRouter
from app.schemas import UserInput
from app.services.financial_service import FinancialService

router = APIRouter()
service = FinancialService()

@router.post("/analyze")
def analyze(data: UserInput):
    return service.process(data)
