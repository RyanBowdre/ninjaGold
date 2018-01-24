from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'jkhkjhkjhkj'
import random



@app.route('/')
def total_gold():
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'activity_message_list' not in session:
        session['activity_message_list'] = []
    return render_template("ninja_gold.html")


@app.route('/')
def index():
    return render_template("ninja_gold.html")


@app.route('/process_money', methods = ['POST'])
def gold_maker1():
    find_gold = request.form['building']
    print find_gold
    if find_gold == 'farm':
        session['random_gold1'] = random.randrange(10, 21)
        session['total_gold'] = session['total_gold'] + session['random_gold1']
        activity_message = "Earned {} from the {}!".format(session['random_gold1'], find_gold)
        session['activity_message_list'].append(activity_message)
        print session['random_gold1']
        print session['total_gold']
        print (session['activity_message_list'])
        return redirect ("/")

    elif find_gold == 'cave':
        session['random_gold2'] = random.randrange(5, 11)
        session['total_gold'] = session['total_gold'] + session['random_gold2']
        activity_message = "Earned {} from the {}!".format(session['random_gold2'], find_gold)
        session['activity_message_list'].append(activity_message)
        print session['random_gold2']
        print session['total_gold']
        print (session['activity_message_list'])
        return redirect ("/")

    elif find_gold == 'house':
        session['random_gold3'] = random.randrange(2, 6)
        session['total_gold'] = session['total_gold'] + session['random_gold3']
        activity_message = "Earned {} from the {}!".format(session['random_gold3'], find_gold)
        session['activity_message_list'].append(activity_message)
        print session['total_gold']
        print (session['activity_message_list'])
        return redirect ("/")

    elif find_gold == 'casino':
        session['random_gold4'] = random.randrange(-50, 51)
        session['total_gold'] = session['total_gold'] + session['random_gold4']
        if session['random_gold4'] > 0:
            activity_message = "Entered the casino and gained {} gold...Awesome!".format(session['random_gold4'])
            session['activity_message_list'].append(activity_message)
        elif session['random_gold4'] < 0:
            activity_message = "Entered the casino and lost {} gold...Ouch!".format((session['random_gold4'] * -1))
            session['activity_message_list'].append(activity_message)
        print session['random_gold4']
        print session['total_gold']
        print (session['activity_message_list'])
        return redirect ("/")

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect ("/")

app.run(debug=True)


# find_gold = request.form['building']
# print find_gold
# if find_gold == 'farm':
#     session['random_gold1'] = random.randrange(10, 21)
# elif find_gold == 'cave':
#     session['random_gold1'] = random.randrange(5, 11)
