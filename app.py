import os
from textwrap import wrap
import matplotlib.pyplot as plt
from flask import Flask, request, render_template, send_file
from hades import hades

new_graph_name = ''
symbol_list = ["▚ ▞", "■ □", "♥ ♡", "⚉ ⚇", "★ ☆", "◆ ◇", "◰ ◲", "◤ ◸", "● ○"]

app = Flask(__name__)


def return_code(hash):
    code_string = ''
    big_list = []
    bigg_list = []
    bin_list = [bin(int(i, 16))[2:].zfill(8) for i in wrap(hash, 2)]
    for i in range(8):
        for items in bin_list:
            big_list.append(items[i])
        bigg_list.append(''.join(big_list))
        big_list = []
    for items in bigg_list:
        items = items.replace('1', symbol_list[1].split()[0] + " ")
        items = items.replace('0', symbol_list[1].split()[1] + " ")
        code_string += items + "\n"
    return code_string


@app.route('/', methods=['GET', 'POST'])
def get_hash():
    global new_graph_name
    if request.method == 'POST':
        seed_phrase = request.form.get("hash")
        if seed_phrase == '':
            seed_phrase = '00007e10107e007e0000'
        try:
            code_string = return_code(seed_phrase)
            hash = seed_phrase
        except ValueError:
            h = hades.Hades(seed=seed_phrase)
            hash = h.single_hash()
            code_string = return_code(hash)
        fig, ax = plt.subplots(figsize=(5, 3))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.text(0.1, 0.45, code_string, horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
        plt.axis('off')
        new_graph_name = f"graph_{hash}.jpg"
        for filename in os.listdir('static/'):
            if filename.startswith('graph_'):  # not to remove other images
                os.remove('static/' + filename)
        plt.savefig('static/' + new_graph_name, bbox_inches='tight', pad_inches=0)
        s = hash
    else:
        s = None
    return render_template("view.html", s=s, graph=new_graph_name)


@app.route('/api/<hash>', methods=['GET', 'POST'])
def api(hash):
    global new_graph_name, file_name
    if request.method == 'GET':
        seed_phrase = hash
        if seed_phrase == '':
            seed_phrase = '00007e10107e007e0000'
        try:
            code_string = return_code(seed_phrase)
            hash = seed_phrase
        except ValueError:
            h = hades.Hades(seed=seed_phrase)
            hash = h.single_hash()
            code_string = return_code(hash)
        fig, ax = plt.subplots(figsize=(5, 3))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.text(0.1, 0.45, code_string, horizontalalignment='left', verticalalignment='center', transform=ax.transAxes)
        plt.axis('off')
        new_graph_name = f"graph_{hash}.jpg"
        for filename in os.listdir('static/'):
            if filename.startswith('graph_'):  # not to remove other images
                os.remove('static/' + filename)
        plt.savefig('static/' + new_graph_name, bbox_inches='tight', pad_inches=0)
        file_name = 'static/' + new_graph_name
        return send_file(file_name, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True)
