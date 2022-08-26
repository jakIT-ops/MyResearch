from django.db import models
from django.utils.timezone import now 
from datetime import datetime

# Azure imports
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from msrest.authentication import CognitiveServicesCredentials
import time

# Create your models here.

class Key_Endpoint(models.Model):
    endpoint = models.URLField(max_length=100,null=True)
    key = models.CharField(max_length=100,null=True)
    def set_endpoint(self, e):
        self.endpoint = e
    def set_key(self, k):
        self.key = k

class OCR(models.Model):
    def set_url(self, url):
        self.image_url = url

    image_url = models.URLField(max_length=500,null=True)

    def ocr(self, k_e = Key_Endpoint):
        computervision_client = ComputerVisionClient(k_e.endpoint,\
                         CognitiveServicesCredentials(k_e.key))
        read_image_url = self.image_url
        try:
            read_response = computervision_client.read(read_image_url,  raw=True)
            read_operation_location = read_response.headers["Operation-Location"]
            operation_id = read_operation_location.split("/")[-1]

            # Call the "GET" API and wait for it to retrieve the results
            while True:
                read_result = computervision_client.get_read_result(operation_id)
                if read_result.status not in ['notStarted', 'running']:
                    break
                time.sleep(1)

            # Print the detected text, line by line
            if read_result.status == OperationStatusCodes.succeeded:
                d = ""
                for text_result in read_result.analyze_result.read_results:
                    for line in text_result.lines:
                        d += line.text + "\n"
                return {"result":"Results","detail":d}
                
            return {"result":"Error","detail":""}
        except:
            return {"result":"Invalid Endpoint or Key.","detail":""}

