// index.js

const express = require('express');
const path = require('path');
require('dotenv').config(); // Load environment variables from .env file

const app = express();
const port = process.env.PORT || 3000; // Use PORT from environment variable or default to 3000

// Serve static files from the 'static' directory
app.use(express.static(path.join(__dirname, 'static')));

// Define routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'static', 'index.html')); // Serve the main HTML file
});

// Error handling middleware
app.use((req, res, next) => {
    res.status(404).send('404 Not Found'); // Handle 404 errors
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
