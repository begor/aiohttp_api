import views

def setup_routes(app):
    app.router.add_get('/api/v1/notes', views.notes_index)