class ImageAnalysis2(models.Model):
    image_url = models.URLField(max_length=500,null=True)
    process = models.URLField(max_length=100,null=True)

    def set_url(self, url):
        self.image_url = url

    def set_process(self, options):
        print(options, flush=True)
        self.process = options

    def analyse(self, k_e = Key_Endpoint):
        computervision_client = ComputerVisionClient(k_e.endpoint,\
                         CognitiveServicesCredentials(k_e.key))
        read_image_url = self.image_url
        try:
            # GET
            results = []
            # Description
            if  "DESCRIPTION" in self.process:
                description_results = computervision_client.describe_image(read_image_url)
                intro = "Description of the image"
                info = []
                conf = []
                if (len(description_results.captions) == 0):
                    info.append("No description detected.")
                else:
                    for caption in description_results.captions:
                        info.append((caption.text + " \n").capitalize())
                        conf.append(str(int(caption.confidence * 100)) + "%")
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info)   
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})
            
            # Category
            if "CATEGORY" in self.process:
                remote_image_features = ["categories"]
                categorize_results_remote = computervision_client.analyze_image(read_image_url , remote_image_features)

                intro = "Categories from the image"
                info = []
                conf = []
                if (len(categorize_results_remote.categories) == 0):
                    info.append("No categories detected.")
                else:
                    for category in categorize_results_remote.categories:
                        info.append(category.name.capitalize())
                        conf.append(str(int(category.score * 100)) +"%")
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info)   
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})
                

            # Tag
            if "TAG" in self.process:
                tags_result_remote = computervision_client.tag_image(read_image_url)
                intro = "Tags in the image"
                info = []
                conf = []
                if (len(tags_result_remote.tags) == 0):
                    info.append("No tags detected.")
                else:
                    for tag in tags_result_remote.tags:
                        info.append(tag.name.capitalize())
                        conf.append(str(int(tag.confidence * 100)) +"%")
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info)   
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})
            
            # DETECT
            # Object
            if "OBJECT" in self.process:
                detect_objects_results_remote = computervision_client.detect_objects(read_image_url)
                intro = "Detecting objects in the image"
                info = []
                conf = []

                if len(detect_objects_results_remote.objects) == 0:
                    info.append("No objects detected.")
                else:
                    for object in detect_objects_results_remote.objects:
                        print(info,flush=True)
                        info.append(("object at location: "+ str(object.rectangle.x) +", "+ str(object.rectangle.x + object.rectangle.w) +", "+\
                            str(object.rectangle.y) +", and "+ str(object.rectangle.y + object.rectangle.h)).capitalize())
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info)
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            # Brands
            if "BRAND" in self.process:
                remote_image_features = ["brands"]
                detect_brands_results_remote = computervision_client.analyze_image(read_image_url, remote_image_features)
                intro = "Detecting brands in the image"
                info = []
                conf = []

                if len(detect_brands_results_remote.brands) == 0:
                    info.append("No brands detected.")
                else:
                    for brand in detect_brands_results_remote.brands:
                        conf.append(str(int(brand.confidence * 100))+"%")

                        info.append((brand.name+ " brand detected at location: "+\
                        str(brand.rectangle.x) + ", " + str(brand.rectangle.x + brand.rectangle.w) +
                        ", "+ str(brand.rectangle.y) +",and "+ str(brand.rectangle.y + brand.rectangle.h)).capitalize())
                        
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info)   
                        
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            # Faces
            if "FACES" in self.process:
                remote_image_features = ["faces"]
                detect_faces_results_remote = computervision_client.analyze_image(read_image_url, remote_image_features)
                intro = "Faces in the remote image:  \n"
                info = []
                conf = []
                if (len(detect_faces_results_remote.faces) == 0):
                    info.append("No faces detected.")
                else:
                    for face in detect_faces_results_remote.faces:
                        info.append((str(face.gender) + " of age " + str(face.age) + " at location: "+ str(face.face_rectangle.left) +", "+\
                            str(face.face_rectangle.top) +", "+ str(face.face_rectangle.left + face.face_rectangle.width)+", and "+\
                            str(face.face_rectangle.top + face.face_rectangle.height)).capitalize())
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            # Adult
            if "ADULT" in self.process:
                remote_image_features = ["adult"]
                detect_adult_results_remote = computervision_client.analyze_image(read_image_url, remote_image_features)
                intro = "Analyzing remote image for adult or racy content ..."
                info = []
                conf = []
                info.append("Is adult content: "+ str(detect_adult_results_remote.adult.is_adult_content))
                conf.append(str(int(detect_adult_results_remote.adult.adult_score * 100)) + "%")
                info.append("Has racy content: "+ str(detect_adult_results_remote.adult.is_racy_content))
                conf.append(str(int(detect_adult_results_remote.adult.racy_score * 100))  + "%")
                info.append("Has gory content: "+ str(detect_adult_results_remote.adult.is_gory_content))
                conf.append(str(int(detect_adult_results_remote.adult.gore_score * 100))  + "%")

                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})
            
            # Color scheme in the image
            if "COLOR" in self.process:
                remote_image_features = ["color"]
                detect_color_results_remote = computervision_client.analyze_image(read_image_url, remote_image_features)

                intro = "Getting color scheme of the remote image"
                info = []
                conf = []
                info.append("Is black and white: " + str(detect_color_results_remote.color.is_bw_img))
                info.append("Accent color: "+ str(detect_color_results_remote.color.accent_color))
                info.append("Dominant background color: "+ str(detect_color_results_remote.color.dominant_color_background))
                info.append("Dominant foreground color: " + str(detect_color_results_remote.color.dominant_color_foreground))
                info.append("Dominant colors: " + str(detect_color_results_remote.color.dominant_colors))
                
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})
            
            # Celebrities
            if "CELEBRITIES" in self.process:
                detect_domain_results_celebs_remote = computervision_client.analyze_image_by_domain("celebrities", read_image_url)
                intro = "Celebrities in the remote image"
                info = []
                conf = []
                if len(detect_domain_results_celebs_remote.result["celebrities"]) == 0:
                    info.append("No celebrities detected.")
                else:
                    for celeb in detect_domain_results_celebs_remote.result["celebrities"]:
                        info.append(celeb["name"] + " ")

                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            # Landmarks
            if "LANDMARK" in self.process:
                detect_domain_results_landmarks = computervision_client.analyze_image_by_domain("landmarks", read_image_url)

                intro = "Landmarks in the remote image"
                info = []
                conf = []
                if len(detect_domain_results_landmarks.result["landmarks"]) == 0:
                    info.append("No landmarks detected.")
                else:
                    for landmark in detect_domain_results_landmarks.result["landmarks"]:
                        info.append(landmark["name"] + " ")
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            # Image type
            if "TYPE" in self.process:
                remote_image_features = [VisualFeatureTypes.image_type]
                detect_type_results_remote = computervision_client.analyze_image(read_image_url, remote_image_features)
                intro = "Type of remote image"
                info = []
                conf = []
                if detect_type_results_remote.image_type.clip_art_type == 0:
                    info.append("Image is not clip art.")
                elif detect_type_results_remote.image_type.line_drawing_type == 1:
                    info.append("Image is ambiguously clip art.")
                elif detect_type_results_remote.image_type.line_drawing_type == 2:
                    info.append("Image is normal clip art.")
                else:
                    info.append("Image is good clip art.")

                if detect_type_results_remote.image_type.line_drawing_type == 0:
                    info.append("Image is not a line drawing.")
                else:
                    info.append("Image is a line drawing.")
                
                conf2 = conf
                if len(conf) == 0:
                    conf2 = [""]*len(info) 
                results.append({"intro":intro, "result": zip(info, conf2), "confidence": conf})

            return results
        except:
            return [{"intro":"Invalid Endpoint or Key.","result": zip([], []),"confidence": []}]