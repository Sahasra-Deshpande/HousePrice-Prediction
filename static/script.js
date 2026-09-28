async function predictPrice() {

    const area = Number(
        document.getElementById("area").value
    );

    const bedrooms = Number(
        document.getElementById("bedrooms").value
    );

    const bathrooms = Number(
        document.getElementById("bathrooms").value
    );

    const age = Number(
        document.getElementById("age").value
    );


    if (!area || !bedrooms || !bathrooms || age < 0) {

        document.getElementById("result").innerText =
            "Please enter all details.";

        return;
    }


    const response = await fetch("/predict", {

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


    const data = await response.json();


    document.getElementById("result").innerText =
        "Estimated Price: ₹ " + data.price + " Lakhs";

}