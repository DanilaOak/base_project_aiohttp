from .views import get_version, create_user

def setup_routes(app):
    # Get
    app.router.add_get('/api/version', get_version, allow_head=False)
    # Post
    app.router.add_post('/api/v1/users', create_user)