// Evento para consultar cliente
document.getElementById("consultaForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let identificacion = document.getElementById("identificacionConsulta").value;

    fetch(`http://localhost:8000/clientes/${identificacion}`)
    .then(response => {
        if (!response.ok) {
            throw new Error("Cliente no encontrado");
        }
        return response.json();
    })
    .then(data => {
        let clienteInfo = `
            <h3>Información del Cliente</h3>
            <p><strong>Nombres:</strong> ${data.nombres}</p>
            <p><strong>Apellidos:</strong> ${data.apellidos}</p>
            <p><strong>Tipo de Identificación:</strong> ${data.tipoIdentificacion}</p>
            <p><strong>Fecha de Nacimiento:</strong> ${data.fechaNacimiento}</p>
            <p><strong>Número de Celular:</strong> ${data.numeroCelular}</p>
            <p><strong>Correo Electrónico:</strong> ${data.correoElectronico}</p>
            <h4>Servicios Contratados</h4>
            <ul>
        `;

        data.servicios.forEach(servicio => {
            clienteInfo += `<li>${servicio.servicio} (Inicio: ${servicio.fechaInicio}, Última Facturación: ${servicio.ultimaFacturacion}, Último Pago: ${servicio.ultimoPago})</li>`;
        });

        clienteInfo += `</ul>`;
        document.getElementById("clienteInfo").innerHTML = clienteInfo;
    })
    .catch(error => {
        document.getElementById("clienteInfo").innerText = error.message;
    });
});

// Evento para registrar servicio
document.getElementById("servicioForm").addEventListener("submit", function(event) {
    event.preventDefault();

    let identificacion = document.getElementById("identificacion").value;
    let servicioData = {
        servicio: document.getElementById("servicio").value,
        fechaInicio: document.getElementById("fechaInicio").value,
        ultimaFacturacion: document.getElementById("ultimaFacturacion").value,
        ultimoPago: parseInt(document.getElementById("ultimoPago").value)
    };

    fetch(`http://localhost:8000/clientes/${identificacion}/servicios/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(servicioData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("resultado").innerText = `Servicio registrado exitosamente para el cliente: ${data.identificacion}`;
    })
    .catch(error => {
        document.getElementById("resultado").innerText = "Error registrando servicio: " + error;
    });
});
