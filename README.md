Deep Learning Image Classification Project

Deep Learning Image Classification Project
==========================================

This project focuses on building a Convolutional Neural Network (CNN) based image classification system using TensorFlow and Keras. It also includes a Flask backend that serves both a web-based user interface and an API endpoint for making predictions.

Project Structure
-----------------

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
    

**models:** Contains trained model files (.h5) for image classification.

**notebook:** Includes a Jupyter notebook (notebook.ipynb) for generating and training the CNN model.

**static:** Stores images used in the HTML frontend.

**templates:** Contains the HTML file (index.html) for serving the frontend.

**app.py:** Flask application code providing API endpoints and serving the frontend.

**Dockerfile:** Configuration for building a Docker container.

Features
--------

*   Utilizes a Convolutional Neural Network (CNN) for image classification.
*   Web-based frontend accessible at `http://localhost:5000`.
*   API endpoint for predictions accessible at `http://localhost:5000/predict`.

Technologies Used
-----------------

*   Deep Learning (TensorFlow, Keras)
*   Frontend (HTML, CSS)
*   Docker
*   Flask

Environment Setup
-----------------

To set up the project environment, follow these steps:

1.  Create a new Conda environment:
`conda create --name cv_tensorflow_tumor`3.  Activate the environment:
`conda activate cv_tensorflow_tumor`5.  Install required packages:
`conda install tensorflow==2.12 keras==2.12 flask numpy pandas pillow asyncio`

Running the Project
-------------------

1.  Clone this repository:
`git clone https://github.com/yourusername/your-repo.git`3.  Navigate to the project directory:
`cd your-repo`5.  Run the Flask application:
`python app.py`7.  Access the web-based frontend at `http://localhost:5000` and the API endpoint at `http://localhost:5000/predict`.

Docker Support
--------------

You can also run the project as a Docker container. Build the Docker image using the provided `Dockerfile`:

`docker build -t image-classification-app .`

Run the Docker container:

`docker run -p 5000:5000 image-classification-app`

Access the web-based frontend and API endpoint as before.
