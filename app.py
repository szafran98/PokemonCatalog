from flask import Flask, render_template, request, redirect, url_for
import pokemons

app = Flask(__name__)
cards_to_show = 4
pokemons_json = [{'name':poke.name, 'number':poke.number, 'image_url':poke.image_url, 'supertype':poke.supertype,
             'subtype':poke.subtype, 'rarity':poke.rarity} for poke in pokemons.pokemons_list]

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html', data=pokemons_json[:cards_to_show])

@app.route('/more')
def load_more():
    global cards_to_show
    cards_to_show += 4
    return redirect(url_for('home_page', _method='GET'))

@app.route('/search', methods=['POST', 'GET'])
def search_by_name():
    text = request.form['text']
    for poke in pokemons.pokemons_list:
        returned = poke.return_by_name(text)
        if returned != None:
            global cards_to_show
            cards_to_show = 0
            data = [{'name':returned.name, 'number':returned.number, 'image_url':returned.image_url, 'supertype':returned.supertype,
             'subtype':returned.subtype, 'rarity':returned.rarity}]
            return render_template('index.html', data=data)
    return redirect(url_for('home_page', _method='GET'))

if __name__ == '__main__':
    app.run()
