from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('enter_number.html')  # First page: Select condition

@app.route('/condition', methods=['POST'])
def condition():
    # Get which button was clicked (Condition 1 or 2)
    condition_choice = request.form['condition']
    
    # Redirect to the page for the selected condition
    if condition_choice == '1':
        return redirect(url_for('condition1'))
    elif condition_choice == '2':
        return redirect(url_for('condition2'))

@app.route('/condition1')
def condition1():
    return render_template('condition_page.html', condition="1")

@app.route('/condition2')
def condition2():
    return render_template('condition_page.html', condition="2")

@app.route('/video/<condition>/<part>')
def video(condition, part):
    # Build the filename dynamically based on condition and part
    video_file = f"cond{condition}_part{part}.mp4"
    return render_template('video_viewer.html', video_file=video_file)

if __name__ == "__main__":
    # Explicitly bind the app to 0.0.0.0 and port 5000 for Render deployment
    app.run(debug=True, host="0.0.0.0", port=5000)
