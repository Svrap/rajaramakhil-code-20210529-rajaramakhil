import pandas as pd

file = 'dataset.json' #please change the json file here
json_df = pd.read_json(file)

#calculates the BMI for given weigth and height
def cal_BMI(weight,height):
    BMI = weight / (height/100)**2
    return BMI

#returns the BMI_cat and health risk
def bmiCat(BMI):
    # print(BMI)
    if BMI < 18.4: 
        return "under weight","malnutrition risk"
    elif BMI < 24.9:
        return "Normal Weight","Low risk"
    elif 25 < BMI < 29.9:
        return "Over weight","Enhanced risk"
    elif 30 < BMI < 34.9:
        return "Moderately obese","Medium risk"
    elif 35 < BMI < 39.9:
        return "Severely obese","High risk"
    elif BMI > 40:
        return "Very Severely obese","Very High risk"


BMI = cal_BMI(json_df.WeightKg.values,json_df.HeightCm.values)
bmicatogery = []
healthRisk = []
for b in BMI:
    bmi_cat,health_risk = bmiCat(b)
    bmicatogery.append(bmi_cat)
    healthRisk.append(health_risk)

json_df['BMI'] = BMI
json_df['BMI Category'] = bmicatogery
json_df['Health Risk'] = healthRisk
print(json_df)
