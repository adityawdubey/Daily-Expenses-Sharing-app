# Expense Management Endpoints

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import models
from app.schemas import user as user_schema, expenses as expense_schema
from app.core.database import get_db
from fastapi.responses import JSONResponse, FileResponse
import csv
import os

router = APIRouter()


@router.post("/expenses/")
def add_expense(expense: expense_schema.ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = models.Expense(
        amount=expense.amount,
        split_method=expense.split_method,
        user_id=expense.user_id
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense


@router.get("/expenses/{user_id}")
def get_user_expenses(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Expense).filter(models.Expense.user_id == user_id).all()


@router.get("/expenses/")
def get_all_expenses(db: Session = Depends(get_db)):
    return db.query(models.Expense).all()


@router.get("/balance-sheet")
def download_balance_sheet(user_id: int = None, download: bool = False, db: Session = Depends(get_db)):
    if user_id:
        user_expenses = db.query(models.Expense).filter(models.Expense.user_id == user_id).all()
        if not user_expenses:
            raise HTTPException(status_code=404, detail="No expenses found for the user")

        balance_sheet = {
            "user_id": user_id,
            "total_expenses": sum(expense.amount for expense in user_expenses),
            "expenses": user_expenses
        }
    else:
        all_expenses = db.query(models.Expense).all()
        if not all_expenses:
            raise HTTPException(status_code=404, detail="No expenses found")

        balance_sheet = {
            "total_expenses": sum(expense.amount for expense in all_expenses),
            "expenses": all_expenses
        }

    if download:
        file_path = f"balance_sheet_{'user_' + str(user_id) if user_id else 'all_users'}.csv"
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Expense ID", "Amount", "Split Method", "User ID"])
            for expense in balance_sheet["expenses"]:
                writer.writerow([expense.id, expense.amount, expense.split_method, expense.user_id])
        
        return FileResponse(file_path, filename=file_path, media_type='text/csv')
    return JSONResponse(content=balance_sheet)
