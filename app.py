from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ITF Women Betting Predictor")

class PredictRequest(BaseModel):
    player_A: str
    player_B: str
    odds_A: float | None = None

@app.post("/predict")
def predict(req: PredictRequest):
    # prosta symulacja — tylko przykład
    prob = 0.55  # zawsze zwraca 55% dla zawodniczki A
    suggested_fraction = 0.25  # zawsze 25% banku (dla demo)
    return {
        "prob_A": prob,
        "odds_A": req.odds_A,
        "suggested_fraction_of_bankroll": suggested_fraction,
        "message": f"Zawodniczka {req.player_A} ma {prob*100:.0f}% szansy."
    }
