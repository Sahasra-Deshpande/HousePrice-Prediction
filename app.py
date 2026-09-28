from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib

app = FastAPI()

# Load model
model = joblib.load("model/house_price_model.pkl")


@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>House Price Prediction</title>

        <style>

            body {
                font-family: Arial;
                background: #f2f2f2;
                text-align: center;
                padding-top: 80px;
            }

            .box {
                background: white;
                width: 400px;
                margin: auto;
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0 0 15px #ccc;
            }

            input {
                width: 90%;
                padding: 12px;
                margin: 8px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }

            button {
                width: 95%;
                padding: 12px;
                margin-top: 10px;
                background: black;
                color: white;
                border: none;
                border-radius: 6px;
                cursor: pointer;
            }

            #result {
                margin-top: 20px;
                font-size: 22px;
                font-weight: bold;
            }

        </style>

    </head>


    <body>

        <div class="box">

            <h1>🏠 House Price Prediction</h1>

            <input
                id="area"
                type="number"
                placeholder="Area (sq ft)"
            >

            <input
                id="bedrooms"
                type="number"
                placeholder="Bedrooms"
            >

            <input
                id="bathrooms"
                type="number"
                placeholder="Bathrooms"
            >

            <input
                id="age"
                type="number"
                placeholder="House Age"
            >

            <button onclick="predict()">
                Predict Price
            </button>

            <div id="result"></div>

        </div>


        <script>

            async function predict() {

                let area =
                    Number(document.getElementById("area").value);

                let bedrooms =
                    Number(document.getElementById("bedrooms").value);

                let bathrooms =
                    Number(document.getElementById("bathrooms").value);

                let age =
                    Number(document.getElementById("age").value);


                let response = await fetch("/predict", {

                    method: "POST",

                    headers: {
                        "Content-Type": "application/json"
                    },

                    body: JSON.stringify({

                        area: area,
                        bedrooms: bedrooms,
                        bathrooms: bathrooms,
                        age: age

                    })

                });


                let result = await response.json();


                document.getElementById("result").innerHTML =
                    "Estimated Price: ₹ " +
                    result.price +
                    " Lakhs";

            }

        </script>

    </body>

    </html>
    """


@app.post("/predict")
def predict(data: dict):

    area = float(data["area"])
    bedrooms = float(data["bedrooms"])
    bathrooms = float(data["bathrooms"])
    age = float(data["age"])


    input_data = [[
        area,
        bedrooms,
        bathrooms,
        age
    ]]


    prediction = model.predict(input_data)

    price = round(float(prediction[0]), 2)


    return {
        "price": price
    }