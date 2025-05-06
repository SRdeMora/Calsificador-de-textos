document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("botonClasificar").addEventListener("click", function() {
        let texto = document.getElementById("textoEntrada").value;
        
        fetch("https://calsificador-de-textos.onrender.com/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: texto })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("resultado").innerText = "Categoría: " + (data.category || "Error en la predicción");
        })
        .catch(error => {
            console.error("Error:", error);
            document.getElementById("resultado").innerText = "Error en la conexión con el servidor.";
        });
    });
});
