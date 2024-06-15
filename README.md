# Recommender-system

# Movie Recommender System

This is a movie recommender system built with Streamlit. Follow the steps below to set up the project on your local machine.

## Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/rohanshr135/Recommender-system.git
    cd Recommender-system
    ```

2. **Create and activate a virtual environment:**

    - For Windows:
      ```sh
      python -m venv env
      .\env\Scripts\activate
      ```
    - For macOS/Linux:
      ```sh
      python3 -m venv env
      source env/bin/activate
      ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

## Notes

- Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
- This project uses Git LFS for large files. Make sure you have Git LFS installed and initialized. You can find more information [here](https://git-lfs.github.com/).

## Troubleshooting

- If you encounter any issues with Git LFS, run the following commands:
  ```sh
  git lfs install
  git lfs pull

### 4. Install Git LFS

For users cloning the repository, they need to have Git LFS installed to properly pull the large files:

1. **Install Git LFS:**
   - For macOS:
     ```sh
     brew install git-lfs
     ```
   - For Windows and Linux, follow the instructions on the [Git LFS installation page](https://git-lfs.github.com/).

2. **Initialize Git LFS:**

   ```sh
   git lfs install

Clone the Repository and Pull LFS Files
   git clone https://github.com/rohanshr135/Recommender-system.git
cd Recommender-system
git lfs pull

