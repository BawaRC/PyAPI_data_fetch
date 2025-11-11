# Python API Data Fetch Task

## 📄 About
This project is a simple Python script that fetches and displays user data from a public API.  
It demonstrates how to:
- Use the `requests` library to make GET API calls
- Handle JSON data
- Iterate through API responses
- Format and print data in a clean, readable structure
- Handle errors gracefully

---

## 🧠 Task Overview
The script calls the following endpoint:
```
https://jsonplaceholder.typicode.com/users
```

It retrieves a list of users and displays:
- Name  
- Username  
- Email  
- City  

It also includes an **optional bonus** feature that prints only users whose city name starts with the letter **‘S’**.

---

## 🧩 Requirements
Make sure you have Python 3 installed.

Install the required library:
```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/BawaRC/pyapi-data-fetch.git
   ```
2. Navigate into the project directory:
   ```bash
   cd pyapi-data-fetch
   ```
3. Run the script:
   ```bash
   python fetch_users.py
   ```

---

## 🧾 Example Output

```
User 1:
 Name: Leanne Graham
 Username: Bret
 Email: Sincere@april.biz
 City: Gwenborough
------------------------------
User 2:
 Name: Ervin Howell
 Username: Antonette
 Email: Shanna@melissa.tv
 City: Wisokyburgh
------------------------------

Optional Bonus
 ------------------------------
Users whose city name starts with 'S':
User 1:
 Name: Patricia Lebsack
 Username: Karianne
 Email: Julianne.OConner@kory.org
 City: South Elvis
------------------------------
User 2:
 Name: Mrs. Dennis Schulist
 Username: Leopoldo_Corkery
 Email: Karley_Dach@jasper.info
 City: South Christy
------------------------------
```

---

## 👨‍💻 Author
**Bawa Resume Chauhan**  
Python Developer & Data Science Enthusiast  
📧 [bawa101001@gmail.com]  
🌐 [https://github.com/BawaRC]
