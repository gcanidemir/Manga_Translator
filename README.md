# Manga Translator

This is a Python application that uses Optical Character Recognition (OCR) to extract text from manga images and translate it.

## Usage
Change the image path of the manga panel you want to translate at **app.py**.
```python
imgPath = 'Examples/6.png'
````

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/gcanidemir/Manga_Translator.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd "Manga Translator"
    ```
3.  Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4.  Activate the virtual environment:
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```
5.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the main application:

```bash
python app.py
```

