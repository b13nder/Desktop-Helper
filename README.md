This is a desktop application that uses OpenAI ChatGPT to get more information about the text and concepts you are looking at. The application takes a screenshot, extracts all text, and uses it as a context to ask a question to ChatGPT. This way, your query is more precise and you get much more detailed responses from ChatGPT ex
<img width="1510" alt="ex" src="https://github.com/b13nder/AI_Helper/assets/85758111/b9df3c70-68a2-43ff-a8d1-f4b782b99050">


To make everything work, you need to insert your Open AI API key into the file backend/main.py, line 10.

Dependencies: "axios": "^1.4.0", "electron": "^0.0.1-security", "electron": "^25.2.0", "electron-screenshot": "^1.0.5", "form-data": "^4.0.0", "fs": "^0.0.1-security", "lodash": "^4.17.21", "path": "^0.12.7", "tesseract.js": "^4.1.1"

How to install an d use: First, download the archive from GitHub. Open the "back-end" folder and run the file in the terminal using "python3 main.py". Then, open the "frontend" folder in a separate terminal window and execute the command "npm install" to install the required packages and libraries. After that, enter the command "npm start", and the project will be up and ready to work!
