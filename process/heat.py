from enum import Enum

class Eligibility(Enum):
    UNSURE = "Unsure if Eligible"
    ELIGIBLE = "Placeholder"
    NOT_ELIGIBLE = "Not Eligible"

def get_eligibility04(data):
    burner_type = data.get("HSI_BurnerType",None)
    mod_works = data.get("BCP_ModulationPressuretrol",None)
    burner_set = data.get("BCP_PressuretrolSettings")[0] if data.get("BCP_PressuretrolSettings",None) else None
    day_night_adj = data.get("BC_AdjustRatios")[0] if data.get("BC_AdjustRatios",None) else None
    day_night_cut = data.get("BC_CutoffTemps")[0] if data.get("BC_CutoffTemps",None) else None

    if burner_type == "TBD":
        return Eligibility.UNSURE.value
    elif burner_type in ["Hi","Other","N/A"]:
        return Eligibility.NOT_ELIGIBLE.value
    elif mod_works  == "TBD":
        return Eligibility.UNSURE.value
    elif mod_works == "N/A":
        return Eligibility.NOT_ELIGIBLE.value
    elif mod_works == "No":
        return Eligibility.ELIGIBLE.value
    elif burner_set == "TBD":
        return Eligibility.UNSURE.value
    elif burner_set == "N/A":
        return Eligibility.NOT_ELIGIBLE.value
    elif burner_set == "No":
        return Eligibility.ELIGIBLE.value
    elif day_night_adj == "TBD":
        return Eligibility.UNSURE.value
    elif day_night_adj == "N/A":
        return Eligibility.NOT_ELIGIBLE.value
    elif day_night_adj == "No":
        return Eligibility.ELIGIBLE.value
    elif day_night_cut == "TBD":
        return Eligibility.UNSURE.value
    elif day_night_cut in ["N/A","Yes"]:
        return Eligibility.NOT_ELIGIBLE.value
    elif day_night_cut == "No":
        return Eligibility.ELIGIBLE.value
    
    


    

