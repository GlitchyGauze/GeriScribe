import os
import pandas as pd

def read_notes_to_array(ehr):
    notes = []
    for filename in os.listdir(ehr):
        note_path = os.path.join(ehr,filename)

        if os.path.isfile(note_path) and filename.endswith(".txt"):
            with open(note_path, 'r') as note:
                notes.append(note.read())

    return notes

# Function to pull template from file
# FIXME: will need to update AI comparator because this function is moved to promptprep

# Function to save LLM output to appropriate file
# FIXME: changing the model to OllamaLLM will break the AI comparator, will need to fix notebook on main branch
def save_note_to_file(note, model, patient_id):
    with open("geriscribe/outputs/"+model+"-patient-"+str(patient_id)+".txt", "w") as f:
            f.write(str(note).replace("\\n", "\n"))
