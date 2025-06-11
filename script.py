from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Modèle de données
class Location(BaseModel):
    user_id: str
    latitude: float
    longitude: float
    timestamp: datetime = datetime.utcnow()

# Stockage temporaire (à remplacer par une base de données)
locations = []

@app.post("/location/")
async def receive_location(location: Location):
    locations.append(location)
    return {"message": "Coordonnées enregistrées", "data": location}

@app.get("/locations/", response_model=List[Location])
async def get_locations():
    return locations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
