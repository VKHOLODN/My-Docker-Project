from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Hosting Example</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f4f4f9;
                color: #333;
                padding: 20px;
                margin: 0;
            }
            h1 {
                color: #4CAF50;
                margin-top: 50px;
            }
            p {
                font-size: 18px;
                margin-top: 20px;
            }
            .footer {
                margin-top: 50px;
                font-size: 14px;
                color: #777;
            }
        </style>
    </head>
    <body>
        <h1>Vladyslav Kholodnitskyi</h1>
        <p>Hosting Example</p>
        <div class="footer">
            &copy; 2024 Vladyslav Kholodnitskyi
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)