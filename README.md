# RSA Key Generation with Python & Web Crypto API

This project demonstrates RSA key pair generation using two different methods:

1. **Python Implementation**: Utilizes the `pycryptodome` package to generate RSA key pairs in Python.  
2. **Web Implementation**: Uses the Web Crypto API to create a simple webpage that generates RSA key pairs directly in the browser.

## Features

- **Python Script**: Generates RSA keys and outputs them in PEM format.  
- **Webpage**: Provides an interface to generate RSA keys using the Web Crypto API and displays the results.

## Technologies Used

- **Python**: [PyCryptodome](https://pypi.org/project/pycryptodome/)  
- **Frontend**: HTML, JavaScript, [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)

## How to Run

1. **Python Script**:
   - Install the required package:
     ```bash
     pip install pycryptodome
     ```
   - Run the script:
     ```bash
     python rsa_keygen.py
     ```

2. **Webpage**:
   - Open `index.html` in your browser to generate RSA keys using the Web Crypto API.

## License

This project is open-source and available under the [MIT License](LICENSE).
