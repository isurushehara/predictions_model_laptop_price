from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("../model/predictor.pickle", "rb"))

# Training columns (must be exactly the same as X_train.columns)
columns = [
    'Ram', 'Weight', 'Touchscreen', 'Ips', 'SSD', 'HDD', 'Hybrid',
    'Flash_Storage', 'Company_Acer', 'Company_Apple', 'Company_Asus',
    'Company_Dell', 'Company_HP', 'Company_Lenovo', 'Company_MSI',
    'Company_Other', 'Company_Toshiba', 'TypeName_2 in 1 Convertible',
    'TypeName_Gaming', 'TypeName_Netbook', 'TypeName_Notebook',
    'TypeName_Ultrabook', 'TypeName_Workstation', 'OpSys_Linux',
    'OpSys_Mac', 'OpSys_Other', 'OpSys_Windows', 'cpu_name_AMD',
    'cpu_name_Intel Core i3', 'cpu_name_Intel Core i5',
    'cpu_name_Intel Core i7', 'cpu_name_Other', 'gpu_name_AMD',
    'gpu_name_Intel', 'gpu_name_Nvidia'
]


@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None

    if request.method == "POST":

        ram = int(request.form["Ram"])
        weight = float(request.form["Weight"])
        touchscreen = int(request.form["Touchscreen"])
        ips = int(request.form["Ips"])

        ssd = float(request.form["SSD"])
        hdd = float(request.form["HDD"])
        hybrid = float(request.form["Hybrid"])
        flash = float(request.form["Flash_Storage"])

        company = request.form["Company"]
        typename = request.form["TypeName"]
        opsys = request.form["OpSys"]
        cpu = request.form["cpu_name"]
        gpu = request.form["gpu_name"]

        data = dict.fromkeys(columns, 0)

        data["Ram"] = ram
        data["Weight"] = weight
        data["Touchscreen"] = touchscreen
        data["Ips"] = ips
        data["SSD"] = ssd
        data["HDD"] = hdd
        data["Hybrid"] = hybrid
        data["Flash_Storage"] = flash

        # Company
        company_col = f"Company_{company}"
        if company_col in data:
            data[company_col] = 1

        # Type
        type_col = f"TypeName_{typename}"
        if type_col in data:
            data[type_col] = 1

        # Operating System
        os_col = f"OpSys_{opsys}"
        if os_col in data:
            data[os_col] = 1

        # CPU
        cpu_col = f"cpu_name_{cpu}"
        if cpu_col in data:
            data[cpu_col] = 1

        # GPU
        gpu_col = f"gpu_name_{gpu}"
        if gpu_col in data:
            data[gpu_col] = 1

        input_df = pd.DataFrame([data])

        prediction = model.predict(input_df)[0]

        # # Convert Indian Rupees to LKR
        prediction = prediction * 3.53

        prediction = round(prediction, 2)

    return render_template(
        "index.html",
        prediction=prediction
    )


if __name__ == "__main__":
    app.run(debug=True)
