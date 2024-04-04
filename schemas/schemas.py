from pydantic import BaseModel

class schemaDiabetes(BaseModel):
    Pregnancies: float 
    Glucose: float 	
    BloodPressure: float 	
    SkinThickness: float 	
    Insulin: float 	
    BMI: float 
    DiabetesPedigreeFunction: float 	
    Age: float 

class paciente(BaseModel):
    idpaciente: int 
