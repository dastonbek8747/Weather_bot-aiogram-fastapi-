from fastapi import FastAPI
from get_weather import get_date_day, get_date_week
import uvicorn
from pydantic import BaseModel

app = FastAPI()


class City_model(BaseModel):
    name: str


@app.post("/day/")
async def get_date_day_weather(date: City_model):
    return await get_date_day(date.name)


@app.post("/week/")
async def get_week_date_weather(date: City_model):
    return await get_date_week(date.name)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
