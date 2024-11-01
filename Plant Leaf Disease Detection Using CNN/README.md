# Prerequisites

- Docker installed on your system. [Get Docker](https://docs.docker.com/get-docker/)

# Quick Start

1. Clone this repository:

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Build the Docker image:

   ```bash
   docker build -t streamlit-plant-disease-detection .
   ```

3. Run the Docker container:

   ```bash
   docker run --rm -p 8501:8501 streamlit-plant-disease-detection
   ```

4. Open your web browser and go to `http://localhost:8501` to view the Streamlit application.

---

Run without docker:

```bash
streamlit run app.py --server.enableXsrfProtection false
```

# Dataset

- [Apple Leaf Disease Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset)
