# End-to-End-Book-Recommendation-System
📚 End-to-End Book Recommender System

An end-to-end Machine Learning project that recommends books based on user input using content-based filtering (TF-IDF + cosine similarity).
The system is built with a modular pipeline architecture, deployed using Streamlit, and containerized with Docker.

🚀 Features
📖 Book recommendation based on similarity
⚙️ Modular ML pipeline (ingestion → transformation → training → prediction)
📂 Config-driven architecture using config.yaml
🌐 Interactive UI using Streamlit
🐳 Docker support for deployment
☁️ Ready for AWS EC2 deployment
🧠 Tech Stack
Language: Python
Libraries: Pandas, NumPy, Scikit-learn
ML Technique: TF-IDF + Cosine Similarity
Web App: Streamlit
Deployment: Docker, AWS EC2
📂 Project Structure
End-to-End-Book-Recommender-System/
│
├── config.yaml                # Configuration parameters
│
├── entity/                    # Data classes
│
├── config/
│   └── configuration.py      # Reads config.yaml
│
├── components/               # Core ML modules
│   ├── data_ingestion.py
│   ├── data_transformation.py
│   ├── model_trainer.py
│
├── pipeline/                 # Training & prediction pipelines
│   ├── training_pipeline.py
│   ├── prediction_pipeline.py
│
├── main.py                   # Runs training pipeline
├── app.py                    # Streamlit UI
⚙️ How It Works
Data Ingestion
Downloads and loads dataset
Data Transformation
Cleans text data
Converts book descriptions into vectors using TF-IDF
Model Training
Computes similarity using cosine similarity
Prediction
Takes user input (book name)
Recommends similar books
UI (Streamlit)
Interactive interface for users
🧪 Installation & Setup
Step 1: Clone Repository
git clone https://github.com/MSIVAPAPARAO13/End-to-End-Book-Recommendation-System.git
cd End-to-End-Book-Recommender-System
Step 2: Create Conda Environment
conda create -n books python=3.7.10 -y
conda activate books
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Training Pipeline
python main.py
Step 5: Run Streamlit App
streamlit run app.py

Open in browser:

http://localhost:8501
🐳 Docker Deployment
Build Docker Image
docker build -t book-recommender .
Run Container
docker run -d -p 8501:8501 book-recommender

Access app:

http://<your-ip>:8501
☁️ AWS EC2 Deployment
Launch EC2 (Ubuntu)
Open port 8501
Install Docker
Clone repository
Build & run container
🎯 Use Cases
📚 Online book stores
📖 Library systems
🎓 Educational platforms
🛒 Personalized recommendation engines
📈 Future Improvements
🔥 Add Collaborative Filtering
🔥 Hybrid Recommendation System
🔥 Deep Learning (BERT embeddings)
🔥 User login & personalization
🔥 Deploy on cloud platforms (GCP / Azure)
🧑‍💻 Author

Siva Paparao Medisetti
B.Tech CSE | Machine Learning Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to contribute!