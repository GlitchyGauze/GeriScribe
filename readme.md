# 2025 Annual Scientific Meeting of the American Geriatrics Society

Welcome attendees! I hope you were able to walk up and meet with us, and we were able to answer any questions you may have had. Below, please find an explanation on this poster and its findings.

## Copy of the Poster Presentation
If you are here for the poster, you can [click here](/AGS%202025%20Conference%20VirtualScribe.pdf) and you can view and download a copy for your reference.

## How to Use this Code

The main code resides in the [GeriScribe Jupyter Notebook](/geriscribe.ipynb), with supporting code that can be found in [EHR Tools](/ehrtools.py) and [Prompt Prep](/promptprep.py).

In short, the logic is as follows:

- geriscribe.ipynb: the main notebook to run and test code and change LLMs
  - ehrtools.py: code to read and write data (i.e., get patient notes and save AI-generated notes)
  - promptprep.py: code for prompting the model used, **includes prompt templates**

At its current state, you can place text files into the [geriscribe/inputs](geriscribe/inputs) folder and run the geriscribe notebook. You can change which model is used in the notebook. The output will be found in the [geriscribe/outputs](geriscribe/outputs) folder, and named by the filename and the model used.

## What is all this other code?

The rest of the code is from Microsoft's Gen AI stack that is used for development of AI software. You can read more about it [here](https://github.com/docker/genai-stack).

The goal with this code is to replace the geriscribe notebook with other tools. For instance, update the number of modalities from which to accept input for note generation, such as pdfbot allowing for knoweldge graph generation of PDF files. The current code in the geriscribe notebook can be retooled into the bot.py to have a ChatGPT-like interface where you write your scratchpad notes and getting the same comprehensive geriatrics note as output.

## How to Contact

For questions, you can reach the first author at the poster, or email at sandhua1@uthscsa.edu
