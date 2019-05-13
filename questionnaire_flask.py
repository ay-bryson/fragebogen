import os
import json

from flask import Flask, url_for, redirect, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('start'))


@app.route('/start', methods=['GET', 'POST'])
def start():
    if request.method == 'GET':
        context = {}
        context['users'] = [''.join(filename.split('.')[:-1]) for filename in os.listdir('./user_data')]
        print(context)
        return render_template('start.html', **context)

    elif request.method == 'POST':
        initiate_user(request.form)
        return redirect(url_for('fragen'))


@app.route('/fragen', methods=['GET', 'POST'])
def fragen():
    if request.method == 'GET':
        context = {}
        context['participant_id'] = get_participant_id()
        return render_template('fragen.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('gad7'))


@app.route('/gad7', methods=['GET', 'POST'])
def gad7():
    if request.method == 'GET':
        context = {}
        context['items'] = get_items('gad7')
        return render_template('gad7.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('phq9'))


@app.route('/phq9', methods=['GET', 'POST'])
def phq9():
    if request.method == 'GET':
        context = {}
        context['items'] = get_items('phq9')
        return render_template('phq9.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('bfi10'))


@app.route('/bfi10', methods=['GET', 'POST'])
def bfi10():
    if request.method == 'GET':
        context = {}
        context['items'] = get_items('bfi10')
        return render_template('bfi10.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('narq'))


@app.route('/narq', methods=['GET', 'POST'])
def narq():
    if request.method == 'GET':
        context = {}
        context['items'] = get_items('narq')
        return render_template('narq.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('empathy'))


@app.route('/empathy', methods=['GET', 'POST'])
def empathy():
    if request.method == 'GET':
        context = {}
        context['items'] = get_items('empathy')
        return render_template('empathy.html', **context)

    elif request.method == 'POST':
        process_post_data(request.form)
        return redirect(url_for('finished'))


@app.route('/finished')
def finished():
    return render_template('finished.html')


def get_items(items_label):
    with open('program_data/{}.txt'.format(items_label.upper()), 'r', encoding='utf-8') as items_file:
        items = items_file.readlines()
    items_dict = []

    i = 0
    is_required = '' if DEV_MODE else 'required'

    for item in items:
        items_dict.append({'text': item,
                           'label': items_label + '_' + str(i + 1),
                           'required': is_required})
        i += 1
    return items_dict


def process_post_data(form_data):
    participant_id = get_participant_id()
    new_entries = {}
    for key in form_data:
        new_entries[key] = form_data[key]
    with open('user_data/{}.json'.format(participant_id), 'r') as user_file:
        current_dict = json.load(user_file)
    for new_key in form_data:
        current_dict[new_key] = form_data[new_key]
    with open('user_data/{}.json'.format(participant_id), 'w') as user_file:
        json.dump(current_dict, user_file, indent=4)


def initiate_user(form_data):
    participant_id = form_data['participant_id']
    with open('user_data/{}.json'.format(participant_id), 'w') as new_user_file:
        json.dump(dict(), new_user_file)
    with open('user_data/current_user.txt', 'w') as current_user_file:
        current_user_file.write(participant_id)


def get_participant_id():
    with open('user_data/current_user.txt', 'r') as current_user_file:
        return current_user_file.read()


DEV_MODE = False


if __name__ == '__main__':
    app.run(debug=True)