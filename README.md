# 📚 End-to-End Book Recommender System
<img width="1600" height="937" alt="image" src="https://github.com/user-attachments/assets/2d25a8a7-6937-438a-b030-edd099782a83" />

An end-to-end Machine Learning project that recommends books based on user input using **Collaborative Filtering (KNN)**.

The system is built using a modular pipeline architecture, deployed with **Streamlit**, and containerized using **Docker**.

---

## 🚀 Features

* 📖 Book recommendation using KNN similarity
* ⚙️ Modular ML pipeline

  * Data Ingestion → Validation → Transformation → Training → Recommendation
* 📂 Config-driven architecture (`config.yaml`)
* 🌐 Interactive UI using Streamlit
* 🐳 Docker support for deployment
* ☁️ Ready for AWS EC2 deployment

---

## 🧠 Tech Stack

**Language:**

* Python

**Libraries:**

* Pandas
* NumPy
* Scikit-learn
* SciPy

**ML Algorithm:**

* K-Nearest Neighbors (Collaborative Filtering)

**Web App:**

* Streamlit

**Deployment:**

* Docker
* AWS EC2

---

## 📂 Project Structure

```
End-to-End-Book-Recommender-System/
│
├── config/
│   ├── config.yaml
│   └── configuration.py
│
├── books_recommender/
│   ├── components/
│   │   ├── stage_00_data_ingestion.py
│   │   ├── stage_01_data_validation.py
│   │   ├── stage_02_data_transformation.py
│   │   └── stage_03_model_trainer.py
│   │
│   ├── pipeline/
│   │   └── training_pipeline.py
│   │
│   ├── entity/
│   │   └── config_entity.py
│   │
│   ├── utils/
│   ├── logger/
│   └── exception/
│
├── artifacts/                # Generated files (models, data)
├── app.py                    # Streamlit app
├── main.py                   # Run training pipeline
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Data Ingestion

* Downloads dataset from URL
* Extracts into local directory

### 2️⃣ Data Validation

* Cleans dataset
* Filters active users & popular books

### 3️⃣ Data Transformation

* Creates user-item matrix (pivot table)

### 4️⃣ Model Training

* Trains KNN model
* Saves model as `.pkl`

### 5️⃣ Recommendation

* Takes user input (book name)
* Returns similar books

### 6️⃣ UI (Streamlit)

* Interactive web interface
* Displays recommendations with images

---

## 🧪 Installation & Setup

### 🔹 Step 1: Clone Repository

```bash
git clone https://github.com/MSIVAPAPARAO13/End-to-End-Book-Recommendation-System.git
cd End-to-End-Book-Recommendation-System
```

---

### 🔹 Step 2: Create Environment

```bash
conda create -n books python=3.7.10 -y
conda activate books
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 🔹 Step 4: Run Training Pipeline

```bash
python main.py
```

---

### 🔹 Step 5: Run Streamlit App

```bash
streamlit run app.py
```

---

### 🌐 Open in Browser

```
http://localhost:8501
```

---

## 🐳 Docker Deployment

### 🔹 Build Image

```bash
docker build -t book-recommender .
```

---

### 🔹 Run Container

```bash
docker run -d -p 8501:8501 book-recommender
```

---

### 🌐 Access App

```
http://localhost:8501
```

---

## ☁️ AWS EC2 Deployment

1. Launch EC2 (Ubuntu)
2. Open port **8501**
3. Install Docker
4. Clone repository
5. Build & run container

---

## 🎯 Use Cases

* 📚 Online book stores
* 📖 Library systems
* 🎓 Educational platforms
* 🛒 Personalized recommendation engines

---

## 📈 Future Improvements

* 🔥 Hybrid Recommendation System
* 🔥 Deep Learning (BERT embeddings)
* 🔥 User login & personalization
* 🔥 Cloud deployment (GCP / Azure)

---

## 🧑‍💻 Author

**Siva Paparao Medisetti**
B.Tech CSE | Machine Learning Enthusiast

---

## ⭐ Support

If you like this project:

👉 Give it a ⭐ on GitHub
👉 Feel free to contribute
