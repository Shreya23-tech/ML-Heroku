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


@app.post('/sperformance')
def stud_performance(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    school_= input_dictionary['school']
    sex_= input_dictionary['sex']
    age_= input_dictionary['age']
    address_= input_dictionary['address']
    famsize_= input_dictionary['famsize']
    Pstatus_= input_dictionary['Pstatus']
    Fedu_= input_dictionary['Fedu']
    Mjob_= input_dictionary['Mjob']
    Fjob_= input_dictionary['Fjob']
    reason_= input_dictionary['reason']
    guardian_= input_dictionary['guardian']
    traveltime_= input_dictionary['traveltime']
    studytime_= input_dictionary['studytime']
    failures_= input_dictionary['failures']
    schoolsup_= input_dictionary['schoolsup']
    famsup_= input_dictionary['famsup']
    paid_= input_dictionary['paid']
    activities_= input_dictionary['activities']
    nursery_= input_dictionary['nursery']
    higher_= input_dictionary['higher']
    internet_= input_dictionary['internet']
    romantic_= input_dictionary['romantic']
    famrel_= input_dictionary['famrel']
    freetime_= input_dictionary['freetime']
    Walc_= input_dictionary['Walc']
    health_= input_dictionary['health']
    absences_= input_dictionary['absences']
    G1_= input_dictionary['G1']
    G2_= input_dictionary['G2']

    input_list = [ school_,sex_,age_,address_,famsize_,Pstatus_,Fedu_,Mjob_,Fjob_,reason_,guardian_,traveltime_,studytime_,failures_,	schoolsup_,famsup_,paid_,	activities_,nursery_,higher_,internet_,	romantic_,	famrel_,freetime_,		Walc_,health_,	absences_,	G1_,G2_]
    
    
    prediction= Sperformance_model.predict([input_list])
    
    return prediction[0]
