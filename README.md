## JinjaPwn

`JinjaPwn` is a simple web-based offensive security tool used to generate, test, and validate malicious Jinja expressions for exploitation and red-team operations.


It is designed for security engineers and researchers who need quick access to payload generation during assessments and want to go beyound the trivial `{7*7}` SSTI validation via Jinja expressions.


## Features

- Web-based interface to craft Jinja expressions.
- Built-in payload templates for common attack scenarios such as:
  - Outbound connection tests
  - Command execution
  - File dropper + execution
  - AWS credential extraction (Boto3, Requests, urllib3)
- Docker support for fast deployment.
- CLI mode for quick local usage.


### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/mhaskar/JinjaPwn
   cd JinjaPwn
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Access it in your browser:
   ```
   http://127.0.0.1:5000
   ```

---

### Docker Setup

1. Build the Docker image:
   ```bash
   docker build -t jinja-pwn .
   ```

2. Run the container:
   ```bash
   docker run -p 5000:5000 jinja-pwn
   ```

3. Access the UI at:
   ```
   http://127.0.0.1:5000
   ```

---