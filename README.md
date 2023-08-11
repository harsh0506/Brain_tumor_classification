<!DOCTYPE html>
<html>

<head>
    <title>Deep Learning Image Classification Project</title>
</head>

<body>
    <h1>Deep Learning Image Classification Project</h1>

    <p>This project focuses on building a Convolutional Neural Network (CNN) based image classification system using
        TensorFlow and Keras. It also includes a Flask backend that serves both a web-based user interface and an API
        endpoint for making predictions.</p>

    <h2>Project Structure</h2>
    <pre>
        |- models
              |--- model.h5
        |- notebook
              |--- notebook.ipynb
        |- static
              |--- (images for HTML)
        |- templates
              |--- index.html
        |- app.py
        |- Dockerfile
    </pre>

    <p><strong>models:</strong> Contains trained model files (.h5) for image classification.</p>
    <p><strong>notebook:</strong> Includes a Jupyter notebook (notebook.ipynb) for generating and training the CNN
        model.</p>
    <p><strong>static:</strong> Stores images used in the HTML frontend.</p>
    <p><strong>templates:</strong> Contains the HTML file (index.html) for serving the frontend.</p>
    <p><strong>app.py:</strong> Flask application code providing API endpoints and serving the frontend.</p>
    <p><strong>Dockerfile:</strong> Configuration for building a Docker container.</p>

    <h2>Features</h2>
    <ul>
        <li>Utilizes a Convolutional Neural Network (CNN) for image classification.</li>
        <li>Web-based frontend accessible at <code>http://localhost:5000</code>.</li>
        <li>API endpoint for predictions accessible at <code>http://localhost:5000/predict</code>.</li>
    </ul>

    <h2>Technologies Used</h2>
    <ul>
        <li>Deep Learning (TensorFlow, Keras)</li>
        <li>Frontend (HTML, CSS)</li>
        <li>Docker</li>
        <li>Flask</li>
    </ul>

    <h2>Environment Setup</h2>
    <p>To set up the project environment, follow these steps:</p>
    <ol>
        <li>Create a new Conda environment:</li>
        <code>conda create --name cv_tensorflow_tumor</code>
        <li>Activate the environment:</li>
        <code>conda activate cv_tensorflow_tumor</code>
        <li>Install required packages:</li>
        <code>conda install tensorflow==2.12 keras==2.12 flask numpy pandas pillow asyncio</code>
    </ol>

    <h2>Running the Project</h2>
    <ol>
        <li>Clone this repository:</li>
        <code>git clone https://github.com/yourusername/your-repo.git</code>
        <li>Navigate to the project directory:</li>
        <code>cd your-repo</code>
        <li>Run the Flask application:</li>
        <code>python app.py</code>
        <li>Access the web-based frontend at <code>http://localhost:5000</code> and the API endpoint at
            <code>http://localhost:5000/predict</code>.</li>
    </ol>

    <h2>Docker Support</h2>
    <p>You can also run the project as a Docker container. Build the Docker image using the provided <code>Dockerfile</code>:</p>
    <code>docker build -t image-classification-app .</code>
    <p>Run the Docker container:</p>
    <code>docker run -p 5000:5000 image-classification-app</code>
    <p>Access the web-based frontend and API endpoint as before.</p>
</body>

</html>
