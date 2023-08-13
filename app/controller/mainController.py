from flask import render_template,request,make_response
from app.controller.gptController import gptController
from app.controller.powerPointController import powerPointController

def index(): 
     return render_template('index.html')


def downloadPresentation():
    try:
        inputText = request.args.get('inputText')
        slideNumber = request.args.get('slideCount')
        language = request.args.get('language')
        apiKey = request.args.get('apiKey')
        print(apiKey)
        presentationPath = 'app/temp/output.pptx'

        json_data = getJSON(inputText,slideNumber,language,apiKey)
        makePresentation(json_data,presentationPath)

        # Prepare the file to be downloaded
        with open(presentationPath, 'rb') as file:
            data = file.read()

        response = make_response(data)
        response.headers['Content-Disposition'] = 'attachment; filename=output.pptx'
        response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'

        return response
    except Exception as e:
        print(str(e))
        return render_template('error.html')

def getJSON(inputText,slideNumber,language,apiKey):
    gptControl = gptController(apiKey)
    json_data = gptControl.chatGPTrequest(inputText,slideNumber,language)
    return findJSON(json_data)

def makePresentation(json_data, presentationPath):
    presentationController = powerPointController()
    presentation = presentationController.createPowerpoint(json_data)
    presentation.save(presentationPath)

def findJSON(text):
    indexJSON = text.find('{')
    return text[indexJSON:]