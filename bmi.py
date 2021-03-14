# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 21:48:40 2021

@author: karthick
"""

import json

#read json
def loadJson(file):
    with open(jsonFile) as jf:
        jsonData = json.load(jf)
    return jsonData


#convert Centimeters to Meters
def convertCMtoM(val):
    val_m = float(val/100.0)
    return val_m
    

#Check Category
def checkBmiCategory(data):
    
    if data <= 18.4:
        bmi_category = "Under Weight"
    elif 18.5 <= data <= 24.9:
        bmi_category = "Normal Weight"
    elif 25 <= data <= 29.9:
        bmi_category = "Over Weight"
    elif 30 <= data <= 34.9:
        bmi_category = "Moderately Obese"
    elif 35 <= data <= 39.9:
        bmi_category = "Severely Obese"
    elif data >= 40: 
        bmi_category = "Very Severely Obese"
    
    return bmi_category

#Check Health Risk
def checkHealthRisk(data):
    
    if data <= 18.4:
        health_risk = "Malnutrition Risk"
    elif 18.5 <= data <= 24.9:
        health_risk = "Low Risk"
    elif 25 <= data <= 29.9:
        health_risk = "Enhanced Risk"
    elif 30 <= data <= 34.9:
        health_risk = "Medium Risk"
    elif 35 <= data <= 39.9:
        health_risk = "High Risk"
    elif data >= 40: 
        health_risk = "Very High Risk"
    
    return health_risk


#Main Function / Calculate BMI
def calculateBMI(data):
    
    #BMI(kg/m ) = mass(kg) / height(m)
    
    height = convertCMtoM(data["HeightCm"])
    bmi = round(data["WeightKg"]/height, 2)
    i["BmiKg/M2"] = bmi
    i["BmiCategory"] = checkBmiCategory(bmi)
    i["HealthRisk"] = checkHealthRisk(bmi)
    
    return data


if __name__ == "__main__":
    
    #load json data
    jsonFile = "bmi.json"
    bmi_data = loadJson(jsonFile)
    
    bmi = []
    #calculate BMI
    for i in bmi_data:
        bmi.append(calculateBMI(i))
        
    #Count Over weight
    over_weight_category = ["Over Weight", "Severely Obese", "Very Severely Obese"]
    
    #export JSON
    with open ("BMI-Results.json", "w") as writeJson:
        json.dump(bmi, writeJson, indent=4)
    
    overweight = [i for i in bmi if i['BmiCategory'] in over_weight_category]
    
    count_overweight = len(overweight)
    
    print("Total number of overweight people is %s"%(count_overweight))
    
    
    
    
    
    
    
