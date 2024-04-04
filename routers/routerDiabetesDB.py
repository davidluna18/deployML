import pickle
from fastapi import APIRouter, Depends
from schemas import schemas
import numpy as np
from database.database import SessionLocal, get_db
from sqlalchemy import func
from models import models
from models.models import pacientes

router = APIRouter()

pkl_filename = "RandomForestDiabetes.pkl"
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Sano','Diabetes']  

@router.post('/predict')
def predict_diabetes(data:schemas.paciente, db: SessionLocal = Depends(get_db)): # type: ignore
    
    #data = data.dict()
    data = data.model_dump()
    
    idpaciente=data['idpaciente']
   
    paciente = db.query(models.pacientes).filter(
                                    pacientes.idpacientes==idpaciente,
                                ).first()

    print(paciente.nombre)
    xin = np.array([paciente.pregnancies,
                    paciente.glucose,
                    paciente.bloodpressure,
                    paciente.skinthickness,
                    paciente.insulin,
                    paciente.BMI,
                    paciente.diabetespedigreefunction,
                    paciente.age]).reshape(1,8)

    prediction = model.predict(xin)
    yout = labels[prediction[0]]
    
    return {
        'name': paciente.nombre,
        'prediction': yout
    }