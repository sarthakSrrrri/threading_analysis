from fastapi import FastAPI
from service.sequential import run_sequential

app = FastAPI(title = "Threading vs Sequental")

@app.get("/sequential")
def sequential_point():
    return run_sequential()


