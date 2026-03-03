import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static",
    static_url_path="/static"
)

UPLOAD_FOLDER = "../uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# =========================
# DISEASE INFORMATION
# =========================

DISEASE_INFO = {
    "Acne": {
        "details": "A common skin condition causing pimples, blackheads, and whiteheads.",
        "cause": "Clogged pores due to oil buildup, bacteria, and hormonal changes."
    },
    "Actinic Keratosis": {
        "details": "Rough, scaly patches caused by long-term sun exposure.",
        "cause": "UV radiation damage to skin cells."
    },
    "Benign Tumors": {
        "details": "Non-cancerous growths on the skin.",
        "cause": "Abnormal but harmless cell growth."
    },
    "Bullous": {
        "details": "Fluid-filled blisters on the skin.",
        "cause": "Autoimmune reactions or infections."
    },
    "Candidiasis": {
        "details": "Fungal infection affecting moist areas of skin.",
        "cause": "Overgrowth of Candida fungus."
    },
    "Drug Eruption": {
        "details": "Skin reaction caused by medication.",
        "cause": "Allergic response to certain drugs."
    },
    "Eczema": {
        "details": "Inflammatory skin condition causing itching and redness.",
        "cause": "Immune system overreaction and environmental triggers."
    },
    "Infestations/Bites": {
        "details": "Skin irritation caused by insect bites or infestations.",
        "cause": "Parasites or insect exposure."
    },
    "Lichen": {
        "details": "Chronic inflammatory condition with purple itchy rash.",
        "cause": "Immune system dysfunction."
    },
    "Lupus": {
        "details": "Autoimmune disease affecting skin and organs.",
        "cause": "Immune system attacking healthy tissues."
    },
    "Moles": {
        "details": "Small dark skin growths made of pigment cells.",
        "cause": "Clustered melanocytes."
    },
    "Psoriasis": {
        "details": "Chronic autoimmune condition causing scaly patches.",
        "cause": "Rapid skin cell production."
    },
    "Rosacea": {
        "details": "Facial redness and visible blood vessels.",
        "cause": "Genetic and environmental triggers."
    },
    "Seborrheic Keratoses": {
        "details": "Non-cancerous brown or black growths.",
        "cause": "Unknown, often age-related."
    },
    "Skin Cancer": {
        "details": "Abnormal malignant growth of skin cells.",
        "cause": "Excessive UV exposure."
    },
    "Sun/Sunlight Damage": {
        "details": "Skin damage due to prolonged sun exposure.",
        "cause": "Ultraviolet radiation."
    },
    "Tinea": {
        "details": "Fungal infection known as ringworm.",
        "cause": "Dermatophyte fungi."
    },
    "Unknown/Normal": {
        "details": "The skin appears normal or condition not recognized.",
        "cause": "No major abnormality detected."
    },
    "Vascular Tumors": {
        "details": "Growths formed from blood vessels.",
        "cause": "Abnormal blood vessel formation."
    },
    "Vasculitis": {
        "details": "Inflammation of blood vessels.",
        "cause": "Autoimmune or infection-related inflammation."
    },
    "Vitiligo": {
        "details": "Loss of skin pigment in patches.",
        "cause": "Autoimmune destruction of pigment cells."
    },
    "Warts": {
        "details": "Small rough growths caused by virus.",
        "cause": "Human papillomavirus (HPV)."
    }
}


# =========================
# KEYWORD MATCHING
# =========================

DISEASE_KEYWORDS = {
    "Acne": ["acne"],
    "Actinic Keratosis": ["actinic"],
    "Benign Tumors": ["benign"],
    "Bullous": ["bullous"],
    "Candidiasis": ["candidiasis", "candida"],
    "Drug Eruption": ["drug"],
    "Eczema": ["eczema"],
    "Infestations/Bites": ["infestation", "bite"],
    "Lichen": ["lichen"],
    "Lupus": ["lupus"],
    "Moles": ["mole"],
    "Psoriasis": ["psoriasis"],
    "Rosacea": ["rosacea"],
    "Seborrheic Keratoses": ["seborrheic", "keratosis"],
    "Skin Cancer": ["cancer"],
    "Sun/Sunlight Damage": ["sun", "damage"],
    "Tinea": ["tinea"],
    "Unknown/Normal": ["normal", "unknown"],
    "Vascular Tumors": ["vascular"],
    "Vasculitis": ["vasculitis"],
    "Vitiligo": ["vitiligo"],
    "Warts": ["wart"]
}


def predict_from_filename(filename):
    name = filename.lower().replace("-", " ").replace("_", " ")

    for disease, keywords in DISEASE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in name:
                return disease

    return "Unknown/Normal"


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    image_file = None

    if request.method == "POST":
        file = request.files["image"]
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            disease = predict_from_filename(filename)

            result = {
                "name": disease,
                "details": DISEASE_INFO[disease]["details"],
                "cause": DISEASE_INFO[disease]["cause"]
            }

            image_file = filename

    return render_template(
        "index.html",
        result=result,
        image_file=image_file
    )


if __name__ == "__main__":
    app.run(debug=True)