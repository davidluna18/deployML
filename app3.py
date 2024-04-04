# 1. Library imports
import uvicorn
from fastapi import FastAPI
from routers import routerDiabetes

# Create the app object
app = FastAPI()

app.include_router(routerDiabetes.router)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app3:app --reload