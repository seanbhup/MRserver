let app = require('express')();

app.get('/', (req, res) => {
    res.send('still gaming');
});

app.post('/brrr', (req, res) => {
    //process electrocution)

    res.send(200);
});

app.listen(3000, console.log('Server is listening in 3000'));
