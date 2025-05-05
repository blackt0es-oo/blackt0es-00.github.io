from flask import Flask, request, render_template



app=Flask(__name__)
history = []

class Task:
    def __init__(self, action, due):
        self.action=action
        self.due=due
    
    def format(self):
        return [self.action,self.due]




@app.route('/', methods=['GET','POST'])
def backend():
    global history
    
    if request.method == 'POST':
        action = request.form['action']
        due = request.form['due']
        task=Task(action=action, due=due).format()
        history.append(task)
        
    
    print(history)       
    return render_template('index.html', history=history)


if __name__ == "__main__":
    app.run(debug=True)
