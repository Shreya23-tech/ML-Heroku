from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    school :str
    sex	: str
    age : int
    address	: str
    famsize	: str
    Pstatus	: str
    Fedu : int
    Mjob : int	
    Fjob : str	
    reason : str
    guardian : str	
    traveltime : int
    studytime : int
    failures : int	
    schoolsup : str
    famsup : str
    paid : str	
    activities	: str
    nursery	: str
    higher	: str
    internet : str	
    romantic : str	
    famrel	: int
    freetime : int		
    Walc : int
    health : int	
    absences : int	
    G1 : int
    G2	: int
    

# loading the saved model
Sperformance_model = pickle.load(open('Sperformance.sav','rb'))


@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    school= input_dictionary['school']
    sex= input_dictionary['sex']
    age= input_dictionary['age']
    address= input_dictionary['address']
    famsize= input_dictionary['famsize']
    Pstatus= input_dictionary['Pstatus']
    Fedu= input_dictionary['Fedu']
    Mjob= input_dictionary['Mjob']
    Fjob= input_dictionary['Fjob']
    reason= input_dictionary['reason']
    guardian= input_dictionary['guardian']
    traveltime= input_dictionary['traveltime']
    studytime= input_dictionary['studytime']
    failures= input_dictionary['failures']
    schoolsup= input_dictionary['schoolsup']
    famsup= input_dictionary['famsup']
    paid= input_dictionary['paid']
    activities= input_dictionary['activities']
    nursery= input_dictionary['nursery']
    higher= input_dictionary['higher']
    internet= input_dictionary['internet']
    romantic= input_dictionary['romantic']
    famrel= input_dictionary['famrel']
    freetime= input_dictionary['freetime']
    Walc= input_dictionary['Walc']
    health= input_dictionary['health']
    absences= input_dictionary['absences']
    G1= input_dictionary['G1']
    G2= input_dictionary['G2']

    input_list = [ school,sex,age,address,famsize,Pstatus,Fedu,Mjob,Fjob,reason,guardian,traveltime,
    studytime,
    failures,	
    schoolsup,
    famsup,
    paid,	
    activities,
    nursery,
    higher,
    internet,	
    romantic,	
    famrel,
    freetime,		
    Walc,
    health,	
    absences,	
    G1,
    G2,]
    
    G3= Sperformance_model.predict([input_list])
    
    return G3
