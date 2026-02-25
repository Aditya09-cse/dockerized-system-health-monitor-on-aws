from flask import Flask, request
import psutil

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def check_system_health():
    if request.method == "POST":
        cpu_threshold = int(request.form["cpu"])
        disk_threshold = int(request.form["disk"])
        memory_threshold = int(request.form["memory"])

        current_cpu = psutil.cpu_percent(interval=1)
        disk_usage = psutil.disk_usage('/').percent
        memory_usage = psutil.virtual_memory().percent

        def get_status(value, threshold):
            return ("Alert 🚨", "danger") if value > threshold else ("Safe ✅", "safe")

        cpu_status, cpu_class = get_status(current_cpu, cpu_threshold)
        disk_status, disk_class = get_status(disk_usage, disk_threshold)
        memory_status, memory_class = get_status(memory_usage, memory_threshold)

        return f"""
        <html>
        <head>
            <title>System Health Dashboard</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #1e3c72, #2a5298);
                    color: white;
                    text-align: center;
                    padding: 40px;
                }}
                .container {{
                    background: white;
                    color: #333;
                    padding: 30px;
                    border-radius: 15px;
                    max-width: 600px;
                    margin: auto;
                    box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
                }}
                h1 {{
                    margin-bottom: 20px;
                }}
                .metric {{
                    margin: 15px 0;
                    font-size: 18px;
                    padding: 10px;
                    border-radius: 8px;
                }}
                .safe {{
                    background-color: #d4edda;
                    color: #155724;
                }}
                .danger {{
                    background-color: #f8d7da;
                    color: #721c24;
                }}
                button {{
                    margin-top: 20px;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 8px;
                    background-color: #2a5298;
                    color: white;
                    font-size: 16px;
                    cursor: pointer;
                }}
                button:hover {{
                    background-color: #1e3c72;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>System Health Dashboard</h1>

                <div class="metric {cpu_class}">
                    CPU Usage: {current_cpu}% → {cpu_status}
                </div>

                <div class="metric {disk_class}">
                    Disk Usage: {disk_usage}% → {disk_status}
                </div>

                <div class="metric {memory_class}">
                    Memory Usage: {memory_usage}% → {memory_status}
                </div>

                <form action="/">
                    <button>Check Again</button>
                </form>
            </div>
        </body>
        </html>
        """

    return """
    <html>
    <head>
        <title>System Health Input</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #1e3c72, #2a5298);
                color: white;
                text-align: center;
                padding: 50px;
            }
            .form-container {
                background: white;
                color: #333;
                padding: 30px;
                border-radius: 15px;
                max-width: 500px;
                margin: auto;
                box-shadow: 0px 10px 25px rgba(0,0,0,0.3);
            }
            input {
                width: 80%;
                padding: 10px;
                margin: 10px 0;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            button {
                padding: 10px 20px;
                border: none;
                border-radius: 8px;
                background-color: #2a5298;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #1e3c72;
            }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h1>Enter Threshold Values</h1>
            <form method="post">
                <input type="number" name="cpu" placeholder="CPU Threshold (%)" required><br>
                <input type="number" name="disk" placeholder="Disk Threshold (%)" required><br>
                <input type="number" name="memory" placeholder="Memory Threshold (%)" required><br>
                <button type="submit">Check System</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
