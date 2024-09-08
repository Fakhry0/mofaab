from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from flask_mail import Message
from app import mail
from threading import Thread

contact_bp = Blueprint('contact', __name__)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message(subject=f"Contact Form: {name}",
                      sender=email,
                      recipients=['alylolo223344@gmail.com'],
                      body=message)
        try:
            Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
            flash('Your message has been sent!', 'success')
        except Exception as e:
            flash(f'An error occurred while sending your message: {str(e)}', 'danger')
        
        return redirect(url_for('contact.contact'))
    
    return render_template('contact.html')
