
# ChatWhisper  
ChatWhisper: A Django-based backend API for real-time chat functionality, with a LLM running in the background  
  
## How to Run ChatWhisper  
  
### Prerequisites  
  
Before you begin, ensure you have the following installed on your system:  
- Python 3.10 or higher  
- pip (Python package installer)  
- Virtualenv (optional, but recommended for creating isolated Python environments)  
  
### Setting Up the Project  
  
1. **Clone the Repository**  
  
Clone the ChatWhisper repository to your local machine using:  
  
```bash  
https://github.com/Koenigsloewe/ChatWhisper_Backend.git  
cd ChatWhisper
```  

2. **Create and Activate a Virtual Environment (Optional)**  
  
If you're using virtualenv to create an isolated environment, execute:  
  
```bash  
virtualenv venv
```  
On Windows, activate the virtual environment with:  
  
```bash  
.\venv\Scripts\activate  
```  
  
On Unix or MacOS, use:  
  
```bash  
source venv/bin/activate
```  
Download the Llama LLM Model  
  
Download the Llama LLM model from [Hugging Face](https://huggingface.co/). After downloading, place the model in the ChatWhisper/llm_model folder within your project directory.  
  
This model is crucial for the AI-driven chat functionalities in ChatWhisper.  
  
3. **Configure the Environment Variables**  
  
Create a .env.local file in the root directory of the project to store your environment variables. Add the following attributes to the file, ensuring to replace placeholder values with your actual configuration details:  
  
```code  
DJANGO_SECRET_KEY="<your_django_secret_key_here>"  
DEBUG=True  
CORS_ALLOWED_ORIGINS=<your_cors_allowed_origins_here>  
AUTH_COOKIE_SECURE=False  
LLM_MODEL_ABSOLUTE_PATH=<your_llm_model_absolute_path_here>  
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000  
```  
  
4. **Install Dependencies**  
  
Install all required Python packages specified in requirements.txt:  
  
```bash  
pip install -r requirements.txt
```  
5. **Run Migrations**  
  
Initialize your database schema:  
  
```bash  
python manage.py makemigrationspython manage.py migrate
```  
6. **Run the Development Server**  
  
Start the Django development server:  
  
```bash  
python manage.py runserver  
```  
  
The server will start running on http://127.0.0.1:8000/. You can now access the API endpoints as defined in your project's URL configurations.  
  
7. **Testing the Application**  
  
To ensure everything is set up correctly, you might want to create a superuser and access the Django admin site:  
  
```bash  
python manage.py createsuperuser
```  
Follow the prompts to create a user, then navigate to http://127.0.0.1:8000/admin/ and log in with your new user credentials.
