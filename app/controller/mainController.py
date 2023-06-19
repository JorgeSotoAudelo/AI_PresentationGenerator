from flask import render_template,request,make_response
from app.controller.gptController import gptController
from app.controller.powerPointController import powerPointController

def index(): 
     return render_template('index.html')


def downloadPresentation():
    inputText = request.args.get('inputText')
    gptControl = gptController()
    presentationController = powerPointController()
    json_data = gptControl.chatGPTrequest(inputText)
    presentation = presentationController.createPowerpoint(json_data)
    presentation_path = 'app/temp/output.pptx'
    presentation.save(presentation_path)

    # Prepare the file to be downloaded
    with open(presentation_path, 'rb') as file:
        data = file.read()

    response = make_response(data)
    response.headers['Content-Disposition'] = 'attachment; filename=output.pptx'
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'

    return response


