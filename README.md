# engage_bay_knowledge_base

Instructions:
I have added a file named "GPT API" that allows you to simply deploy this API locally 

Download both files and unzip the knowledge base text files.


Change these two variables in the code as per your requirements,Open ai api key and directory(directory for knowledge base files)


1)Installing the necessary packages. Run these commands on terminal to install the necessary packages.


pip install gpt-index
pip install fastapi
pip install openai



2) Copypasting this in the terminal 
uvicorn API:app --port 8000 --reload

3) It is creating embeddings so it will take some time to load initially.. About 30 seconds or so

4) Then once it says its deployed in a local session you can copy paste this link.

http://127.0.0.1:8000/predict?input_text=what is a smart list?

5) Once you have retreived the index.json file once, it will appear in local directory, you dont have to do it again and you can delete this part of the code that hogs memory:

index = construct_index("docs")







