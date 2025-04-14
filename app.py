import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄")

st.title("🔄 Universal Unit Converter")
st.markdown("Convert values between common units !")


unit_categories = {
    "Length": {
        "meters": 1,
        "kilometers": 1000,
        "feet": 0.3048,
        "miles": 1609.34
    },
    "Weight": {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.453592,
        "ounces": 0.0283495
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    }
}


category = st.selectbox("Select Unit Category", list(unit_categories.keys()))


if category != "Temperature":
    units = list(unit_categories[category].keys())

    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", value=0.0)

    # Conversion
    if from_unit and to_unit:
        base = value * unit_categories[category][from_unit]  
        result = base / unit_categories[category][to_unit]   
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

else:
    
    temp_units = list(unit_categories["Temperature"].keys())
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter temperature", value=0.0)

    def convert_temp(value, from_u, to_u):
        if from_u == to_u:
            return value
        if from_u == "Celsius":
            if to_u == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_u == "Kelvin":
                return value + 273.15
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (value - 32) * 5/9
            elif to_u == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return value - 273.15
            elif to_u == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32

    result = convert_temp(value, from_unit, to_unit)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
