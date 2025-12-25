from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from azure.storage.blob import BlobServiceClient
from azure.cosmos import CosmosClient
import uuid, os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ---------------- AZURE ----------------
from dotenv import load_dotenv
load_dotenv()

BLOB_CONN = os.getenv("BLOB_CONN")
COSMOS_URI = os.getenv("COSMOS_URI")
COSMOS_KEY = os.getenv("COSMOS_KEY")

blob = BlobServiceClient.from_connection_string(BLOB_CONN)
container = blob.get_container_client("images")

cosmos = CosmosClient(COSMOS_URI, COSMOS_KEY)
db = cosmos.get_database_client("imageGalleryDB")
col = db.get_container_client("images")
# --------------------------------------

# ---------- Upload ----------
@app.route("/upload", methods=["POST"])
def upload():
    f = request.files["image"]
    title = request.form.get("title","")
    tags = request.form.get("tags","")

    name = str(uuid.uuid4()) + "_" + f.filename

    # Upload to Azure Blob
    container.upload_blob(name, f, overwrite=True)

    # Public cloud URL
    url = container.url + "/" + name

    # Save metadata in Cosmos
    col.create_item({
        "id": name,
        "url": url,
        "title": title,
        "tags": tags
    })

    return jsonify({"msg":"Upload successful"})

# ---------- Load Gallery ----------
@app.route("/images")
def images():
    return jsonify(list(col.read_all_items()))

# ---------- Serve Local Fallback ----------
@app.route("/uploads/<filename>")
def serve_upload(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# -----------------------------------
app.run(host="0.0.0.0", port=5000)
