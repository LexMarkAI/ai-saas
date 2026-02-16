from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI SaaS Backend", version="1.0.0")


class EchoRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "ok", "message": "AI SaaS API running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/version")
def version():
    return {"version": "1.0.0"}


@app.post("/echo")
def echo(data: EchoRequest):
    return {
        "received": data.text,
        "length": len(data.text)
    }
from fastapi import FastAPI

app = FastAPI()
from fastapi import FastAPI
from pydantic import BaseModel
class CVInput(BaseModel):
    name: str
    years_experience: int
    employment_gaps_months: int
    previous_terminations: int


@app.post("/hr/screen")
def screen_cv(payload: CVInput):
    risk_score = 0
    flags = []

    if payload.years_experience < 2:
        risk_score += 2
        flags.append("Low experience")

    if payload.employment_gaps_months > 6:
        risk_score += 2
        flags.append("Significant employment gap")

    if payload.previous_terminations > 0:
        risk_score += 3
        flags.append("Previous termination history")

    return {
        "candidate": payload.name,
        "risk_score": risk_score,
        "risk_level": (
            "Low" if risk_score <= 2 else
            "Medium" if risk_score <= 4 else
            "High"
        ),
        "flags": flags
    }
class CVInput(BaseModel):
    name: str
    years_experience: int
    employment_gaps_months: int
    previous_terminations: int


@app.post("/hr/screen")
def screen_cv(payload: CVInput):
    risk_score = 0
    flags = []

    if payload.years_experience < 2:
        risk_score += 2
        flags.append("Low experience")

    if payload.employment_gaps_months > 6:
        risk_score += 2
        flags.append("Significant employment gap")

    if payload.previous_terminations > 0:
        risk_score += 3
        flags.append("Previous termination history")

    return {
        "candidate": payload.name,
        "risk_score": risk_score,
        "risk_level": (
            "Low" if risk_score <= 2 else
            "Medium" if risk_score <= 4 else
            "High"
        ),
        "flags": flags
    }
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone

app = FastAPI(title="ai-saas", version="0.1.0")


class EchoIn(BaseModel):
    text: str


@app.get("/")
def root():
    return {"status": "ok", "message": "FastAPI is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {
        "name": app.title,
        "version": app.version,
        "utc": datetime.now(timezone.utc).isoformat(),
    }


@app.post("/echo")
def echo(payload: EchoIn):
    # payload.text is validated automatically (must be a string)
    return {"received": payload.text, "length": len(payload.text)}

