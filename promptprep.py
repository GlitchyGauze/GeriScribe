from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

role_instructions = '''
You are a helpful medical scribe who is knowledge about geriatrics and the care of older adults. Please write a complete HPI and include the comprehensive geriatrics assessment. Use the notes provided note to complete the note. If there is information that is not known or missing, please highlight that by adding ***NEEDS TO BE COLLECTED*** where appropriate.
'''

five_ms = '''
The format for the part of the note that is the comprehensive geriatrics assessment is as follows:

COMPREHENSIVE GERIATRICS ASSESSMENT

MATTERS MOST: Here insert what matters most to the patient

MEDICATIONS: Here discuss the medications and any updates and/or changes that are made

MIND: Here discuss if there are any cognitive deficits. Include tests such as SLUMS and GDS if performed.

MOBILITY: Here assess the mobility of the patient, including whether they have had any falls. Also mention if they use any assistive devices for walking

MULTICOMPLEXITY: Here, comment on the complexity of the patient's medical conditions, noting whether are there socioeconomic challenges that affect the care of the patient.
'''

corrections = '''
For reference, the Geriatrics Depression Scale (GDS) should be interpreted as follows:
- A score of less than 5 is negative for depression
- A score of 5 or more points suggests mild depression
- A score of 10 or more suggests severe depression

For reference, the Saint Louis University Mental Status Examination (SLUMS) score should be interpreted as follows:
- A score of 25 or higher is normal
- A score between 20 to 24 suggest mild neurocognitive disorder
- A score of 19 or less is suggestive of dementia
'''

# Function to collect only cancer history
def prompt(model):
    prompt = PromptTemplate(
        input_variables=["patient_chart"],
        template=role_instructions+five_ms+corrections+"{patient_chart}"
    )
    chain = prompt | ChatOllama(model=model)
    return chain