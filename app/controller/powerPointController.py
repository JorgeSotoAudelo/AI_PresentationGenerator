
import os
import json
from pptx.util import Inches,Pt
from pptx import Presentation
from app.controller.imagesController import imageController


class powerPointController:
    def __init__(self):
        self.imgController = imageController()

    def createPowerpoint(self,json_data):
        presentation = Presentation()

        data = json.loads(json_data)
        if 'slides' not in data:
            # Handle case where 'slides' key is missing
            return None

        for slide_data in data['slides']:
            slide = presentation.slides.add_slide(presentation.slide_layouts[1])

            # Set slide title
            title = slide.shapes.title
            title.text = slide_data.get('title', '')

            # Set slide text
            content_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(5))
            text_frame = content_box.text_frame
            text_frame.text = slide_data.get('text', '')

            # Configure text formatting
            text_frame.word_wrap = True
            text_frame.auto_size = True

            # Search image on Pixabay
            search_query = slide_data.get('image', '')
            image_url = self.imgController.searchImage(search_query)

            # Download image and add to slide
            if image_url:
                image_path = self.imgController.downloadImage(image_url)
                if image_path:
                    image_box = slide.shapes.add_picture(image_path, Inches(1), Inches(3), width=Inches(6), height=Inches(4))

                    # Adjust image positioning
                    image_box.left = int((presentation.slide_width - image_box.width) / 2)

                # Delete downloaded image from server
                if os.path.exists(image_path):
                    os.remove(image_path)

            # Adjust font size for longer text
            if len(text_frame.text) > 200:
                text_frame.text = slide_data.get('text', '')
                font = text_frame.paragraphs[0].runs[0].font
                font.size = Pt(16)

        return presentation