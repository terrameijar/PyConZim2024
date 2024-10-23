from flask import Flask, jsonify, render_template,request
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, Transformer
from config import Config
from commands import populate_database


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()
    
app.cli.add_command(populate_database)

admin = Admin(app, name='transformers', template_mode='bootstrap4')
admin.add_view(ModelView(Transformer, db.session))

# API Endpoints


@app.route("/api/transformers/<name>")
def get_transformer(name):
    decoded_name = name.replace('%20', ' ')
    transformer = db.session.execute(db.select(Transformer).filter_by(name=decoded_name)).scalars().first()
    if transformer:
        return jsonify({
            'name': transformer.name,
            'affiliation': transformer.affiliation,
            'abilities': transformer.abilities,
            'transformation_mode': transformer.transformation_mode,
            'image_url': transformer.image_url,
            'description': transformer.description,
            'quote': transformer.quote
        })
    else:
        return jsonify({'error': 'Transformer not found'}), 404

@app.route('/api/transformers', methods=['GET'])
def get_transformers():
    """
    Retrieve a paginated list of Transformers (filter by name or affiliation)
    """
    name = request.args.get('name')
    affiliation = request.args.get('affiliation')
    page = request.args.get('page', 1, type=int)

    query = Transformer.query
    if name:
        query = query.filter(Transformer.name.ilike(f'%{name}%'))
    if affiliation:
        query = query.filter(Transformer.affiliation.ilike(f'%{affiliation}%'))
    
    transformers = query.paginate(page=page)
    

    return jsonify({
        'transformers': [
            {
                'name': bot.name,
                'affiliation': bot.affiliation,
                'abilities': bot.abilities,
                'transformation_mode': bot.transformation_mode,
                'image_url': bot.image_url,
                'description': bot.description,
                'quote': bot.quote
            } for bot in transformers.items
        ],
        'total_pages': transformers.pages,
        'page': transformers.page
    })

# HTML Views (User Facing Pages)


@app.route('/')
def list_all_transformers():
    """
    View Paginated list of Transformers
    """
    
    return render_template('index.html')


@app.route('/transformers/<name>')
def view_transformer(name):
    """
    View details of a Transformer using its name
    """
    return render_template('view.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)