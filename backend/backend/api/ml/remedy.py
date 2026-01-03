# -------------------------------------------------
# Betel Leaf Disease Remedies (Severity-based)
# -------------------------------------------------

REMEDY_DATA = {

    "Bacterial_Leaf_Blight": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Remove and destroy infected leaves",
                "Avoid overhead irrigation",
                "Improve field drainage"
            ],
            "scientific": [
                "Spray copper oxychloride (2–2.5 g per liter of water)"
            ],
            "prevention": [
                "Use disease-free planting material",
                "Disinfect cutting tools regularly",
                "Avoid water stagnation"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Prune infected branches",
                "Increase plant spacing"
            ],
            "scientific": [
                "Apply copper-based bactericide every 7–10 days"
            ],
            "prevention": [
                "Monitor plants weekly",
                "Avoid splashing water on leaves"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
            
            "cultural": [
                "Remove and destroy heavily infected plants"
            ],
            "scientific": [
                "Apply recommended bactericides under agricultural officer guidance"
            ],
            "prevention": [
                "Crop rotation",
                "Soil sterilization before replanting"
            ]
        }
    },

    "Fungal_Brown_Spot": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Remove infected leaves",
                "Reduce leaf wetness"
            ],
            "scientific": [
                "Spray neem oil or mancozeb (2 g per liter)"
            ],
            "prevention": [
                "Maintain field hygiene",
                "Ensure good air circulation"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Prune affected areas"
            ],
            "scientific": [
                "Apply systemic fungicide at 10-day intervals"
            ],
            "prevention": [
                "Improve drainage",
                "Avoid dense planting"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
            
            "cultural": [
                "Destroy infected plants"
            ],
            "scientific": [
                "Use systemic fungicides under expert supervision"
            ],
            "prevention": [
                "Use resistant varieties",
                "Practice crop rotation"
            ]
        }
    },

    "Leaf_Spot": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Remove affected leaves",
                "Clean fallen debris"
            ],
            "scientific": [
                "Apply neem oil spray weekly"
            ],
            "prevention": [
                "Improve air circulation",
                "Avoid excess moisture"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Prune infected leaves"
            ],
            "scientific": [
                "Apply fungicides like chlorothalonil"
            ],
            "prevention": [
                "Reduce irrigation frequency",
                "Monitor plant health"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
            
            "cultural": [
                "Remove and destroy infected plants"
            ],
            "scientific": [
                "Apply systemic fungicide as recommended"
            ],
            "prevention": [
                "Soil treatment",
                "Crop rotation"
            ]
        }
    },

    "Kalamadiri_Haniya": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Improve soil drainage",
                "Remove early infected spots"
            ],
            "scientific": [
                "Apply bio-fungicides"
            ],
            "prevention": [
                "Maintain clean field conditions"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Remove infected leaves"
            ],
            "scientific": [
                "Apply recommended fungicides"
            ],
            "prevention": [
                "Avoid water stagnation"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
            
            "cultural": [
                "Remove infected plants completely"
            ],
            "scientific": [
                "Chemical fungicides under expert advice"
            ],
            "prevention": [
                "Soil disinfection before next crop"
            ]
        }
    },

    "Red_Spider_Mite": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Wash leaves with water",
                "Increase humidity"
            ],
            "scientific": [
                "Spray neem oil or soap solution"
            ],
            "prevention": [
                "Inspect underside of leaves regularly"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Remove infested leaves"
            ],
            "scientific": [
                "Apply acaricides as recommended"
            ],
            "prevention": [
                "Avoid drought stress"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
           
            "cultural": [
                "Isolate infected plants"
            ],
            "scientific": [
                "Chemical acaricides under expert guidance"
            ],
            "prevention": [
                "Prevent spread to healthy plants"
            ]
        }
    },

    "Caterpillar_Damage": {
        "early": {
            "warning_level": "LOW",
            
            "cultural": [
                "Hand-pick caterpillars"
            ],
            "scientific": [
                "Use neem extract spray"
            ],
            "prevention": [
                "Regular field inspection"
            ]
        },
        "moderate": {
            "warning_level": "MEDIUM",
            
            "cultural": [
                "Use light traps",
                "Encourage natural predators"
            ],
            "scientific": [
                "Apply Bacillus thuringiensis (Bt)"
            ],
            "prevention": [
                "Monitor larval activity"
            ]
        },
        "severe": {
            "warning_level": "HIGH",
            
            "cultural": [
                "Remove severely damaged plants"
            ],
            "scientific": [
                "Chemical insecticides under guidance"
            ],
            "prevention": [
                "Prevent reinfestation"
            ]
        }
    }
}

# -------------------------------------------------
# Helper (18-class compatible)
# -------------------------------------------------
def get_remedy(severity_label: str):
    disease, severity = severity_label.split("/")
    data = REMEDY_DATA.get(disease, {}).get(severity, {})

    return {
        "warning_level": data.get("warning_level", "UNKNOWN"),
        "cultural": data.get("cultural", []),
        "scientific": data.get("scientific", []),
        "prevention": data.get("prevention", [])
    }
