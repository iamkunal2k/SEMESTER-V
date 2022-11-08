const express = require('express');
const app = express()
const PORT = 8700;
const cors = require('cors')

app.use(cors())
app.get('/', (req, res) => {
	res.json({
		data : [
			{ 'name': 'Dhairya Kukadia', 'rollNo': 23 },
			{ 'name': 'Kunal Kumbhare', 'rollNo': 24},
			{ 'name': 'Mayank Raj', 'rollNo': 26}

		]
	})
})

app.listen(PORT, () => {
	console.log(`http://localhost:${PORT}`)
})
