
# RUSGen - Reddit User Summary Generator

This project is a Python script that utilizes the Reddit API (via the PRAW library) to retrieve a user's submission history and generates a summarized text using the BART (Bidirectional and AutoRegressive Transformers) model. The script saves the user data to a text file and appends the summarized text to another file. It provides a convenient way to analyze and summarize a user's Reddit activity.


## Installation

To run this project, follow these steps:

1. Clone the repository to your local machine using the following command:

```bash
  git clone https://github.com/RaymonDev/RUSGen
```

2. Create a virtual environment (optional but recommended) to keep the project dependencies isolated:
```
python -m venv myenv
```
3. Activate the virtual environment:
-  For Windows:
```bash
  myenv\Scripts\activate
```
- For Unix or Linux: 
```bash
 source myenv/bin/activate
```
4. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```
5. Edit the script and replace the Reddit API credentials (client_id, client_secret, user_agent, username, and password) with your own credentials. Ensure you have the necessary permissions to access the Reddit API.
6. Save the changes and execute the script:
```bash
python main.py
```

    
## Contributing

Contributions are always welcome!



## License

[MIT](https://choosealicense.com/licenses/mit/)

