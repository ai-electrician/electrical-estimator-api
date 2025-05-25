from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate-estimate', methods=['POST'])
def generate_estimate():
    data = request.get_json()

    square_feet = data.get("squareFeet", 0)
    outlet_count = data.get("outletCount", 0)
    lighting_count = data.get("lightingFixtureCount", 0)
    switch_count = data.get("switchCount", 0)
    panel_count = data.get("panelCount", 0)
    emt_conduit_feet = data.get("emtConduitFeet", 0)

    materials = [
        {"name": "Duplex outlet", "quantity": outlet_count, "unit": "each"},
        {"name": "Lighting fixture", "quantity": lighting_count, "unit": "each"},
        {"name": "Single pole switch", "quantity": switch_count, "unit": "each"},
        {"name": "Electrical panel", "quantity": panel_count, "unit": "each"},
        {"name": "EMT conduit", "quantity": emt_conduit_feet, "unit": "feet"},
        {"name": "12AWG THHN wire", "quantity": outlet_count * 50, "unit": "feet"}
    ]

    labor_hours = (
        outlet_count * 0.5 +
        lighting_count * 0.75 +
        switch_count * 0.3 +
        panel_count * 8 +
        (emt_conduit_feet / 20)
    )

    result = {
        "materials": materials,
        "laborHours": round(labor_hours, 1),
        "assumptions": "Calculated using basic rules of thumb for commercial installations."
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
