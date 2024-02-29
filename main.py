from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "AI API"
app.description = "AI Endpoints for BardAI, PalmAI and OpenAI. Python/FastAPI.  Developer: edisonsanchez.com (a.k.a. MrDonMomo)"
app.version = "0.0.1"
app.terms_of_service = "https://edisonsanchez.com/terms"
app.contact = {
    "name": "Edison Sanchez",
    "url": "https://edisonsanchez.com",
    "email": "info@edisonsanchez.com",
}
app.license_info = {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
}


laws = [
    {
        "id": 1,
        "title": "Codigo Civil",
        "description": "Codigo Civil Dominicano",
        "category": 0,
    }
]


@app.get("/health", tags=["Base"])
def message():
    return HTMLResponse("<h1>Health Check Passed!</h1")


@app.get("/laws", tags=["Laws"])
def get_laws():
    return laws
