# 🦊 Zootopia Web Generator

## Project Description

This project is a **Python-based web content generator** that fetches real-time animal data from an external API (API-Ninjas) and dynamically creates a static HTML webpage (`animals.html`) to display the results.

### What problem does it solve?

The project demonstrates a clean, robust, and modern architecture for building small data-driven applications. Specifically, it solves the problem of **safely integrating external data** into a web display while adhering to industry best practices, such as:
1.  **Securing API keys** using a `.env` file and `.gitignore`.
2.  **Modularizing code** (separating data fetching from web generation).
3.  **Handling user input** and gracefully displaying error messages for non-existent search terms.

### Who is the intended audience?

The intended audience includes:
* Users interested in quickly generating a simple HTML list of animal facts based on a keyword.
* Developers learning best practices for **API integration**, **environment variable management (`dotenv`)**, and **Python project structure**.

***

## Usage

Follow these steps to set up and run the Zootopia Web Generator.

### 1. Project Setup and Dependencies

Before running the script, you must install the necessary packages and set up your environment variables.

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_REPOSITORY_URL]
    cd Zootopia_with_API
    ```

2.  **Activate the virtual environment (Recommended):**
    ```bash
    # Create the environment
    python3 -m venv venv
    # Activate the environment
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    The project relies on `requests` and `python-dotenv`.
    ```bash
    pip install -r requirements.txt
    ```

### 2. Configuration (API Key)

This program requires an API key to communicate with the data source. **For security, this key is loaded from a local `.env` file which is ignored by Git.**

1.  **Create the `.env` file:** Create a copy of the provided `.env.example` file and rename it to **`.env`** in the root directory.
    ```bash
    cp .env.example .env
    ```

2.  **Insert your personal API key:** Open the new **`.env`** file and insert your API key in the following format:
    ```env
    API_KEY=YOUR_ACTUAL_API_KEY_HERE
    ```

### 3. Execution

Run the main script from your terminal. The program will prompt you for an animal name.

1.  **Start the script:**
    ```bash
    python3 animal_web_generator.py
    ```

2.  **Enter the animal name when prompted:**
    ```
    Enter a name of an animal: Fox 
    ```

**Output:**
The program will display the fetched data in the console and then generate the static output file:
`Website was successfully generated to the file animals.html.`

To view the results, open the newly created `animals.html` file in your web browser.

***

## Contributing Guidelines (Optional)

We welcome contributions to improve the Zootopia Web Generator!

1.  **Fork** the repository.
2.  Create a new feature branch (`git checkout -b feature/new-data-source`).
3.  Commit your changes following conventional commit style (e.g., `feat: added database connection`).
4.  Push to the branch (`git push origin feature/new-data-source`).
5.  Open a **Pull Request**.