const express = require('express');
const app = express();

app.use(express.json()); // Para parsear el cuerpo de la solicitud como JSON

app.post('/webhook', (req, res) => {
    console.log('Webhook recibido xavi:', req.body);
    res.status(200).send('Webhook recibido exitosamente');
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Servidor escuchando en http://localhost:${PORT}`);
});
