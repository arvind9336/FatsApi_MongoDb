import os
from dotenv import load_dotenv
load_dotenv()
MONGODB_URI=os.getenv("MONGODB_URI")
MONGODB_DB=os.getenv("DATABASE_NAME")