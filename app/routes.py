import views

def setup_routes(app):
    app.router.add_route('*', '/api/notes', views.NoteView)
