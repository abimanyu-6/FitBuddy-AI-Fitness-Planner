from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.post("/get_diet")
async def get_diet(request: Request, age: int = Form(...), weight: float = Form(...), height: float = Form(...), goal: str = Form(...)):
    # Simple diet plan - AI key illaama kooda work aagum da
    if goal == "Weight Loss":
        diet_text = f"Age {age}, Weight {weight} ku - Morning: Oats, Afternoon: Brown Rice + Chicken, Night: Soup"
    else:
        diet_text = f"Age {age}, Weight {weight} ku - Morning: Eggs + Milk, Afternoon: Rice + Fish, Night: Chicken + Veggies"
    
    return templates.TemplateResponse(request, "result.html", {"goal": goal, "diet": diet_text})