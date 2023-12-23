from flask import Flask, render_template, request, redirect, url_for,session,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetings.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.secret_key ="random"
db = SQLAlchemy(app)

class Meeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    start_time = db.Column(db.String(12), nullable=False)
    end_time = db.Column(db.String(12), nullable=False)
    attendees = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<Meeting {self.title}>'

@app.route('/')
def index():
    meetings = Meeting.query.all()
    return render_template('index.html', meetings=meetings)

@app.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date'] 
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        attendees = request.form['attendees']
        new_meeting = Meeting(title=title, date=date, start_time=start_time, end_time=end_time, attendees=attendees)
        db.session.add(new_meeting)
        db.session.commit()
        flash('data successfully added', 'success')
        
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route('/update', methods=['POST', 'GET'])
def update():
    id = request.args.get('id')
    meeting = Meeting.query.get(id)

    if request.method == 'POST':
        if meeting:
            db.session.delete(meeting)
            db.session.commit()

            title = request.form['title']
            date = request.form['date']
            start_time = request.form['start_time']
            end_time = request.form['end_time']
            attendees = request.form['attendees']
            
            meeting = Meeting(id=id,title=title, date=date, start_time=start_time, end_time=end_time, attendees=attendees)
            db.session.add(meeting)
            db.session.commit()
        
        return redirect(url_for('index'))
    return render_template('update.html', meeting=meeting)




@app.route('/delete/<int:id>', methods=['POST', 'GET'])
def delete(id):
    meeting = Meeting.query.get(id)
    db.session.delete(meeting)
    db.session.commit()
    return redirect(url_for('index'))  

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)