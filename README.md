📚 End-to-End Book Recommender System

An end-to-end Machine Learning project that recommends books based on user input using Collaborative Filtering (KNN).

The system is built with a modular pipeline architecture, deployed using Streamlit, and containerized with Docker.

🚀 Features
📖 Book recommendation using similarity (KNN)
⚙️ Modular ML pipeline
(Ingestion → Validation → Transformation → Training → Recommendation)
📂 Config-driven architecture using config.yaml
🌐 Interactive UI with Streamlit
🐳 Docker support for deployment
☁️ Ready for AWS EC2 deployment
🧠 Tech Stack
Language: Python
Libraries: Pandas, NumPy, Scikit-learn, SciPy
ML Algorithm: K-Nearest Neighbors (Collaborative Filtering)
Web App: Streamlit
Deployment: Docker, AWS EC2
📂 Project Structure
End-to-End-Book-Recommender-System/
│
├── config/
│   └── config.yaml                # Configuration file
│
├── books_recommender/
│   ├── components/                # ML pipeline stages
│   │   ├── stage_00_data_ingestion.py
│   │   ├── stage_01_data_validation.py
│   │   ├── stage_02_data_transformation.py
│   │   ├── stage_03_model_trainer.py
│   │
│   ├── config/
│   │   └── configuration.py       # Reads config.yaml
│   │
│   ├── entity/
│   │   └── config_entity.py       # Data structures
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py   # Orchestrates pipeline
│   │
│   ├── utils/
│   │   └── util.py                # Helper functions
│   │
│   ├── logger/
│   │   └── log.py
│   │
│   ├── exception/
│   │   └── exception_handler.py
│
├── artifacts/                     # Generated outputs
│
├── main.py                        # Run training pipeline
├── app.py                         # Streamlit UI
├── requirements.txt
├── Dockerfile
⚙️ How It Works
1️⃣ Data Ingestion
Downloads dataset from URL
Extracts files into artifacts folder
2️⃣ Data Validation
Cleans dataset
Filters active users & popular books
Saves cleaned data
3️⃣ Data Transformation
Creates user-item matrix (pivot table)
Prepares data for model
4️⃣ Model Training
Trains KNN model using cosine similarity
Saves model as .pkl
5️⃣ Recommendation
Takes user input (book name)
Returns similar books
6️⃣ UI (Streamlit)
Interactive web interface
Displays recommendations with images
🧪 Installation & Setup
Step 1: Clone Repository
git clone https://github.com/MSIVAPAPARAO13/End-to-End-Book-Recommendation-System.git
cd End-to-End-Book-Recommendation-System
Step 2: Create Conda Environment
conda create -n books python=3.7.10 -y
conda activate books
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Training Pipeline
python main.py
Step 5: Run Streamlit App
streamlit run app.py
🌐 Open in Browser
http://localhost:8501
🐳 Docker Deployment
Build Image
docker build -t book-recommender .
Run Container
docker run -d -p 8501:8501 book-recommender
Access App
http://localhost:8501
☁️ AWS EC2 Deployment
Steps:
Launch EC2 (Ubuntu)
Open port 8501
Install Docker
Clone repository
Build & run container
🎯 Use Cases
📚 Online Book Stores
📖 Library Systems
🎓 Educational Platforms
🛒 Personalized Recommendation Engines
📈 Future Improvements
🔥 Hybrid Recommendation System
🔥 Deep Learning (BERT embeddings)
🔥 User personalization
🔥 Cloud deployment (GCP / Azure)
🧑‍💻 Author

Siva Paparao Medisetti
B.Tech CSE | Machine Learning Enthusiast

⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Feel free to contribute