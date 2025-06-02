from flask import Flask, request
import logging
import time

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route("/")
def home():
    logging.info("Received request at /")
    return "Welcome to the Python Docker App!"

@app.route("/health")
def health():
    logging.info("Health check passed")
    return "OK"

@app.route("/echo", methods=["POST"])
def echo():
    data = request.json
    logging.info(f"Received data: {data}")
    return {"received": data}

@app.route("/simulate-error")
def error():
    logging.error("Simulated error triggered!")
    return "Error!", 500

if __name__ == "__main__":
    logging.info("Starting Flask app...")
    time.sleep(1)
    app.run(host="0.0.0.0", port=5000)



# curl http://localhost:5000/
# curl http://localhost:5000/health
# curl -X POST http://localhost:5000/echo -H "Content-Type: application/json" -d '{"msg": "hello"}'
# curl http://localhost:5000/simulate-error
