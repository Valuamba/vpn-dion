import os.path
import os
from flask import Flask, send_file

app = Flask(__name__)


@app.route("/create_config/<image_id>")
def hello_world(image_id: str):
    pass


if __name__ == "__main__":
    port = int(os.environ.get('IMAGE_SERVER_PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)